# [TASK] TSK-007: Rediseño Profesional de la Sección de Galería

Este ticket describe el trabajo necesario para implementar una galería fotográfica profesional y dinámica para el establecimiento.

## Contexto
La sección de galería actualmente reutiliza la plantilla genérica. Se requiere un diseño dedicado que permita visualizar las actividades del establecimiento de forma elegante, utilizando un Grid moderno y un visualizador (Lightbox/Modal) para las fotos.

## Objetivos
- [ ] Crear una plantilla `gallery.html` dedicada.
- [ ] Implementar un Grid de imágenes con efectos de hover.
- [ ] Añadir un visualizador tipo "Lightbox" para ampliar las imágenes (Carousel Modal).
- [ ] Mantener la estética premium y profesional (Glassmorphism, transiciones suaves).
- [ ] Preparar la carga de imágenes de prueba (Mock images).

## Cambios Propuestos

### Componente: Frontend

#### [NEW] [gallery.html](file:///Users/miguelolivera/Desktop/MIGUEL/PYTHON/workWebChoroico/WebChoroico/core/templates/gallery.html)
- Estructura de encabezado institucional.
- Galería tipo Masonry o Grid balanceado.
- Soporte para visualización ampliada.

#### [NEW] [gallery.css](file:///Users/miguelolivera/Desktop/MIGUEL/PYTHON/workWebChoroico/WebChoroico/core/static/css/gallery.css)
- Animaciones de entrada de imágenes.
- Filtros suaves y overlays con texto descriptivo al hacer hover.
- Estilos para el visor modal (Carousel).

#### [MODIFY] [routes.py](file:///Users/miguelolivera/Desktop/MIGUEL/PYTHON/workWebChoroico/WebChoroico/core/routes.py)
- Actualizar la ruta `/gallery` para renderizar la nueva plantilla y pasar los datos de las imágenes.

## Plan de Verificación
- Verificar la correcta carga de imágenes.
- Probar la interactividad del carrusel/modal.
- Validar que el diseño sea responsivo y no pierda calidad en móviles.
