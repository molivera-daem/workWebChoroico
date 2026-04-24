# Ticket: Integración de Logo del Establecimiento

**Ticket:** TSK-003
**Estado:** Completado
**Fecha de Inicio:** 2025-12-29
**Fecha de Finalización:** 2025-12-29
**Depende de:** TSK-001

---

## 🧑‍💼 Ayudante en Jefe de Producto

### 1. Descripción de la Idea

Una vez estabilizada la base técnica (`TSK-001`) y el despliegue (`TSK-002`), es fundamental comenzar con la identidad visual del sitio. El objetivo de este ticket es integrar el logo oficial del establecimiento "Aurora de Chile" en las ubicaciones clave de la web para reforzar la marca y profesionalismo.

**Problema Detectado:**
La web actual no cuenta con el logo oficial visible, lo que dificulta la identificación institucional y personalización del diseño.

### 2. Historia de Usuario (User Story)

**Como** Representante del Establecimiento,
**Quiero** que el logo de la escuela aparezca de forma visible en el encabezado y pie de página,
**Para** que los visitantes reconozcan de inmediato la marca institucional de la Escuela Aurora de Chile.

### 3. Requisitos Mínimos Viables (MVP)

1.  **Recopilación de Activos:**
    *   Obtener el logo en formato de alta calidad (SVG o PNG transparente preferiblemente).
    *   Definir variantes (claro/oscuro si aplica).

2.  **Integración en Header:**
    *   Colocar el logo en la parte superior izquierda (o centro según diseño).
    *   Asegurar que sea responsivo (se adapte a móviles).
    *   Linkear el logo a la página de "Home".

3.  **Integración en Footer:**
    *   Agregar una versión del logo (puede ser simplificada) en el pie de página junto a los datos de contacto.

4.  **Estilo y Alineación:**
    *   Asegurar que el tamaño sea armonioso con la tipografía actual.

### 4. Impacto Esperado

*   **Identidad:** Fortalecimiento de la imagen institucional.
*   **Navegación:** Mejora de la usabilidad al tener un punto de retorno (logo-home) consistente.
*   **Estética:** Una interfaz que se siente completa y oficial.

### 5. Preguntas para el Equipo

*   **@Diseñador_UX_UI:** ¿Tenemos el logo en formato vectorial (SVG)? ¿Cuál es la proporción ideal para el header?
*   **@Desarrollador_Senior:** ¿Ubicamos el logo en la carpeta `static/img/` o usamos una CDN?

---

## 🏗️ Arquitecto de Software

*   **Estructura de Archivos**: Recomiendo guardar el logo en `core/static/img/branch/logo.svg` (usar SVG para escalabilidad infinita sin pérdida de peso).
*   **Implementación**: Debería cargarse vía `url_for('static', filename='img/branch/logo.svg')` en el `base.html` (o `layout.html`) para que esté presente en todas las páginas.

## 🎨 Diseñador UX/UI

*   **Dimensiones**: Para el header, el logo no debe exceder los 50px de altura para mantener la barra de navegación compacta.
*   **Contraste**: Si el header es oscuro, necesitaremos la versión negativa (blanca) del logo.
*   **Spacing**: Mantener un padding de al menos 10px alrededor del logo.

## 🔧 Ingeniero DevOps

*   **Optimización**: El archivo debe pasar por una herramienta de minificación (`svgo` para SVG o `tinypng` para PNG) antes del despliegue para no afectar el LCP (Largest Contentful Paint).
*   **Vercel**: El despliegue automático en Vercel manejará correctamente los archivos estáticos.

## 🔍 Ingeniero QA

*   **Pruebas de Regresión**: Verificar que el logo cargue en todas las rutas (`/`, `/about-us`, `/news`).
*   **Responsive**: Comprobar que en móviles el logo no empuje los elementos del menú (hamburguesa).
*   **Accessibility**: El tag `<img>` DEBE tener un `alt="Logo Escuela Aurora de Chile"`.

## 🛠️ Refinador Técnico

*   **Plan de Acción**:
    1.  Subir el archivo de imagen a la carpeta de assets.
    2.  Modificar la plantilla base (Jinaja2) para incluir el componente de logo.
    3.  Ajustar estilos CSS globales (`main.css` o similar) para el posicionamiento.
