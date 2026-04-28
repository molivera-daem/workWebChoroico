import os
import sys

# Agregar el directorio WebChoroico al path para que las importaciones funcionen
path = os.path.dirname(os.path.abspath(__file__))
web_choroico_path = os.path.join(path, 'WebChoroico')
if web_choroico_path not in sys.path:
    sys.path.insert(0, web_choroico_path)

# Importar la instancia de Flask
try:
    from app import app
except ImportError:
    from WebChoroico.app import app

# Esto es lo que Vercel necesita encontrar
application = app

if __name__ == "__main__":
    app.run()
