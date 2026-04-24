# TSK-009: Integración de Supabase como Backend as a Service (BaaS)

## 📋 Descripción
Implementar la infraestructura necesaria para conectar la aplicación Flask con Supabase, permitiendo el manejo de base de datos (PostgreSQL), autenticación y almacenamiento de archivos (Storage).

## 🎯 Objetivos
1.  Configurar el cliente oficial de Supabase en el núcleo de la aplicación.
2.  Migrar la gestión de configuración a variables de entorno seguras.
3.  Establecer un patrón de diseño para el acceso a datos.

## 👥 Roles Involucrados
- **Arquitecto de Software:** Definir la estructura del cliente y el patrón de integración.
- **Desarrollador Senior:** Implementar el cliente y actualizar las rutas existentes.
- **Ingeniero DevOps:** Configurar las variables de entorno y dependencias.

## 🛠 Tareas Técnicas

### Fase 1: Entorno y Dependencias (DevOps)
- [ ] Instalar `supabase` y `python-dotenv`.
- [ ] Actualizar `requirements.txt`.
- [ ] Configurar `.env.example` con las nuevas claves necesarias.

### Fase 2: Arquitectura y Conectividad (Arquitecto)
- [ ] Crear `WebChoroico/core/database/` para centralizar la lógica de datos.
- [ ] Implementar `supabase_client.py` con el patrón Singleton o Factory.

### Fase 3: Implementación de Prueba (Desarrollador Senior)
- [ ] Crear una tabla de prueba en Supabase (ej. `config_site`).
- [ ] Implementar una ruta de validación `/test-db` para confirmar la conexión.

## 📊 Criterios de Aceptación
- El servidor Flask debe iniciar sin errores con las nuevas dependencias.
- La conexión con Supabase debe ser exitosa y manejada mediante variables de entorno.
- No debe haber credenciales "hardcodeadas" en el código fuente.
