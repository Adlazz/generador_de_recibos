# 🔐 Configuración de Autenticación

Esta aplicación ahora incluye un sistema de autenticación multi-usuario. Cada usuario tiene su propio historial de recibos privado.

---

## 🚀 Configuración Rápida (Primera Vez)

### 1. Instalar Dependencias

```bash
pip install -r requirements.txt
```

### 2. Generar Usuarios y Contraseñas

El archivo `.streamlit/secrets.toml` ya existe pero tiene contraseñas de ejemplo que **NO FUNCIONAN**.

Ejecuta el script para generar contraseñas reales:

```bash
python generate_password.py
```

**Ejemplo de uso:**
```
Ingresa el username (ej: juan_perez): adrian
Ingresa el nombre completo (ej: Juan Pérez): Adrian Martinez
Ingresa el email (ej: juan@ejemplo.com): adrian@ejemplo.com
Ingresa la contraseña: miPassword123
```

El script generará algo como:

```toml
[credentials.usernames.adrian]
email = "adrian@ejemplo.com"
name = "Adrian Martinez"
password = "$2b$12$xyz123...hash_real_aqui"
```

### 3. Actualizar el archivo `.streamlit/secrets.toml`

Abre el archivo `.streamlit/secrets.toml` y:

1. **Borra las secciones de usuarios de ejemplo** (admin, usuario1)
2. **Pega los usuarios que generaste** con el script
3. **Cambia la cookie key** por algo aleatorio y único:
   ```toml
   [cookie]
   name = "generador_recibos_auth"
   key = "tu_clave_super_secreta_12345"  # ← Cambia esto
   expiry_days = 30
   ```

**Ejemplo de archivo final:**

```toml
[credentials]

[credentials.usernames.adrian]
email = "adrian@ejemplo.com"
name = "Adrian Martinez"
password = "$2b$12$real_hash_generado_aqui"

[credentials.usernames.maria]
email = "maria@ejemplo.com"
name = "Maria Lopez"
password = "$2b$12$otro_hash_real_aqui"

[cookie]
name = "generador_recibos_auth"
key = "clave_aleatoria_muy_segura_xyz789"
expiry_days = 30
```

### 4. Ejecutar la Aplicación

```bash
streamlit run app.py
```

### 5. Iniciar Sesión

Usa el **username** y **contraseña** que configuraste.

---

## 👥 Gestión de Usuarios

### Agregar un nuevo usuario

1. Ejecuta: `python generate_password.py`
2. Copia el output
3. Pégalo en `.streamlit/secrets.toml` dentro de `[credentials.usernames]`
4. Guarda y reinicia la app

### Cambiar contraseña

1. Genera un nuevo hash con `python generate_password.py`
2. Reemplaza el campo `password` del usuario en `secrets.toml`
3. Guarda y reinicia la app

### Eliminar usuario

1. Borra la sección completa del usuario en `secrets.toml`
2. Guarda y reinicia la app

---

## 📂 Archivos de Datos

Cada usuario tiene su propio archivo JSON:

```
data/
├── recibos_adrian.json      # Recibos de adrian
├── recibos_maria.json       # Recibos de maria
└── recibos_*.pdf            # PDFs generados
```

Los usuarios **NO** pueden ver los recibos de otros usuarios.

---

## 🔒 Seguridad

### ⚠️ IMPORTANTE:

1. **NUNCA** commitees el archivo `.streamlit/secrets.toml` a Git (ya está en `.gitignore`)
2. **NUNCA** compartas los hashes de contraseña
3. **SIEMPRE** usa contraseñas fuertes en producción
4. **CAMBIA** la cookie key por algo aleatorio y único

### Para Producción (Streamlit Cloud):

- Los secrets se configuran en la interfaz web de Streamlit Cloud
- **NO** se suben al repositorio de GitHub
- Ver instrucciones en [DEPLOY.md](DEPLOY.md)

---

## 🐛 Problemas Comunes

### "Error al cargar la configuración de autenticación"
- Verifica que `.streamlit/secrets.toml` existe
- Revisa que no tenga errores de sintaxis TOML
- Asegúrate de tener las secciones `[credentials]` y `[cookie]`

### "Usuario o contraseña incorrectos" (siempre falla)
- Los hashes de ejemplo NO funcionan
- Debes generar hashes reales con `python generate_password.py`

### No veo mis recibos antiguos
- Los recibos antiguos están en `data/recibos.json`
- Los nuevos están en `data/recibos_username.json`
- Para migrar: `cp data/recibos.json data/recibos_tuusername.json`

---

## 📚 Recursos

- [Streamlit Authenticator Docs](https://github.com/mkhorasani/Streamlit-Authenticator)
- [TOML Format](https://toml.io/)
- [Deployment Guide](DEPLOY.md)

---

**¿Listo para deployment?** Lee [DEPLOY.md](DEPLOY.md) para instrucciones detalladas.
