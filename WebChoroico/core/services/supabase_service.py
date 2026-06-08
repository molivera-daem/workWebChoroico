from ..database.supabase_client import get_supabase_client

class SupabaseService:
    def __init__(self):
        self.client = get_supabase_client()
        # IDs de noticias que deben ser excluidas (por ejemplo, si no se pueden borrar por permisos)
        self.excluded_news_ids = [
            "892b22fe-7e12-4fe1-a801-a4deda9c50c2"  # Proceso de Matrículas 2026
        ]

    def get_all_news(self):
        """Obtiene todas las noticias ordenadas por fecha de creación descendente."""
        try:
            response = self.client.table("news").select("*").order("created_at", desc=True).execute()
            # Filtrar noticias excluidas
            filtered_news = [item for item in response.data if item.get('id') not in self.excluded_news_ids]
            return filtered_news
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

    def list_files(self, bucket_name: str, path: str):
        """Lista los archivos en un bucket y path específicos."""
        try:
            return self.client.storage.from_(bucket_name).list(path)
        except Exception as e:
            print(f"Error al listar archivos en {bucket_name}/{path}: {e}")
            return []

    def get_public_url(self, bucket_name: str, file_path: str):
        """Obtiene la URL pública de un archivo."""
        try:
            res = self.client.storage.from_(bucket_name).get_public_url(file_path)
            # El cliente de python de supabase a veces retorna un string o un objeto con la url
            if isinstance(res, str):
                return res
            return res.get('publicURL') or res # Ajuste según versión de la librería
        except Exception as e:
            print(f"Error al obtener URL pública: {e}")
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

    def get_news_by_id(self, news_id):
        """Obtiene una noticia específica por su ID."""
        try:
            response = self.client.table("news").select("*").eq("id", news_id).single().execute()
            return response.data
        except Exception as e:
            print(f"Error al obtener noticia {news_id}: {e}")
            return None

    def delete_news_by_title_pattern(self, pattern):
        """Elimina noticias cuyo título coincida con el patrón."""
        try:
            # Primero buscamos para confirmar qué vamos a borrar
            search_query = self.client.table("news").select("id, title").ilike("title", f"%{pattern}%").execute()
            items_to_delete = search_query.data
            
            if not items_to_delete:
                print(f"No se encontraron noticias con el patrón: {pattern}")
                return 0
                
            print(f"Se eliminarán {len(items_to_delete)} noticias: {[item['title'] for item in items_to_delete]}")
            
            # Procedemos a eliminar
            response = self.client.table("news").delete().ilike("title", f"%{pattern}%").execute()
            return len(items_to_delete)
        except Exception as e:
            print(f"Error al eliminar noticias: {e}")
            return 0

    def get_news_images(self, folder_name):
        """Obtiene todas las URLs de imágenes de una carpeta específica en storage."""
        try:
            bucket_name = "assets"
            path = f"noticias/{folder_name}"
            files = self.client.storage.from_(bucket_name).list(path)
            
            urls = []
            for f in files:
                if f['name'] != '.emptyFolderPlaceholder':
                    res = self.client.storage.from_(bucket_name).get_public_url(f"{path}/{f['name']}")
                    url = res if isinstance(res, str) else res.get('publicURL')
                    urls.append(url)
            return urls
        except Exception as e:
            print(f"Error al obtener imágenes de {folder_name}: {e}")
            return []

    def get_staff(self):
        """Obtiene el personal del establecimiento. Retorna la lista local de models.py si falla Supabase."""
        try:
            # Intentamos obtener datos reales de Supabase
            response = self.client.table("staff").select("*").order("order_index").execute()
            
            if response.data and len(response.data) > 0:
                return response.data
            
            raise Exception("Table empty or not found")
            
        except Exception as e:
            # Importación tardía para evitar círculos de dependencia si los hubiera
            from ..models import get_staff_as_dicts
            print(f"Usando lista de personal local de models.py (Motivo: {e})")
            return get_staff_as_dicts()
