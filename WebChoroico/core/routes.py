"""
@file core/routes.py
@description Definición de las rutas principales del sitio web.
@author Miguel Olivera Labrin
"""

from flask import Blueprint, render_template
from .services.supabase_service import SupabaseService

main = Blueprint('main', __name__)
supabase_service = SupabaseService()

@main.route('/')
def home():
    """
    Ruta principal (Home).
    Renderiza la plantilla index.html con las noticias más recientes.
    """
    # TSK-010: Obtención dinámica de noticias para el preview del Home
    news_items = supabase_service.get_all_news()
    return render_template('index.html', news=news_items)

@main.route('/about-us')
def about_us():
    """
    Ruta 'Quiénes Somos'.
    Renderiza la plantilla about_us.html con el contenido correspondiente.
    """
    # TSK-001: Refactorización a Application Factory
    return render_template('about_us.html', section="Quiénes Somos", icon="fa-users")

@main.route('/news')
def news():
    """
    Ruta de 'Noticias'.
    Muestra un feed de noticias institucionales con datos de Supabase.
    """
    # TSK-010: Obtención dinámica de noticias desde Supabase
    news_items = supabase_service.get_all_news()
    return render_template('news.html', section="Noticias", icon="fa-newspaper", news=news_items)

@main.route('/news/<news_id>')
def news_detail(news_id):
    """
    Muestra el detalle de una noticia y su galería asociada.
    """
    item = supabase_service.get_news_by_id(news_id)
    if not item:
        return "Noticia no encontrada", 404
        
    # Si es la noticia de Color Run, cargamos las imágenes de su carpeta
    images = []
    if "Color Run" in item['title']:
        images = supabase_service.get_news_images("Color Run")
        
    return render_template('news_detail.html', news=item, images=images)

@main.route('/gallery')
def gallery():
    """
    Vista principal de la Galería.
    Muestra una foto de portada por cada actividad/álbum, filtrando logos y vacíos.
    """
    gallery_items = supabase_service.get_gallery_items()
    
    # IDs a excluir (Logos y duplicados antiguos)
    excluded_ids = [
        "0da262ed-365c-4f5e-919a-c06a79753b98", # Logo
        "8d1d80ae-04f0-47a9-8602-6920beed90ba", # Logo duplicado
        "b28505a6-b854-4e75-9c21-eed0c3330d3c", # Duplicado frontis
    ]
    
    # Función para normalizar categorías
    import unicodedata
    def normalize_cat(s):
        if not s: return "OTROS"
        s = s.upper()
        return ''.join(c for c in unicodedata.normalize('NFD', s)
                      if unicodedata.category(c) != 'Mn')

    # 1. Agrupar TODAS las fotos por categoría normalizada
    albums_data = {}
    for p in gallery_items:
        if p['id'] in excluded_ids or "logo" in p['image_url'].lower():
            continue
            
        cat_norm = normalize_cat(p.get('category'))
        if cat_norm not in albums_data:
            albums_data[cat_norm] = []
        albums_data[cat_norm].append(p)

    # 2. Seleccionar la mejor portada para cada álbum
    final_albums = {}
    for cat_norm, photos in albums_data.items():
        # Intentamos encontrar la primera foto que NO sea placeholder y NO termine en -0
        best_photo = None
        for p in photos:
            is_placeholder = p['image_url'] == "/static/img/placeholder.jpg"
            is_zero = p['image_url'].split('/')[-1].split('.')[0].endswith(('_0', '-0'))
            
            if not is_placeholder and not is_zero:
                best_photo = p
                break
        
        # Si no encontramos una "perfecta", tomamos la primera que no sea placeholder
        if not best_photo:
            for p in photos:
                if p['image_url'] != "/static/img/placeholder.jpg":
                    best_photo = p
                    break
        
        # Si aún no hay nada (todo es placeholder), tomamos la primera disponible
        if not best_photo and photos:
            best_photo = photos[0]
            
        if best_photo:
            best_photo['display_category'] = best_photo.get('category', cat_norm)
            final_albums[cat_norm] = best_photo
            
    return render_template('gallery.html', 
                           section="Galería", 
                           icon="fa-images", 
                           albums=final_albums)

@main.route('/gallery/<category>')
def gallery_album(category):
    """
    Vista de detalle de un álbum específico.
    """
    all_items = supabase_service.get_gallery_items()
    
    # Función para normalizar categorías (Remover acentos y pasar a mayúsculas)
    import unicodedata
    def normalize_cat(s):
        if not s: return "OTROS"
        s = s.upper()
        return ''.join(c for c in unicodedata.normalize('NFD', s)
                      if unicodedata.category(c) != 'Mn')

    # Filtrar solo fotos válidas de esta categoría (comparando normalizados)
    target_norm = normalize_cat(category)
    
    album_photos = [
        p for p in all_items 
        if normalize_cat(p.get('category')) == target_norm
        and p['image_url'] != "/static/img/placeholder.jpg"
        and "logo" not in p['image_url'].lower()
        and not p['image_url'].split('/')[-1].split('.')[0].endswith(('_0', '-0'))
    ]
    
    if not album_photos:
        return "Álbum no encontrado", 404
        
    # Usamos el nombre de la categoría del primer elemento para el título
    display_name = album_photos[0].get('category', category)
    
    return render_template('gallery_album.html', 
                           section="Galería", 
                           category=display_name, 
                           photos=album_photos)

@main.route('/personal')
def staff():
    """
    Ruta de 'Personal'.
    Muestra la lista de funcionarios del establecimiento.
    """
    staff_members = supabase_service.get_staff()
    return render_template('staff.html', section="Personal", icon="fa-user-tie", staff=staff_members)

