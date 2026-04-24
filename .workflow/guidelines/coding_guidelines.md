# Directrices de Codificación del Proyecto WebChoroico

## 1. Introducción
Este documento define las buenas prácticas y estándares de codificación para el desarrollo en Python/Flask para la Escuela Choroico. El objetivo es asegurar que el código sea limpio, consistente, mantenible y de alta calidad. Seguir estas guías es obligatorio.

## 2. Principios Generales
- **Idioma del Código:** Nombres de variables, funciones, clases, archivos y rutas deben estar en **Inglés**.
- **Idioma de Comentarios:** Los comentarios explicativos y la documentación (docstrings) deben estar en **Español**.
- **KISS (Keep It Simple, Stupid):** Prefiere soluciones simples.
- **DRY (Don't Repeat Yourself):** Encapsula lógica reutilizable.
- **Consistencia:** Sigue la convención de nombres estándar de Python (PEP 8).

## 3. Estructura de Archivos y Nomenclatura
- **Directorios/Paquetes:** `snake_case`. Ejemplo: `app/routes/`.
- **Archivos Python (`.py`):** `snake_case`. Ejemplo: `auth_controller.py`.
- **Clases:** `PascalCase`. Ejemplo: `RegistrationForm`.
- **Funciones y Variables:** `snake_case`. Ejemplo: `calculate_average`.
- **Constantes:** `UPPER_SNAKE_CASE`. Ejemplo: `MAX_LOGIN_ATTEMPTS`.
- **Templates HTML:** `snake_case`. Ejemplo: `about_us.html`.
- **Clases CSS:** `kebab-case`. Ejemplo: `.main-menu`.

## 4. Guía de Backend (Python / Flask)

### Estructura de API
- **Modelos (`models.py`):** Definición de tablas de BBDD.
- **Rutas (`routes.py` o Blueprints):** Definición de endpoints.
- **Servicios/Lógica:** Si la lógica crece, separar en módulos (ej. `services/email_service.py`).

### Documentación (Docstrings)
Todos los módulos y funciones deben estar documentados usando docstrings (estándar de Python) en **Español**.

**Documentación a Nivel de Archivo:**
```python
"""
@file app/routes.py
@description Definición de las rutas principales del sitio web.
@author Miguel Olivera Labrin
"""
```

**Documentación a Nivel de Función:**
```python
def calculate_average(grades):
    """
    Calcula el promedio de una lista de notas.

    :param list grades: Lista de números flotantes con las notas.
    :return: El promedio calculado.
    :rtype: float
    :raises ValueError: Si la lista está vacía.
    """
    if not grades:
        raise ValueError("La lista de notas no puede estar vacía")
    return sum(grades) / len(grades)
```

## 5. Guía de Frontend (Jinja2 / HTML / CSS)

### Estructura
- **Templates:** Usar herencia (`{% extends "base.html" %}`) para evitar repetición de código (header/footer).
- **Bloques:** Usar bloques definidos (`{% block content %}`) para inyectar contenido.

**Encabezado de Archivo HTML:**
```html
<!--
    @file app/templates/about_us.html
    @description Página estática institucional "Quiénes Somos".
    @author Miguel Olivera Labrin
-->
```

## 6. Base de Datos
- Usar SQLAlchemy (si aplica) o consultas SQL limpias.
- Comentarios en SQL para migraciones manuales en Español.

## 7. Trazabilidad de Features (Tickets)
Para mantener trazabilidad entre tickets (`TSK-XXX`) y código, marcar cambios significativos:

```python
# TSK-001: Implementación de la factoría de aplicación para escalabilidad
def create_app():
    ...
```

## 8. Git y Commits
- **Formato:** [Conventional Commits](https://www.conventionalcommits.org/). El mensaje del commit puede ser en inglés o español, pero mantenga consistencia (preferiblemente Español dado los comentarios).
    - `feat:` Nueva funcionalidad.
    - `fix:` Corrección de error.
    - `refactor:` Cambios de código que no alteran funcionalidad.
    - `docs:` Cambios en documentación.
