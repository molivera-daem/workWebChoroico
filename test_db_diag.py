import os
from supabase import create_client
from dotenv import load_dotenv

load_dotenv('WebChoroico/.env')

def test_db():
    url = os.environ.get("SUPABASE_URL")
    key = os.environ.get("SUPABASE_KEY")
    
    if not url or not key:
        print("❌ Faltan credenciales en .env")
        return

    try:
        supabase = create_client(url, key)
        print(f"✅ Conectado a: {url}")
        
        # Probar tabla staff
        print("\n--- Probando tabla 'staff' ---")
        try:
            res_staff = supabase.table("staff").select("*").execute()
            print(f"Número de registros en 'staff': {len(res_staff.data)}")
            if len(res_staff.data) > 0:
                print("Primer registro:", res_staff.data[0])
            else:
                print("⚠️ La tabla 'staff' está VACÍA.")
        except Exception as e:
            print(f"❌ Error al consultar 'staff': {e}")

        # Probar tabla news para ver si funciona la conexión general
        print("\n--- Probando tabla 'news' ---")
        try:
            res_news = supabase.table("news").select("id, title").limit(1).execute()
            print(f"Número de noticias encontradas: {len(res_news.data)}")
        except Exception as e:
            print(f"❌ Error al consultar 'news': {e}")

    except Exception as e:
        print(f"❌ Error crítico de conexión: {e}")

if __name__ == "__main__":
    test_db()
