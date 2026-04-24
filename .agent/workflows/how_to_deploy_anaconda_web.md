---
description: How to deploy the Flask application to Anaconda Web (cPanel)
---

# Despliegue en Anaconda Web (cPanel)

Este flujo de trabajo describe los pasos manuales para desplegar la aplicación `WebChoroico` en el hosting compartido de Anaconda Web.

## Prerrequisitos
- Acceso a cPanel
- Código del proyecto comprimido (`.zip`)

## Pasos

1.  **Preparar el Código**
    - En tu máquina local, comprime el contenido de la carpeta `WebChoroico` en un archivo `.zip`.
    - **IMPORTANTE:** EXCLUYE la carpeta `venv/`, `__pycache__/` y el archivo `.env`. (El archivo `.env` lo crearás manualmente en el servidor o usarás la UI de cPanel).
    - Asegúrate de incluir `passenger_wsgi.py` y `requirements.txt`.

2.  **Subir Archivos via cPanel**
    - Ingresa a cPanel -> **Administrador de Archivos**.
    - Navega a la carpeta raíz de tu aplicación (usualmente `/home/usuario/repositories/webchoroico` o similar, depende de cómo creaste la app).
    - Sube el archivo `.zip`.
    - Descomprime el archivo (sobrescribiendo si es necesario).

3.  **Configurar "Setup Python App"**
    - En cPanel, busca y abre **Setup Python App**.
    - Crea una nueva aplicación (o edita la existente):
        - **Python version:** Selecciona la recomendada (ej. 3.9 o superior).
        - **App Directory:** La carpeta donde subiste los archivos.
        - **App Domain:** El dominio de tu escuela (ej. `escuelachoroico.cl`).
        - **Application startup file:** `passenger_wsgi.py` (Esto es clave).
        - **Application entry point:** `application` (Esto debe coincidir con la variable `application` dentro de `passenger_wsgi.py`).

4.  **Instalar Dependencias**
    - En la interfaz de "Setup Python App", verás una sección "Configuration files".
    - Escribe `requirements.txt` y presiona "Add".
    - Luego presiona el botón **Run Pip Install**. Esto instalará `Flask`, `python-dotenv`, etc. en el servidor.

5.  **Configurar Variables de Entorno**
    - En la misma interfaz, busca la sección "Environment variables".
    - Agrega las variables que tienes en tu `.env` local:
        - `FLASK_APP`: `passenger_wsgi.py`
        - `FLASK_ENV`: `production`
        - `SECRET_KEY`: (Genera una clave segura y única para producción)

6.  **Reiniciar la Aplicación**
    - Presiona el botón **Restart** en la parte superior de la configuración de la app.

7.  **Verificar**
    - Abre tu dominio en el navegador. Deberías ver la aplicación funcionando.
