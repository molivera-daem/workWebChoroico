from core import create_app
from config import ProductionConfig

# 'app' es el punto de entrada que busca Vercel por defecto
app = create_app(ProductionConfig)
