import os
import sys

path = os.path.dirname(os.path.abspath(__file__))
if path not in sys.path:
    sys.path.append(path)

from core.services.supabase_service import SupabaseService

def cleanup_and_recreate():
    service = SupabaseService()
    
    print("🧹 Limpiando noticias antiguas de Supabase...")
    # Eliminamos todas las noticias existentes para limpiar ejemplos
    try:
        service.client.table("news").delete().neq("id", "00000000-0000-0000-0000-000000000000").execute()
        print("✅ Noticias antiguas eliminadas.")
    except Exception as e:
        print(f"⚠️ Error al limpiar (puede que no haya noticias): {e}")

    # Re-creamos la noticia del Carabinero con la foto del storage
    title = "Conmemoración del Día del Carabinero"
    content = "Nuestra comunidad escolar realizó una emotiva ceremonia para conmemorar el Día del Carabinero, destacando su labor y compromiso con la seguridad de nuestro país. Los estudiantes participaron con actos artísticos y palabras de agradecimiento."
    image_url = "https://mfcjgbnwfvphnsqeytrx.supabase.co/storage/v1/object/public/assets/noticias/carabineros/WhatsApp%20Image%202026-04-28%20at%2015.13.35%20(1).jpeg"
    
    print(f"🚀 Creando noticia oficial: {title}...")
    result = service.create_news_item(title, content, image_url)
    
    if result:
        print("✅ Noticia oficial creada exitosamente!")
    else:
        print("❌ Error al crear la noticia.")

if __name__ == "__main__":
    cleanup_and_recreate()
