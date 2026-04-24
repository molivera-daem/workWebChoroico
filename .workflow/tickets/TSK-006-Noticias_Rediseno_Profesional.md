# [TASK] TSK-006: Rediseño Profesional de la Sección de Noticias

Este ticket describe el trabajo necesario para transformar la sección de noticias en un feed profesional y dinámico, manteniendo la estética premium del sitio.

## Contexto
Actualmente, la sección de noticias reutiliza la plantilla de `about_us.html`. Se requiere crear una plantilla dedicada y un diseño de "cards" (tarjetas) que permita mostrar las noticias de forma organizada y visualmente atractiva.

## Objetivos
- [ ] Crear una nueva plantilla `news.html` dedicada.
- [ ] Implementar un diseño de tarjetas (Grid) para las noticias.
- [ ] Asegurar que el diseño sea responsivo y mantenga la línea profesional (vibrant colors, glassmorphism, micro-animations).
- [ ] Preparar la estructura para futura carga dinámica de datos.

## Cambios Propuestos

### Componente: Frontend (Plantillas y Estilos)

#### [NEW] [news.html](file:///Users/miguelolivera/Desktop/MIGUEL/PYTHON/workWebChoroico/WebChoroico/core/templates/news.html)
Crear una nueva plantilla que herede de `base.html` y contenga:
- Sección de encabezamiento con título y descripción.
- Contenedor de noticias tipo Grid.
- Diseño de tarjetas con: Imagen, Etiqueta (categoría), Fecha, Título, Extracto y Botón/Enlace "Leer más".

#### [MODIFY] [routes.py](file:///Users/miguelolivera/Desktop/MIGUEL/PYTHON/workWebChoroico/WebChoroico/core/routes.py)
Actualizar la ruta `@main.route('/news')` para que renderice `news.html` en lugar de `about_us.html`.

#### [MODIFY] [index.css](file:///Users/miguelolivera/Desktop/MIGUEL/PYTHON/workWebChoroico/WebChoroico/core/static/css/index.css) (o archivo de estilos correspondiente)
Añadir estilos específicos para las tarjetas de noticias:
- Efectos de hover (elevación, brillo).
- Uso de sombras suaves y bordes redondeados.
- Tipografía legible y jerarquizada.

## Plan de Verificación

### Verificación Manual
- Acceder a `/news` y verificar que el nuevo diseño se visualiza correctamente.
- Comprobar la responsividad en diferentes tamaños de pantalla (móvil, tablet, desktop).
- Verificar que los efectos de hover y animaciones funcionan fluidamente.
