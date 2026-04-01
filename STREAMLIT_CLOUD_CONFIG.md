# 🔐 Configuración de Secrets en Streamlit Cloud

## ⚠️ IMPORTANTE: Debes hacer esto ANTES de que la app funcione

Tu app ahora tiene autenticación. Sigue estos pasos para configurarla en Streamlit Cloud:

---

## 📝 Paso a Paso

### 1. Ve a tu app en Streamlit Cloud

URL: https://share.streamlit.io/

### 2. Encuentra tu app deployada

Si aún no la has deployado:
- Click en "New app"
- Repository: `Adlazz/generador_de_recibos`
- Branch: `main`
- Main file: `app.py`
- **NO HAGAS CLICK EN DEPLOY AÚN**

### 3. Configura los Secrets

1. **Click en "Advanced settings"** (antes de hacer deploy)
2. **Click en la pestaña "Secrets"**
3. **Pega el siguiente contenido:**

```toml
[credentials]

[credentials.usernames.adrian]
email = "adrianlazz@hotmail.com"
name = "Adrian"
password = "GENERA_AQUI_TU_PASSWORD"

[cookie]
name = "generador_recibos_auth"
key = "clave_super_secreta_cambiame_12345xyz"
expiry_days = 30
```

### 4. Genera tu contraseña hasheada

**OPCIÓN A - Local (Recomendado):**

En tu computadora, ejecuta:
```bash
python generate_password.py
```

Cuando te pida:
- Username: `adrian` (o el que quieras)
- Nombre: `Adrian`
- Email: `adrianlazz@hotmail.com`
- Contraseña: `tu_password_secreto`

Te dará algo como:
```toml
[credentials.usernames.adrian]
email = "adrianlazz@hotmail.com"
name = "Adrian"
password = "$2b$12$xyz123abc...ESTE_ES_EL_HASH_REAL"
```

**OPCIÓN B - Online:**
1. Ve a: https://bcrypt-generator.com/
2. Ingresa tu contraseña deseada
3. Copia el hash generado (empieza con `$2b$12$...`)
4. Pégalo en el campo `password`

### 5. Actualiza el Secret en Streamlit Cloud

Reemplaza `"GENERA_AQUI_TU_PASSWORD"` con el hash que generaste.

**Ejemplo final:**
```toml
[credentials]

[credentials.usernames.adrian]
email = "adrianlazz@hotmail.com"
name = "Adrian"
password = "$2b$12$xyz123abc456def789ghi...HASH_REAL_AQUI"

[cookie]
name = "generador_recibos_auth"
key = "mi_clave_aleatoria_super_secreta_789xyz"
expiry_days = 30
```

### 6. Guarda y Deploy

1. Click en **"Save"**
2. Click en **"Deploy!"**

---

## 🎉 ¡Listo!

Ahora tu app tendrá login. Usa:
- **Username:** `adrian` (o el que configuraste)
- **Password:** La contraseña que usaste para generar el hash

---

## 👥 Agregar más usuarios después

1. Ve a tu app en Streamlit Cloud
2. Settings → Secrets
3. Genera nuevo hash con `python generate_password.py`
4. Agrega al secret:
```toml
[credentials.usernames.nuevo_usuario]
email = "nuevo@ejemplo.com"
name = "Nombre Nuevo"
password = "$2b$12$HASH_DEL_NUEVO_USUARIO"
```
5. Guarda (la app se reinicia automáticamente)

---

## 🔒 Migrar tus recibos actuales

Si ya tienes recibos en la app actual, se guardan en `data/recibos.json`.

Después del deploy con autenticación, tus recibos estarán en `data/recibos_adrian.json` (archivo nuevo vacío).

**Para no perder tus recibos:**

Si tienes acceso SSH/shell al deployment (no aplicable en Streamlit Cloud gratuito), ejecuta:
```bash
cp data/recibos.json data/recibos_adrian.json
```

**En Streamlit Cloud:**
Los datos se pierden en cada reinicio, así que:
1. Descarga todos tus PDFs antes del deploy
2. Vuelve a generarlos después del login

---

## ❓ Preguntas

**¿Puedo tener varios usuarios?**
Sí, agrega más secciones `[credentials.usernames.NOMBRE]`

**¿Cada usuario ve los recibos de los demás?**
No, cada usuario tiene su propio historial privado.

**¿Cómo cambio mi contraseña?**
1. Genera nuevo hash con `python generate_password.py`
2. Actualiza el secret en Streamlit Cloud
3. Guarda

**¿Olvidé mi contraseña?**
1. Genera un nuevo hash
2. Reemplázalo en los Secrets
3. Usa la nueva contraseña

---

**🔗 Más info:** Ver [DEPLOY.md](DEPLOY.md) y [AUTH_SETUP.md](AUTH_SETUP.md)
