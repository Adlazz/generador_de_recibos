# 🚀 PASOS RÁPIDOS PARA DEPLOYMENT

## ✅ Lo que YA está hecho:

- ✅ Sistema de autenticación implementado
- ✅ Código pusheado a GitHub
- ✅ Dependencias actualizadas en requirements.txt
- ✅ Archivos de configuración creados

---

## 📋 LO QUE NECESITAS HACER AHORA:

### Opción A: Deployment Rápido con Contraseña de Ejemplo

**⚡ Para probar rápido (5 minutos):**

1. **Ve a Streamlit Cloud:** https://share.streamlit.io/

2. **Click en "New app":**
   - Repository: `Adlazz/generador_de_recibos`
   - Branch: `main`
   - Main file: `app.py`

3. **Click en "Advanced settings" → "Secrets"**

4. **Copia y pega este contenido:**
   ```toml
   [credentials]

   [credentials.usernames.admin]
   email = "admin@ejemplo.com"
   name = "Administrador"
   password = "$2b$12$tJGWQi74hajOuAS/uV7llOLeYkOteeVd6pRfYZ39rBVdldZ5lGT6G"

   [cookie]
   name = "generador_recibos_auth"
   key = "clave_temporal_12345xyz"
   expiry_days = 30
   ```

5. **Click en "Deploy!"**

6. **Login con:**
   - Username: `admin`
   - Password: `admin123`

**⚠️ DESPUÉS del deploy, cambia la contraseña siguiendo "Opción B"**

---

### Opción B: Deployment Seguro con Tu Propia Contraseña

**🔒 Para producción (10 minutos):**

1. **En tu computadora, genera tu contraseña:**
   ```bash
   python generate_password.py
   ```

2. **Cuando te pregunte:**
   - Username: `adrian` (o el que quieras)
   - Nombre: `Adrian`
   - Email: `adrianlazz@hotmail.com`
   - Password: `TU_PASSWORD_SECRETO`

3. **Copia el output que te da** (algo como):
   ```toml
   [credentials.usernames.adrian]
   email = "adrianlazz@hotmail.com"
   name = "Adrian"
   password = "$2b$12$xyz123...HASH_AQUI"
   ```

4. **Ve a Streamlit Cloud** → "New app" → "Advanced settings" → "Secrets"

5. **Pega:**
   ```toml
   [credentials]

   [credentials.usernames.adrian]
   email = "adrianlazz@hotmail.com"
   name = "Adrian"
   password = "$2b$12$xyz123...EL_HASH_QUE_GENERASTE"

   [cookie]
   name = "generador_recibos_auth"
   key = "mi_clave_super_secreta_xyz789"
   expiry_days = 30
   ```

6. **Deploy!**

7. **Login con:**
   - Username: `adrian`
   - Password: `TU_PASSWORD_SECRETO`

---

## 📁 Archivos de Referencia:

- **[secrets_example.toml](secrets_example.toml)** - Ejemplo listo para copiar
- **[STREAMLIT_CLOUD_CONFIG.md](STREAMLIT_CLOUD_CONFIG.md)** - Guía paso a paso detallada
- **[AUTH_SETUP.md](AUTH_SETUP.md)** - Setup local completo
- **[DEPLOY.md](DEPLOY.md)** - Guía de deployment en todas las plataformas

---

## 🔑 Credenciales de Ejemplo (para pruebas):

**Username:** `admin`
**Password:** `admin123`

**⚠️ IMPORTANTE:** Estas credenciales son temporales. Cámbialas después del primer login.

---

## 👥 Agregar más usuarios después:

1. Ve a tu app → Settings → Secrets
2. Ejecuta localmente: `python generate_password.py`
3. Agrega el nuevo usuario al final:
   ```toml
   [credentials.usernames.nuevo_usuario]
   email = "nuevo@ejemplo.com"
   name = "Nuevo Usuario"
   password = "$2b$12$HASH_GENERADO"
   ```
4. Guarda (la app se reinicia automáticamente)

---

## 🎯 ¿Qué hace el sistema de autenticación?

✅ **Login seguro** al abrir la app
✅ **Cada usuario** tiene su historial privado de recibos
✅ **Los recibos** se guardan en archivos separados (`recibos_username.json`)
✅ **Logout** seguro con botón en sidebar
✅ **Sesión persistente** por 30 días (configurable)

---

## 🐛 Problemas comunes:

**"Error al cargar la configuración de autenticación"**
→ No configuraste los Secrets en Streamlit Cloud

**"Usuario o contraseña incorrectos" (siempre falla)**
→ El hash está mal. Genera uno nuevo con `python generate_password.py`

**"No veo la opción de Secrets"**
→ Click en "Advanced settings" ANTES de hacer Deploy

---

## 📞 ¿Necesitas ayuda?

- **Guía completa:** [DEPLOY.md](DEPLOY.md)
- **Setup local:** [AUTH_SETUP.md](AUTH_SETUP.md)
- **Config Streamlit Cloud:** [STREAMLIT_CLOUD_CONFIG.md](STREAMLIT_CLOUD_CONFIG.md)

---

**🚀 ¡Ve y haz el deployment! Todo está listo.**
