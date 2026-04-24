# Ticket: Rediseño Profesional (Estilo Municipal/Institucional)

**Ticket:** TSK-004
**Estado:** Completado
**Fecha de Inicio:** 2025-12-30
**Fecha de Finalización:** 2025-12-30
**Depende de:** TSK-003

---

## 🧑‍💼 Ayudante en Jefe de Producto

### 1. Descripción de la Idea
El usuario ha solicitado una maquetación profesional inspirada en el sitio de la [Municipalidad de Cunco](https://www.municunco.cl/). Esto implica pasar de un diseño minimalista/glassmorphism a uno más robusto, institucional y con secciones de contenido claras.

**Objetivo:**
Transformar la interfaz actual en un portal educativo profesional que transmita confianza, orden y modernidad.

### 2. Historia de Usuario (User Story)
**Como** Director del Establecimiento,
**Quiero** tener un portal web estructurado con secciones de noticias, trámites y servicios,
**Para** que la comunidad educativa acceda a la información de forma clara y profesional.

### 3. Requisitos Mínimos Viables (MVP)
1.  **Header Institucional**: 
    *   Top-bar con contacto/redes sociales.
    *   Nav-bar con logo (izquierda) y menú (derecha), con fondo sólido o degradado suave.
2.  **Hero Section**:
    *   Banner de gran impacto con imagen real de la escuela y texto superpuesto.
3.  **Secciones de Contenido**:
    *   Grid de Noticias destacadas.
    *   Sección de "Servicios" o "Trámites" (Iconos + Títulos).
4.  **Footer Profesional**:
    *   Columnas de enlaces, redes sociales y mapa/contacto.
5.  **Responsividad**:
    *   Ajuste perfecto en dispositivos móviles.

### 4. Impacto Esperado
*   **Percepción**: Mayor seriedad y presencia institucional.
*   **Usabilidad**: Mejor organización de la información para padres y apoderados.

---

## 🏗️ Respuestas de Roles

### 🏗️ Arquitecto de Software
*   **Componentización**: Dividir `base.html` en macros o sub-plantillas (`header.html`, `footer.html`) si la complejidad aumenta mucho.
*   **Nomenclatura**: Mantener BEM para las clases de CSS para evitar conflictos en un diseño más grande.

### 🎨 Diseñador UX/UI
*   **Paleta de Colores**: Usar azules institucionales, blancos limpios y grises suaves.
*   **Tipografía**: Mantener 'Poppins' o 'Roboto' para lectura clara.
*   **Iconografía**: Usar FontAwesome consistently.

### 🔧 Ingeniero DevOps
*   **Assets**: Vigilar el peso de las imágenes del Hero Banner para no degradar el tiempo de carga en móviles.

### 🔍 Ingeniero QA
*   **Navegación**: Asegurar que los menús desplegables (si los hay) funcionen bien en táctil.
*   **Contraste**: Verificar legibilidad del texto sobre las imágenes del banner.

### 🛠️ Refinador Técnico
*   **Fases**:
    1.  Rediseño de `base.html` (Header/Footer).
    2.  Implementación del Hero en `index.html`.
    3.  Creación de secciones de noticias y servicios en Home.
    4.  Ajuste de estilos globales en `style.css`.
    5.  **Adición de Sección de Redes Sociales**: Crear un bloque interactivo para Facebook e Instagram antes del footer.
