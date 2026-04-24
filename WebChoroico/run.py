"""
@file run.py
@description Punto de entrada para ejecución local (Desarrollo).
@author Miguel Olivera Labrin
"""

from core import create_app
from config import DevelopmentConfig

app = create_app(DevelopmentConfig)

if __name__ == '__main__':
    # Usamos puerto 5002 para evitar conflictos con AirPlay en macOS (que usa el 5001)
    # Escuchamos en 0.0.0.0 para asegurar visibilidad
    app.run(host='0.0.0.0', port=5002)
