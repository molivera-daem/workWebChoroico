from ..database.supabase_client import get_supabase_client

class SupabaseService:
    def __init__(self):
        self.client = get_supabase_client()

    def get_all_news(self):
        """Obtiene todas las noticias ordenadas por fecha de creación descendente."""
        try:
            response = self.client.table("news").select("*").order("created_at", desc=True).execute()
            return response.data
        except Exception as e:
            print(f"Error al obtener noticias: {e}")
            return []

    def get_gallery_items(self):
        """Obtiene todos los elementos de la galería."""
        try:
            response = self.client.table("gallery").select("*").order("created_at", desc=True).execute()
            return response.data
        except Exception as e:
            print(f"Error al obtener galería: {e}")
            return []

    def create_news_item(self, title, content, image_url):
        """Crea una nueva noticia en la tabla news."""
        try:
            data = {
                "title": title,
                "content": content,
                "image_url": image_url
            }
            response = self.client.table("news").insert(data).execute()
            return response.data
        except Exception as e:
            print(f"Error al crear noticia: {e}")
            return None

    def upload_file(self, bucket_name: str, file_path: str, destination_path: str):
        """Sube un archivo al Storage y retorna su URL pública."""
        try:
            with open(file_path, 'rb') as f:
                self.client.storage.from_(bucket_name).upload(
                    path=destination_path,
                    file=f,
                    file_options={"content-type": "image/jpeg"}
                )
            
            # Obtener la URL pública
            url_response = self.client.storage.from_(bucket_name).get_public_url(destination_path)
            return url_response
        except Exception as e:
            if "already exists" in str(e):
                return self.client.storage.from_(bucket_name).get_public_url(destination_path)
            print(f"Error al subir archivo {file_path}: {e}")
            return None

    def create_gallery_item(self, title, category, image_url):
        """Crea un registro en la tabla gallery."""
        try:
            data = {
                "title": title,
                "category": category,
                "image_url": image_url
            }
            response = self.client.table("gallery").insert(data).execute()
            return response.data
        except Exception as e:
            print(f"Error al crear registro en galería: {e}")
            return None
