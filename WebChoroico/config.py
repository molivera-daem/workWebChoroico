"""
@file config.py
@description Definición de clases de configuración para distintos entornos.
@author Miguel Olivera Labrin
"""

import os
from dotenv import load_dotenv

load_dotenv()

class Config:
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'you-will-never-guess'
    DEBUG = False
    Testing = False

class DevelopmentConfig(Config):
    DEBUG = True

class ProductionConfig(Config):
    DEBUG = False
    # En cPanel/Anaconda, las variables de entorno se manejan vía UI o.env
    # Asegúrate de setear SECRET_KEY en producción
