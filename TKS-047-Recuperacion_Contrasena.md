# Feature: Sistema de Recuperación de Contraseña (Forgot Password)

**Ticket:** FEAT-047
**Estado:** Completado
**Fecha de Inicio:** 2025-12-17
**Fecha de Finalización:** PENDIENTE

---

## 🗣️ Ayudante en Jefe de Producto

### 1. Descripción de la Idea

Actualmente, si un usuario olvida su contraseña, no existe un mecanismo autónomo para recuperarla. Esto bloquea el acceso total a la cuenta y requiere soporte manual, lo cual no es escalable para un lanzamiento público. Esta funcionalidad implementará el flujo estándar de "Olvidé mi contraseña" mediante verificación por correo electrónico.

**Problema Detectado:**
La ausencia de este flujo es un bloqueador crítico para el lanzamiento (MVP). Los usuarios esperan poder recuperar su acceso sin intervención humana.

### 2. Historia de Usuario (User Story)

**Como** usuario registrado,
**Quiero** poder solicitar un enlace de restablecimiento de contraseña a mi correo electrónico,
**Para** definir una nueva contraseña y recuperar el acceso a mi cuenta si la olvido, de forma segura.

### 3. Requisitos Mínimos Viables (MVP)

1.  **Solicitud de Reset (Frontend + Backend):**
    *   Enlace "¿Olvidaste tu contraseña?" en el formulario de Login.
    *   Formulario simple para ingresar el email.
    *   Endpoint `POST /auth/forgot-password` que genere un token y envíe el correo.

2.  **Envío de Correo Electrónico:**
    *   Integración con servicio de email (ej. Resend, SendGrid o AWS SES, a definir por Arquitecto).
    *   Plantilla de correo con enlace único: `https://app.bitdatajournal.com/reset-password?token=XYZ`.

3.  **Página de Restablecimiento:**
    *   Ruta pública `/reset-password`.
    *   Validación del token (vigencia y firma).
    *   Formularios para ingresar y confirmar la nueva contraseña.
    *   Endpoint `POST /auth/reset-password`.

### 4. Impacto Esperado

*   **Autonomía:** 100% de los casos de olvido de contraseña resueltos por el usuario.
*   **Seguridad:** Eliminación de procesos manuales inseguros o cambios de clave por base de datos directos.
*   **Confianza:** Cumplimiento de expectativas básicas de funcionalidad SaaS.

### 5. Preguntas para el Equipo

*   **@Arquitecto_Software_Lider_Tecnico:**
    1.  ¿Qué servicio de envío de correos recomendamos usar considerando costos y facilidad de integración (ej. Resend vs Nodemailer puro)?
    2.  ¿Cuál debe ser el tiempo de expiración del token de recuperación (ej. 15 min, 1 hora)?
    3.  ¿Necesitamos rate-limiting específico para el endpoint de "forgot-password" para evitar spam?

*   **@Disenador_UX_UI:**
    1.  ¿Tenemos una plantilla base para correos transaccionales o diseño una simple de texto?
    2.  ¿La página de reset debe heredar el diseño de la Landing o del App Login?

*   **@Ingeniero_Calidad_QA:**
    1.  ¿Cómo probaremos el flujo de correo en entornos de desarrollo/test sin enviar emails reales a usuarios?

---

## 🏛️ Arquitecto de Software / Líder Técnico

**Análisis y Decisiones Técnicas:**

1.  **Servicio de Email:**
    *   **Selección:** Recomiendo **Resend** (resend.com).
    *   **Justificación:** Tienen una excelente integración con el ecosistema Vercel/Next.js, una API SDK muy limpia y un tier gratuito generoso para empezar. Además, facilita el diseño de templates con React Email si queremos evolucionar.
    *   **Alternativa:** Si queremos cero coste externo, podemos usar `nodemailer` con una cuenta de Gmail de servicio, pero es menos profesional y propenso a bloqueos. Vamos con Resend.

2.  **Seguridad del Token:**
    *   **Expiración:** **1 Hora**. 15 minutos es muy agresivo si el correo tarda en llegar.
    *   **Firma:** JWT firmado con una clave secreta específica para resets (no la misma de sesión), conteniendo el `user_id` y el hash de la contraseña actual.
    *   **Truco de Seguridad:** Incluir el hash de la contraseña actual en el payload del token asegura que si el usuario cambia la contraseña por otro medio, o solicita otro reset, los tokens viejos se invaliden automáticamente ("One-time use" implícito).

3.  **Rate Limiting:**
    *   **Mandatorio:** Absolutamente SI.
    *   **Política:** Máximo 3 solicitudes de reset por IP/Email cada hora. Esto previene ataques de enumeración y spam de costos en Resend. Podemos implementarlo con un middleware ligero usando Redis (Upstash) o una tabla simple en Supabase `rate_limits` si el tráfico es bajo. Para MVP, tabla en DB es suficiente.

---

## 🎨 Diseñador UX/UI

**Definición de Interfaz:**

1.  **Plantilla de Correo:**
    *   **Estructura:** Header con Logo (BitData Journal) centrado. Cuerpo con saludo "Hola, {Nombre}", texto explicativo breve y un botón primario (mismo estilo que la app, Azul Marino/Cian) con el texto "Restablecer Contraseña". Footer con link de soporte y texto legal pequeño.
    *   **Formato:** HTML limpio. Evitar imágenes pesadas para asegurar entregabilidad.

2.  **Diseño de Pantalla de Reset:**
    *   **Layout:** Debe usar el mismo `AuthLayout` que las páginas de Login y Registro para mantener la consistencia visual y de marca.
    *   **Flujo Visual:**
        1.  **Paso 1 (Request):** Card centrada, título "Recuperar Acceso", input Email, Botón "Enviar Enlace". Mensaje de éxito: "Si el correo existe, recibirás instrucciones...".
        2.  **Paso 2 (New Password):** Card centrada, título "Nueva Contraseña", input Password, input Confirm Password, checklist de requisitos (8 caracteres, 1 numero, etc. igual que registro).

---

## 🧪 Ingeniero de Calidad (QA)

**Estrategia de Pruebas:**

1.  **Pruebas de Correo (Dev/Test):**
    *   **Entorno Local:** No enviaremos correos reales. Configuraremos el servicio de email para que en modo `development`, simplemente haga un `console.log` del link de reset.
    *   **Opción Pro:** Usar **Ethereal Email** (servicio de Nodemailer) que captura los correos y te da una URL para verlos. Es genial para tests E2E y manuales sin spam.

2.  **Casos de Prueba Críticos:**
    *   **Usuario Inexistente:** Solicitar reset para `noexiste@gmail.com`. La UI debe decir "Si el correo existe..." (Security by Obscurity) para no revelar qué emails están registrados.
    *   **Token Expirado/Inválido:** Intentar usar un link viejo o manipulado. Debe redirigir a una página de error amigable "El enlace ha caducado".
    *   **Token Reutilizado:** Intentar usar el mismo link dos veces. Debe fallar.
    *   **Cambio Exitoso:** Verificar que tras el cambio, la contraseña vieja ya no funciona y la nueva sí.

---

## 🛠️ Refinador Técnico

**Plan de Implementación Detallado:**

1.  **Base de Datos (PostgreSQL/Supabase):**
    *   **Tabla `users`:** Añadir columnas para el manejo del token.
        ```sql
        ALTER TABLE users ADD COLUMN reset_password_token TEXT;
        ALTER TABLE users ADD COLUMN reset_password_expires TIMESTAMPTZ;
        ```
    *   **Tabla `rate_limits`:** Crear tabla para controlar el spam de correos.
        ```sql
        CREATE TABLE rate_limits (
            key TEXT PRIMARY KEY, -- Ej: 'forgot_pass_email@test.com'
            count INTEGER DEFAULT 1,
            expires_at TIMESTAMPTZ NOT NULL
        );
        ```

2.  **Backend (Node.js/Express):**
    *   **Dependencias:** Instalar `resend` (`npm install resend`).
    *   **Email Service:** Crear `src/services/emailService.js` como wrapper de Resend. Debe incluir método `sendPasswordResetEmail(email, token)`.
    *   **Rate Limiter Middleware:** Crear `src/middleware/dbRateLimiter.js` que use la tabla `rate_limits`.
    *   **Auth Controller:**
        *   `forgotPassword(req, res)`: Valida email, genera token (crypto.randomBytes), guarda en DB con expiración (1h), envía correo.
        *   `resetPassword(req, res)`: Valida token, verifica expiración, hashea nueva password, actualiza usuario, limpia token.

3.  **Frontend (Next.js):**
    *   **Páginas:**
        *   `src/app/(auth)/forgot-password/page.tsx`: Formulario simple de email.
        *   `src/app/(auth)/reset-password/page.tsx`: Formulario de doble input (password + confirm). Lee `searchParams.token`.
    *   **API Client:** Actualizar `src/utils/apiAuth.ts` (o similar) con `requestPasswordReset(email)` y `confirmPasswordReset(token, newPassword)`.

### 4. Estructura de Archivos Afectados (Anti-Colisión)

*   **[MODIFY]** `.workflow/EstructuraBBDD.sql` (Documentar cambios schema)
*   **[NEW]** `backend/src/services/emailService.js`
*   **[NEW]** `backend/src/middleware/dbRateLimiter.js`
*   **[MODIFY]** `backend/src/controllers/authController.js`
*   **[MODIFY]** `backend/src/routes/authRoutes.js`
*   **[NEW]** `frontend/src/app/(auth)/forgot-password/page.tsx`
*   **[NEW]** `frontend/src/app/(auth)/reset-password/page.tsx`
*   **[MODIFY]** `frontend/src/app/(auth)/login/page.tsx` (Agregar link)

---

## 👨‍💻 Desarrollador Senior

**Fecha de Finalización:** 2025-12-18

---

## 👨‍💻 Desarrollador Senior

**Implementación Realizada:**

1.  **Backend:**
    *   Se implementó el flujo completo con `authController.js` y `emailService.js`.
    *   Se usó **Resend** para el envío de correos.
    *   **Seguridad:** Se decidió mantener un mensaje de éxito genérico ("Si el correo existe...") para evitar la enumeración de usuarios, siguiendo las mejores prácticas de seguridad (OWASP).
    *   **Rate Limiting:** Se implementó `limiters/forgotPasswordLimiter` y protecciones globales.
    *   **i18n:** Todos los mensajes y logs están internacionalizados (frontend y backend).

2.  **Frontend:**
    *   Nuevas páginas: `/forgot-password` y `/reset-password`.
    *   Integración con el Modal de Login existente para una experiencia fluida.

3.  **Configuración Pendiente:**
    *   **Dominio de Correo:** Actualmente se usa el dominio de pruebas de Resend (`onboarding@resend.dev`). Queda pendiente la configuración del dominio personalizado (`soporte@bitdatajournal.com` o similar) una vez se adquiera el dominio definitivo. Esta tarea se ha movido al roadmap de infraestructura.

