import os
import sys

path = os.path.dirname(os.path.abspath(__file__))
if path not in sys.path:
    sys.path.append(path)

from core.services.supabase_service import SupabaseService

def update_news_with_photos():
    service = SupabaseService()
    # Probaremos varios buckets comunes si es necesario
    buckets_to_try = ["news-images", "images", "assets", "gallery"]
    folder_path = "noticias/carabineros"
    
    files = []
    found_bucket = None
    
    for bucket in buckets_to_try:
        print(f"🔍 Buscando en bucket '{bucket}'...")
        try:
            res = service.list_files(bucket, folder_path)
            if res and len(res) > 0:
                files = res
                found_bucket = bucket
                break
        except:
            continue

    if not files:
        print(f"❌ No se encontraron archivos en '{folder_path}' en ninguno de los buckets conocidos.")
        return

    photo_urls = []
    for f in files:
        if isinstance(f, dict) and 'name' in f and not f['name'].startswith('.'):
            full_path = f"{folder_path}/{f['name']}"
            url = service.get_public_url(found_bucket, full_path)
            if url:
                photo_urls.append(url)

    if not photo_urls:
        print("❌ No se pudieron generar URLs para las fotos.")
        return

    print(f"✅ Se encontraron {len(photo_urls)} fotos en el bucket '{found_bucket}'.")
    
    main_image = photo_urls[0]
    
    try:
        print("📝 Buscando noticia 'Conmemoración del Día del Carabinero'...")
        news_response = service.client.table("news").select("*").eq("title", "Conmemoración del Día del Carabinero").execute()
        
        if news_response.data:
            news_id = news_response.data[0]['id']
            # Actualizamos la noticia con la primera imagen encontrada
            service.client.table("news").update({"image_url": main_image}).eq("id", news_id).execute()
            print(f"✅ Noticia actualizada con la imagen: {main_image}")
        else:
            print("❌ No se encontró la noticia para actualizar.")
            
    except Exception as e:
        print(f"❌ Error al actualizar la base de datos: {e}")

if __name__ == "__main__":
    update_news_with_photos()
