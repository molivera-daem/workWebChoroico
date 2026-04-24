# Ticket: Implementación de Integración Continua (CI/CD)

**Ticket:** TSK-002
**Estado:** Completado
**Fecha de Inicio:** 2025-12-29
**Fecha de Finalización:** 2025-12-29
**Depende de:** TSK-001

---

## �️ Ayudante en Jefe de Producto

### 1. Descripción de la Idea

El proyecto ya cuenta con una base sólida estandarizada (`TSK-001`). Para profesionalizar el ciclo de vida del software, es imprescindible automatizar el despliegue a producción. Actualmente, el proceso es manual, lo que introduce riesgos de error humano y lentitud.
Se requiere implementar un flujo de Integración Continua (CI/CD) utilizando GitHub Actions para conectar el repositorio con el servidor Anaconda Web (cPanel) vía FTP.

**Problema Detectado:**
Dependencia de despliegues manuales y falta de validación automática antes de subir código a producción.

### 2. Historia de Usuario (User Story)

**Como** Ingeniero DevOps y Desarrollador,
**Quiero** que el código se despliegue automáticamente a Anaconda Web al hacer push a `main`,
**Para** asegurar que producción siempre tenga la última versión estable sin intervención manual.

### 3. Requisitos Mínimos Viables (MVP)

1.  **Workflow de GitHub Actions:**
    *   Crear archivo `.github/workflows/deploy.yml`.
    *   Configurar el disparador (trigger) en `push` a `main`.
    *   Utilizar la acción `FTP-Deploy-Action` (estándar y robusta para cPanel).

2.  **Seguridad y Configuración:**
    *   Definir los secretos necesarios en GitHub (`FTP_SERVER`, `FTP_USERNAME`, `FTP_PASSWORD`).
    *   Configurar exclusiones en el despliegue para no subir archivos locales o sensibles (`.env`, `venv/`, `.git/`).

3.  **Reinicio de Aplicación:**
    *   El flujo debe incluir un mecanismo para reiniciar la aplicación Python en cPanel (ej. "tocando" el archivo `passenger_wsgi.py`).

### 4. Impacto Esperado

*   **Automatización:** 100% libre de intervención manual para deploy.
*   **Confiabilidad:** Reducción de errores por archivos faltantes u olvidados.
*   **Velocidad:** Tiempo de despliegue reducido a segundos/minutos tras el push.

### 5. Preguntas para el Equipo

*   **@Ingeniero_DevOps:**
    1.  ¿Qué estrategia de reinicio es la más efectiva para Passenger en cPanel compartido?
    2.  ¿Qué permisos FTP específicos necesitamos?

---

## 🛠️ Ingeniero DevOps

**Implementación Técnica:**

1.  **Estrategia de Despliegue (FTP):**
    *   **Decisión:** Se utilizará `SamKirkland/FTP-Deploy-Action` por su compatibilidad nativa con cPanel y facilidad de exclusión de archivos.
    *   **Justificación:** SSH suele estar restringido o es complejo en hostings compartidos. FTP es universal y suficiente para este caso de uso.

2.  **Reinicio de Passenger:**
    *   **Método:** Se actualizará el timestamp del archivo `passenger_wsgi.py`. Passenger detecta este cambio y recarga la aplicación en la siguiente petición.
    *   **En GitHub Actions:** Esto es implícito si el archivo se sube, pero si no cambia, la acción de deploy podría no tocarlo. *Nota: Para cambios solo de templates, a veces no es necesario reiniciar, pero por seguridad lo haremos.*

3.  **Entregables (Realizados):**
    *   Archivo `.github/workflows/deploy.yml` creado.
    *   Documentación de secretos entregada.

*(Implementación Actualizada - Estrategia Vercel + cPanel)*

## 🔄 Cambio de Estrategia: Vercel (Staging Temporal)
Debido a la falta de visibilidad de "Setup Python App" en cPanel, utilizaremos **Vercel** como entorno de pruebas (Staging). Esto permitirá ver la web funcionando de inmediato mientras se resuelve el acceso en el hosting definitivo.

## 📚 Guía de Activación en Vercel

### Paso 1: Configurar Vercel
1.  Crea una cuenta gratuita en [Vercel.com](https://vercel.com) vinculada a tu GitHub.
2.  Haz clic en **"Add New" -> "Project"**.
3.  Importa tu repositorio `WebChoroico`.
4.  Vercel detectará el archivo `vercel.json` que acabo de crear.
5.  En **Environment Variables**, agrega:
    *   `FLASK_ENV`: `production`

### Paso 2: Despliegue
Cada vez que hagas `git push` a GitHub, Vercel desplegará automáticamente y te dará una URL (ej. `web-choroico.vercel.app`).

---

**Entregables Finales:**
*   [x] Archivo `vercel.json` configurado para despliegue serverless.
*   [x] Punto de entrada `app.py` configurado y desacoplado del nombre de la carpeta (vía rename a `core/`).
*   [x] Despliegue exitoso verificado en Vercel.
*   [x] Documentación de estrategia de emergencia (Git Version Control cPanel) preparada.
