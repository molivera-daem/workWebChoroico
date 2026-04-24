import sys
import os

# Añadir el directorio raíz al path para poder importar los módulos
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from WebChoroico.core.services.supabase_service import SupabaseService

def test_connection():
    print("--- 🧪 Iniciando Prueba de Conexión con Supabase ---")
    try:
        service = SupabaseService()
        
        # Intentar obtener noticias (aunque la tabla esté vacía, la consulta debe ser exitosa)
        print("Intentando consultar tabla 'news'...")
        news = service.get_all_news()
        
        print("✅ Conexión exitosa!")
        print(f"Resultado: Se obtuvieron {len(news)} noticias.")
        
        if len(news) == 0:
            print("💡 Nota: La conexión funciona, pero la tabla 'news' parece estar vacía o no existe aún.")
            print("Asegúrate de haber ejecutado el script SQL que te proporcioné anteriormente en el panel de Supabase.")
            
    except Exception as e:
        print(f"❌ Error de conexión: {e}")

if __name__ == "__main__":
    test_connection()
