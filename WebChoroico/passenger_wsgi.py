"""
@file passenger_wsgi.py
@description Punto de entrada WSGI para cPanel/Phusion Passenger.
@description Punto de entrada WSGI para despliegue en cPanel/Anaconda Web.
@author Miguel Olivera Labrin
"""

from core import create_app
from config import ProductionConfig

# 'application' es el nombre que Passenger busca por defecto
application = create_app(ProductionConfig)
