---
description: Cómo configurar el despliegue usando Git Version Control en cPanel
---

# Despliegue con Git Version Control (cPanel)

Esta guía explica cómo conectar tu repositorio de GitHub directamente con cPanel para evitar usar FTP y actualizaciones manuales.

## Prerrequisitos
- Acceso a cPanel.
- Repositorio en GitHub (privado o público).

## Paso 1: Crear el Repositorio en cPanel
1.  En cPanel, busca y abre la herramienta **Git Version Control**.
2.  Haz clic en el botón **Create** (Crear).
3.  Completa los campos:
    *   **Clone URL:** La URL de tu repositorio (ej. `https://github.com/TU_USUARIO/WebChoroico.git`).
    *   **Repository Path:** La carpeta donde se guardará la app.
        *   🛑 **Importante:** Si usas "Setup Python App", asegúrate de que este "Path" sea el mismo que definiste como "App Directory" en la configuración de Python (ej. `repositories/WebChoroico`).
    *   **Repository Name:** `WebChoroico`.
4.  Haz clic en **Create**.

> **Nota:** Si tu repositorio es **Privado**, cPanel te pedirá credenciales o fallará. Si falla, deberás generar una "SSH Key" en cPanel y agregarla en GitHub (Settings -> Deploy Keys), luego usar la URL SSH (`git@github.com:...`) en lugar de HTTPS.

## Paso 2: Automatizar Actualizaciones (Webhooks)
Para que cPanel sepa cuándo hay cambios en GitHub:

1.  En la lista de repositorios de **Git Version Control**, haz clic en **Manage** junto a tu repo.
2.  Ve a la pestaña **Pull or Deploy**.
3.  Copia la **Webhook URL** (se ve como `https://tudominio.cl/cpanelwebcall/...`).
4.  Ve a tu repositorio en **GitHub**.
5.  Entra a **Settings** -> **Webhooks** -> **Add Webhook**.
    *   **Payload URL:** Pega la URL de cPanel.
    *   **Content type:** Selecciona `application/json`.
    *   **Trigger:** Deja "Just the push event".
6.  Guarda el Webhook.

## Paso 3: Configurar .cpanel.yml (Reinicio Automático)
Para que la aplicación Python se reinicie automáticamente después de recibir código nuevo, hemos creado el archivo `.cpanel.yml` en tu proyecto.

1.  Abre el archivo `.cpanel.yml` en tu editor.
2.  **Verifica la ruta:** Asegúrate de que `DEPLOYPATH` coincida con la ruta real en tu servidor (cambia `miguelolivera` por tu usuario real de cPanel si es distinto).
3.  Sube este archivo a GitHub (`git push`).

## Resumen del Flujo
1.  Editas código en tu PC.
2.  `git push origin main`.
3.  GitHub avisa a cPanel (Webhook).
4.  cPanel hace `git pull` y descarga los cambios.
5.  cPanel lee `.cpanel.yml` y ejecuta tareas (ej. reiniciar la app).
