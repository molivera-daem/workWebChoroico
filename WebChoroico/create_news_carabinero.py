import os
import sys

# Agregar el directorio al path
path = os.path.dirname(os.path.abspath(__file__))
if path not in sys.path:
    sys.path.append(path)

from core.services.supabase_service import SupabaseService

def create_carabinero_news():
    service = SupabaseService()
    
    title = "Conmemoración del Día del Carabinero"
    content = "Próximamente se agregará el detalle de la actividad realizada en nuestra escuela en honor al Día del Carabinero."
    # Placeholder de imagen por ahora
    image_url = "https://images.unsplash.com/photo-1593033583907-de1e123cab31?ixlib=rb-1.2.1&auto=format&fit=crop&w=800&q=80"
    
    print(f"🚀 Creando noticia: {title}...")
    result = service.create_news_item(title, content, image_url)
    
    if result:
        print("✅ Noticia creada exitosamente en Supabase!")
    else:
        print("❌ Error al crear la noticia. Verifica la conexión y los campos de la tabla.")

if __name__ == "__main__":
    create_carabinero_news()
