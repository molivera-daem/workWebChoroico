"""
@file core/routes.py
@description Definición de las rutas principales del sitio web.
@author Miguel Olivera Labrin
"""

from flask import Blueprint, render_template
from WebChoroico.core.services.supabase_service import SupabaseService

main = Blueprint('main', __name__)
supabase_service = SupabaseService()

@main.route('/')
def home():
    """
    Ruta principal (Home).
    Renderiza la plantilla index.html.
    """
    # TSK-001: Implementación inicial
    return render_template('index.html')

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

@main.route('/gallery')
def gallery():
    """
    Ruta de 'Galería'.
    Muestra una galería fotográfica institucional con datos de Supabase.
    """
    # TSK-010: Obtención dinámica de galería desde Supabase
    gallery_items = supabase_service.get_all_news() # Se usa get_gallery_items en realidad, corregiré en el servicio si es necesario
    gallery_items = supabase_service.get_gallery_items()
    return render_template('gallery.html', section="Galería", icon="fa-images", photos=gallery_items)

