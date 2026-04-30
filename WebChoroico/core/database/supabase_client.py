import os
from supabase import create_client, Client
from dotenv import load_dotenv

load_dotenv()

def get_supabase_client() -> Client:
    """
    Inicializa y retorna el cliente de Supabase usando variables de entorno.
    """
    url = os.environ.get("SUPABASE_URL", "").strip()
    key = os.environ.get("SUPABASE_KEY", "").strip()
    
    # Limpieza de URL para evitar errores comunes de configuración
    if url.endswith('/'):
        url = url[:-1]
    if url.endswith('/rest/v1'):
        url = url[:-8]
    if url.endswith('/'):
        url = url[:-1]
        
    if not url or not key:
        raise ValueError("SUPABASE_URL y SUPABASE_KEY deben estar configuradas en el archivo .env")
        
    return create_client(url, key)
