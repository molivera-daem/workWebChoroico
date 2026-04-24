import sys
import os

# Añadir el directorio raíz al path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from WebChoroico.core.services.supabase_service import SupabaseService

def migrate():
    service = SupabaseService()
    bucket = "assets"
    
    print(f"--- 🚀 Iniciando Migración de Imágenes a Supabase ---")
    
    # Intentar crear el bucket (esto puede fallar si ya existe o no hay permisos de admin)
    try:
        service.client.storage.create_bucket(bucket, options={"public": True})
        print(f"✅ Bucket '{bucket}' creado.")
    except Exception:
        print(f"ℹ️ El bucket '{bucket}' ya existe o se requiere creación manual.")

    images_to_upload = [
        {
            "local": "WebChoroico/core/static/img/branch/escuela_aurora_principal.jpg",
            "remote": "escuela_aurora_principal.jpg",
            "title": "Frontis Escuela Aurora de Chile",
            "cat": "Infraestructura"
        },
        {
            "local": "WebChoroico/core/static/img/branch/historia_escuela_aurora.jpg",
            "remote": "historia_escuela_aurora.jpg",
            "title": "Nuestra Historia",
            "cat": "Institucional"
        },
        {
            "local": "WebChoroico/core/static/img/branch/logo_aurora_chile.jpeg",
            "remote": "logo_aurora_chile.jpeg",
            "title": "Escudo Institucional",
            "cat": "Identidad"
        }
    ]

    for img in images_to_upload:
        if os.path.exists(img["local"]):
            print(f"Subiendo {img['remote']}...")
            public_url = service.upload_file(bucket, img["local"], img["remote"])
            
            if public_url:
                print(f"✅ Subida exitosa. URL: {public_url}")
                print(f"Creando registro en base de datos...")
                service.create_gallery_item(img["title"], img["cat"], public_url)
            else:
                print(f"❌ Falló la subida de {img['remote']}")
        else:
            print(f"⚠️ No se encontró el archivo local: {img['local']}")

    print("--- ✨ Proceso Finalizado ---")

if __name__ == "__main__":
    migrate()
