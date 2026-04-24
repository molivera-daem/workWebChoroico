# [TASK] TSK-008: Integración de Documentos Descargables

Este ticket describe la implementación de una funcionalidad para que los usuarios puedan ver o descargar documentos (como certificados) directamente desde la página de inicio.

## Contexto
Se requiere que en la sección de "Certificados" de la página principal exista un botón funcional que permita al usuario acceder a un documento de ejemplo. Esta integración debe ser limpia y no alterar el diseño profesional existente.

## Objetivos
- [ ] Crear el directorio `WebChoroico/core/static/docs` para almacenar documentos.
- [ ] Incorporar un documento de ejemplo (PDF/Texto) en el repositorio.
- [ ] Modificar `index.html` para que el botón de "Certificados" apunte al documento.
- [ ] Asegurar que el enlace abra el documento en una pestaña nueva o inicie la descarga.
- [ ] Verificar que el diseño de la tarjeta de servicio se mantenga íntegro.

## Cambios Propuestos

### Componente: Backend / Estructura de Archivos
- **Directorio**: `WebChoroico/core/static/docs/` [NEW]
- **Archivo**: `WebChoroico/core/static/docs/ejemplo_certificado.txt` [NEW] (o PDF si es posible).

### Componente: Frontend
#### [MODIFY] [index.html](file:///Users/miguelolivera/Desktop/MIGUEL/PYTHON/workWebChoroico/WebChoroico/core/templates/index.html)
- Actualizar el enlace `<a href="#">` en la tarjeta de Certificados para usar `url_for` apuntando al archivo estático.

## Plan de Verificación
- Hacer clic en el botón y verificar que el documento se abre o descarga correctamente.
- Comprobar que no hay desplazamientos visuales inesperados en la sección de servicios.
