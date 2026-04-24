# Ticket: Actualización y Estandarización Base del Proyecto

**Ticket:** TSK-001
**Estado:** Completado
**Fecha de Inicio:** 2025-12-29
**Fecha de Finalización:** 2025-12-29

---

## 🗣️ Ayudante en Jefe de Producto

### 1. Descripción de la Idea

El proyecto `WebChoroico` dispone de una base de código inicial en Python/Flask. Recientemente, se ha establecido un nuevo flujo de trabajo profesional (`.workflow`) y se han definido las infraestructuras de despliegue (Anaconda Web/cPanel + NIC Chile).
Es necesario actualizar y estandarizar la base del proyecto actual para que cumpla con los nuevos roles, lineamientos de codificación (`snake_case`) y requisitos de infraestructura antes de comenzar con el desarrollo de nuevas tickets.

**Problema Detectado:**
La estructura actual funciona localmente pero no está preparada para el despliegue en un entorno compartido (cPanel) ni sigue estrictamente los nuevos estándares de documentación y organización definidos por el equipo.

### 2. Historia de Usuario (User Story)

**Como** equipo de desarrollo,
**Quiero** tener una base de código limpia, organizada y pre-configurada para Anaconda Web,
**Para** poder desarrollar nuevas funcionalidades de manera escalable y desplegar sin fricción.

### 3. Requisitos Mínimos Viables (MVP)

1.  **Estructura de Directorios:**
    *   Reorganizar archivos según la definición del Arquitecto (ej. separar `blueprints` si aplica, carpetas `static`/`templates` confirmadas).
    *   **Propuesta de Estructura Escalable:**
        ```
        /
        ├── app/
        │   ├── __init__.py      # App factory (create_app)
        │   ├── routes.py        # Definición de Blueprints de cada modulo
        │   ├── models.py        # Modelos de BBDD
        │   ├── static/          # Assets públicos
        │   └── templates/       # Vistas Jinja2
        ├── config.py            # Configuraciones (Dev/Prod)
        ├── run.py               # Punto de entrada WSGI
        ├── requirements.txt     # Dependencias
        └── .env                 # Variables de entorno
        ```
    *   Asegurar que `run.py` sea compatible con la entrada WSGI de cPanel.

2.  **Limpieza y Estandarización:**
    *   Revisar que todo el código existente cumpla con `snake_case` (variables, funciones).
    *   Eliminar archivos basura o temporales que no sean del proyecto.
    *   Crear/Actualizar `.gitignore`.

3.  **Configuración de Entorno:**
    *   Archivo `requirements.txt` actualizado con versiones fijas.
    *   Archivo de configuración para variables de entorno (ej. `.env.example`).
    *   Script o configuración necesaria para que funcione en Anaconda Web (ej. `passenger_wsgi.py` si fuera necesario, a confirmar por DevOps).

### 4. Impacto Esperado

*   **Despliegue:** 100% listo para subir a Anaconda Web.
*   **Velocidad:** Reducción de errores en futuros desarrollos al tener una base sólida.
*   **Orden:** Cumplimiento total de los lineamientos del `.workflow`.

### 5. Preguntas para el Equipo

*   **@Arquitecto_Software:**
    1.  ¿Mantendremos una estructura plana con `app.py` o pasaremos a una estructura de paquete (ej. `app/__init__.py`) para este MVP?
    2.  ¿Necesitamos configurar `gunicorn` o usaremos el servidor WSGI provisto por cPanel?

*   **@Ingeniero_DevOps:**
    1.  ¿Qué archivos específicos requiere Anaconda Web para detectar la app Python?
    2.  ¿Cómo manejaremos las variables de entorno en cPanel?

*   **@Ingeniero_QA:**
    1.  ¿Qué pruebas básicas ("Smoke Tests") debemos correr para asegurar que la "base" está saludable?

---

## 🏛️ Arquitecto de Software

**Análisis y Decisiones Técnicas:**

1.  **Estructura del Proyecto:**
    *   **Decisión:** Aprobado el paso a **Application Factory Pattern**.
    *   **Justificación:** Estructurar el proyecto como un paquete expondra una funcion `create_app()` que facilita las pruebas (QA) y permite gestionar múltiples configuraciones (Dev/Prod) limpiamente. Esto es crucial para separar la config local de la de Anaconda Web.
    *   **WSGI:** Usaremos un archivo `application.py` o `passenger_wsgi.py` (estándar en cPanel) que importará nuestra factory. No configuraremos Gunicorn manualmente en prod ya que cPanel usa Phusion Passenger o similar para servir la app Python.

2.  **Stack Tecnológico Base:**
    *   **Flask:** Framework principal.
    *   **Python-dotenv:** Para cargar variables de entorno locales.
    *   **Flask-WTF:** Para manejo seguro de formularios (si aplica a futuro, preparar base).

3.  **Respuesta a Preguntas:**
    *   **Estructura:** Sí, pasamos a paquete `app/`.
    *   **Servidor:** Usaremos el servidor WSGI provisto por la configuración "Setup Python App" de cPanel.

---

## 🛠️ Ingeniero DevOps

**Configuración de Infraestructura (Anaconda Web):**

1.  **Integración con cPanel:**
    *   **Punto de Entrada:** Anaconda Web genera por defecto un archivo `passenger_wsgi.py` al crear la "Python App". Debemos modificar ese archivo para que importe nuestro `app` object.
    *   **Estrategia:** El archivo `passenger_wsgi.py` debe hacer: `from app import create_app; application = create_app()`.

2.  **Variables de Entorno:**
    *   **Local:** Usaremos archivo `.env` (ignorado en git).
    *   **Producción (cPanel):** Las variables se configuran en la interfaz "Setup Python App" -> "Environment variables". NO subiremos el archivo `.env` a producción.

3.  **Requisitos:**
    *   Crear archivo `requirements.txt` limpio. cPanel permite instalar dependencias desde este archivo vía interfaz UI.

---

## 🧪 Ingeniero de Calidad (QA)

**Smoke Tests (Pruebas de Humo):**

Para validar que la "Actualización Base" fue exitosa, ejecutaremos:

1.  **Prueba de Arranque:** La aplicación debe iniciar sin errores de importación (`flask run`).
2.  **Ruta Principal:** `GET /` debe retornar código 200 y renderizar el template `index.html`.
3.  **Recursos Estáticos:** Verificar que cargue al menos un archivo CSS/JS (ej. `GET /static/css/style.css` -> 200).
4.  **Manejo de Errores:** Acceder a una ruta inexistente `/ruta-falsa` debe retornar 404 (y preferiblemente un template custom, si existe).
5.  **Entorno:** Verificar que `app.config` cargue correctamente una variable de prueba desde el `.env`.

---

## 🛠️ Refinador Técnico

**Plan de Implementación Detallado:**

1.  **Reestructuración de Carpetas:**
    *   Crear directorio `app/`.
    *   Mover `templates/` y `static/` dentro de `app/`.
    *   Crear `app/__init__.py` con función `create_app()`.
    *   Crear `app/routes.py` y mover lógica de rutas de `app.py`.

2.  **Configuración:**
    *   Crear `config.py` con clase base `Config`.
    *   Crear `.env.example` para documentar variables requeridas.
    *   Limpiar `requirements.txt` (usar `pip freeze` en un venv limpio idealmente).

3.  **Limpieza de Código:**
    *   Renombrar funciones a `snake_case` si hay camellos sueltos.
    *   Eliminar `Procfile` si no se usará Heroku (Anaconda usa cPanel).

### Estructura de Archivos Afectados (Anti-Colisión)

*   **[DELETE]** `app.py` (Lógica movida a `app/routes.py` y `run.py`)
*   **[NEW]** `app/__init__.py`
*   **[NEW]** `app/routes.py`
*   **[NEW]** `config.py`
*   **[NEW]** `run.py` (Para ejecución local)
*   **[MODIFY]** `requirements.txt`
*   **[MOVE]** `templates/` -> `app/templates/`
*   **[MOVE]** `static/` -> `app/static/`

---

## 👨‍💻 Desarrollador Senior

*(Implementación Finalizada)*

**Resumen de Cambios:**
1.  **Refactorización:** Se movió todo el código a la estructura `app/`.
2.  **Factory Pattern:** Implementado en `app/__init__.py`.
3.  **Configuración:** Variables de entorno y clases de configuración listas.
4.  **Entry Points:** `run.py` (local) y `passenger_wsgi.py` (cPanel) creados y verificados.
5.  **Smoke Tests:** Importación de factory exitosa. Dependencias congeladas en `requirements.txt`.

### Actualización (Refinamiento)
Se realizó una segunda pasadad para cumplir estrictamente con `CODING_GUIDELINES.md`:
*   **Renombrado a Inglés:** Rutas (`/about-us`), funciones (`about_us`) y archivos (`about_us.html`).
*   **Documentación:** Se agregaron docstrings y headers (`@file`, `@author`) a todos los archivos.
