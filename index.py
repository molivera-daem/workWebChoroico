import os
import sys

# Agregar el directorio WebChoroico al path para que las importaciones funcionen correctamente
path = os.path.dirname(os.path.abspath(__file__))
web_choroico_path = os.path.join(path, 'WebChoroico')
if web_choroico_path not in sys.path:
    sys.path.append(web_choroico_path)

# Importar la aplicación Flask desde app.py dentro de WebChoroico
# En WebChoroico/app.py tenemos: app = create_app(ProductionConfig)
try:
    from app import app
except ImportError:
    # Intento alternativo si el anterior falla en ciertos entornos
    from WebChoroico.app import app

# Vercel usará el objeto 'app'
if __name__ == "__main__":
    app.run()
