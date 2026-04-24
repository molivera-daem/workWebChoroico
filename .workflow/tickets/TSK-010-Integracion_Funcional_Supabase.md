# Ticket: Integración Funcional con Supabase (Contenidos y Gestión)

**Ticket:** TSK-010
**Estado:** En Proceso (Análisis de Roles)
**Fecha de Inicio:** 2026-04-23

---

## 🗣️ Ayudante en Jefe de Producto

### 1. Descripción de la Idea
Tras la integración del núcleo de Supabase (TSK-009), el siguiente paso crítico es permitir que los administradores de la escuela puedan actualizar noticias y la galería de imágenes sin necesidad de modificar el código fuente. La meta es que la web deje de ser un sitio estático y pase a ser una plataforma gestionable.

**Problema Detectado:**
Actualmente, para añadir una noticia o una foto a la galería, se requiere intervención técnica (editar archivos HTML/CSS y subir imágenes vía FTP/Git), lo que retrasa la comunicación de la escuela.

### 2. Historia de Usuario (User Story)
**Como** administrador del sitio,
**Quiero** gestionar las noticias y la galería desde un panel o base de datos centralizada,
**Para** mantener la información de la escuela actualizada de forma autónoma y rápida.

### 3. Requisitos Mínimos Viables (MVP)
1.  **Noticias Dinámicas:** Almacenar títulos, descripciones, fechas e imágenes en Supabase Database.
2.  **Galería Dinámica:** Gestionar las imágenes de la escuela mediante Supabase Storage y referenciarlas en la base de datos.
3.  **Visualización en Web:** Actualizar las rutas `/news` y `/gallery` para que consuman datos directamente de Supabase en lugar de estar en el código.

---

## 🏛️ Arquitecto de Software

**Análisis y Decisiones Técnicas:**

1.  **Esquema de Base de Datos (SQL):**
    *   Tabla `news`: `id`, `created_at`, `title`, `content`, `image_url`, `author_id`.
    *   Tabla `gallery`: `id`, `created_at`, `title`, `image_url`, `category`.
    *   Utilizaremos RLS (Row Level Security) para asegurar que solo el administrador pueda insertar/modificar datos.

2.  **Capa de Servicio (Pattern):**
    *   No inyectaremos el cliente de Supabase directamente en las rutas.
    *   Crearemos `core/services/supabase_service.py` para abstraer las consultas y el manejo de errores.

3.  **Gestión de Imágenes:**
    *   Las imágenes se subirán al bucket `school-assets` en Supabase Storage.
    *   En la base de datos solo guardaremos la URL pública generada.

---

## 🛠️ Ingeniero DevOps

**Configuración de Infraestructura:**

1.  **Supabase Setup:**
    *   Creación de tablas mediante scripts SQL.
    *   Configuración del Bucket de Storage con políticas de lectura pública.
2.  **Seguridad:**
    *   Verificar que `SUPABASE_KEY` (service_role) nunca se exponga al cliente.
    *   Usar `SUPABASE_ANON_KEY` para las consultas de lectura desde la app si fuera necesario, aunque preferimos manejarlo vía Server-Side (Flask).

---

## 🧪 Ingeniero de Calidad (QA)

**Plan de Pruebas:**

1.  **Integridad de Datos:** Validar que al insertar una noticia en Supabase, esta aparezca instantáneamente en la web.
2.  **Manejo de Imágenes:** Verificar que las imágenes con nombres con espacios o caracteres especiales se procesen correctamente a través de la URL de Supabase.
3.  **Resiliencia:** Probar el comportamiento de la web si la conexión con Supabase falla (debe mostrar un mensaje amigable o usar caché si se implementa).

---

## 🛠️ Refinador Técnico

**Plan de Implementación Detallado:**

1.  **Base de Datos:**
    *   Ejecutar scripts DDL en la consola de Supabase.
2.  **Backend (Flask):**
    *   Implementar métodos `get_all_news()` y `get_gallery_items()` en `supabase_service.py`.
    *   Actualizar las funciones de vista en `core/routes.py` para inyectar estos datos en los templates.
3.  **Frontend (Jinja2):**
    *   Sustituir el contenido "placeholder" en `news.html` y `gallery.html` con bucles `{% for ... %}`.

### Estructura de Archivos Afectados

*   **[NEW]** `WebChoroico/core/services/supabase_service.py`
*   **[MODIFY]** `WebChoroico/core/routes.py`
*   **[MODIFY]** `WebChoroico/core/templates/news.html`
*   **[MODIFY]** `WebChoroico/core/templates/gallery.html`
*   **[MODIFY]** `WebChoroico/.env` (Verificar claves)
