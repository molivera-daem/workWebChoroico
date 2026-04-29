# Ticket: Mejoras Visuales y Funcionales Integrales

**Ticket:** TSK-011
**Estado:** En Proceso (Análisis de Roles)
**Fecha de Inicio:** 2026-04-28

---

## 🗣️ Ayudante en Jefe de Producto

### 1. Descripción de la Idea
Con la infraestructura técnica ya desplegada y conectada a Supabase, el objetivo ahora es transformar la experiencia del usuario (UX) y el impacto visual (UI). Queremos que el sitio no solo sea funcional, sino que proyecte la identidad institucional de la Escuela Aurora de Chile de forma profesional, moderna y accesible.

**Problema Detectado:**
La web actual es funcional pero se siente "plana" y básica. Falta interactividad, un diseño más cohesivo y funcionalidades que mejoren la navegación del usuario.

### 2. Historia de Usuario (User Story)
**Como** visitante de la web (padre, alumno o docente),
**Quiero** navegar por un sitio visualmente atractivo, rápido y fácil de usar en cualquier dispositivo,
**Para** encontrar información institucional de forma eficiente y sentir confianza en la modernización del establecimiento.

### 3. Requisitos Mínimos Viables (MVP)
1.  **Rediseño de la Home:** Incorporación de un Hero dinámico y secciones destacadas.
2.  **Interactividad en Galería:** Implementación de un Lightbox avanzado con filtrado por categorías.
3.  **Sistema de Noticias:** Mejorar la visualización con "cards" modernas y carga optimizada.
4.  **Optimización Móvil (Responsive):** Asegurar que todos los componentes sean 100% adaptables.

---

## 🎨 Diseñador UX/UI

**Propuesta Estética:**

1.  **Paleta de Colores:** Reforzar el uso del azul institucional y blanco, incorporando gris claro para fondos y acentos dorados/naranjas suaves para llamadas a la acción (CTAs).
2.  **Tipografía:** Usar una combinación de Sans-serif (ej. Inter o Roboto) para legibilidad moderna.
3.  **Componentes:**
    *   **Cards:** Bordes redondeados (8px-12px), sombras suaves (soft shadows) y efectos de hover sutiles.
    *   **Botones:** Estados claros de focus y hover con transiciones suaves (0.3s).
4.  **Galería:** Implementar un sistema de filtros (Categorías como: "Deportes", "Actos", "Infraestructura") para organizar el contenido visual.

---

## 🏛️ Arquitecto de Software

**Análisis Técnico:**

1.  **Componentización CSS:** Migrar estilos generales a variables CSS (Custom Properties) en `style.css` para facilitar cambios globales.
2.  **Optimización de Carga:** Implementar "Lazy Loading" nativo para imágenes en la galería y noticias.
3.  **Lógica de Filtrado:** El filtrado de la galería se manejará en el cliente (JavaScript) para mayor rapidez, pero la estructura de datos vendrá preparada desde el `SupabaseService`.

---

## 🛠️ Desarrollador Senior

**Plan de Acción Técnico:**

1.  **Backend:**
    *   Actualizar `SupabaseService` para incluir conteos o categorías únicas si es necesario.
2.  **Frontend:**
    *   Refactorizar `base.html` para incluir un Footer institucional más completo y un menú de navegación con indicadores de página activa.
    *   Mejorar el Lightbox de la galería (ya iniciado en el fix anterior) para que sea más robusto.
3.  **Assets:** Optimizar los assets estáticos actuales (logo, imágenes de historia) para reducir el tiempo de carga.

---

## 🧪 Ingeniero de Calidad (QA)

**Criterios de Aceptación:**

1.  **Cross-browser:** Probar en Chrome, Safari y Firefox.
2.  **Responsive:** Validar visualización correcta en iPhone, tablets y desktop.
3.  **Accesibilidad (A11y):** Verificar contraste de colores y uso de etiquetas `alt` en imágenes dinámicas de Supabase.
4.  **Performance:** El sitio debe cargar la home en menos de 2 segundos en conexiones estándar.

---

## 🛠️ Refinador Técnico

**Plan de Implementación:**

1.  **Fase 1: Estilos Base y Variables.** Definición de colores y tipografía global.
2.  **Fase 2: Rediseño de la Home.** Nueva sección Hero y layout de secciones destacadas.
3.  **Fase 3: Refactorización de Noticias y Galería.** Aplicación de los nuevos estilos de cards y filtros.
4.  **Fase 4: Pulido Móvil.** Ajustes finales de media queries.

### Archivos a Modificar
*   `WebChoroico/core/static/css/style.css`
*   `WebChoroico/core/static/css/news.css`
*   `WebChoroico/core/static/css/gallery.css`
*   `WebChoroico/core/templates/base.html`
*   `WebChoroico/core/templates/index.html`
*   `WebChoroico/core/templates/news.html`
*   `WebChoroico/core/templates/gallery.html`
