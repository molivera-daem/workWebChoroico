import os
import sys

# Agregar el directorio WebChoroico al path para que las importaciones funcionen correctamente
path = os.path.dirname(os.path.abspath(__file__))
sys.path.append(os.path.join(path, 'WebChoroico'))

try:
    # Importar la aplicación Flask
    from WebChoroico.app import app
except Exception as e:
    from flask import Flask
    app = Flask(__name__)
    @app.route('/')
    def error():
        return f"Error al importar la app: {str(e)}<br>Path: {sys.path}<br>Files: {os.listdir(path)}", 500

# Vercel usará el objeto 'app'
if __name__ == "__main__":
    app.run()
