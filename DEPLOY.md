# 🚀 Guía de Deployment - Generador de Recibos

Esta guía te ayudará a desplegar tu aplicación de generador de recibos en diferentes plataformas. Elige la opción que mejor se adapte a tus necesidades.

---

## 📋 Tabla de Contenidos

1. [Streamlit Community Cloud](#1-streamlit-community-cloud-recomendado) (⭐ **Recomendado** - Gratis y Simple)
2. [Railway](#2-railway)
3. [Render](#3-render)
4. [Heroku](#4-heroku)
5. [Docker](#5-docker)
6. [VPS/Servidor Propio](#6-vpsservidor-propio)
7. [Consideraciones Importantes](#consideraciones-importantes)

---

## 1. Streamlit Community Cloud (⭐ Recomendado)

**Ventajas:**
- ✅ Completamente gratis
- ✅ Deploy automático desde GitHub
- ✅ Perfecto para aplicaciones Streamlit
- ✅ SSL/HTTPS incluido
- ✅ Sin tarjeta de crédito requerida

### Paso 1: Preparar el Repositorio en GitHub

1. **Sube tu proyecto a GitHub** (si aún no lo has hecho):
```bash
git init
git add .
git commit -m "Preparar para deployment"
git branch -M main
git remote add origin https://github.com/tu-usuario/generador_de_recibos.git
git push -u origin main
```

2. **Asegúrate de que tu `.gitignore` esté configurado** (ya está listo en tu proyecto)

### Paso 2: Configurar Streamlit Cloud

1. Ve a [share.streamlit.io](https://share.streamlit.io/)
2. Inicia sesión con tu cuenta de GitHub
3. Haz clic en **"New app"**
4. Completa la configuración:
   - **Repository:** `tu-usuario/generador_de_recibos`
   - **Branch:** `main`
   - **Main file path:** `app.py`
5. **NO hagas clic en Deploy todavía** - primero configura los Secrets

### Paso 3: Configurar Secrets (Autenticación) 🔐

⚠️ **IMPORTANTE:** La aplicación ahora tiene sistema de autenticación. Debes configurar los usuarios ANTES de hacer deploy.

1. **En la página de configuración de tu app**, ve a **"Advanced settings"** → **"Secrets"**

2. **Copia y pega el siguiente contenido**, modificando los usuarios y contraseñas:

```toml
[credentials]

[credentials.usernames.admin]
email = "admin@ejemplo.com"
name = "Administrador"
password = "$2b$12$KIXxnF7nF7nF7nF7nF7nF.zQYj9h9h9h9h9h9h9h9h9h9h9h9h"

# Agrega más usuarios aquí si es necesario
# [credentials.usernames.usuario1]
# email = "usuario1@ejemplo.com"
# name = "Usuario Uno"
# password = "$2b$12$HASH_GENERADO_AQUI"

[cookie]
name = "generador_recibos_auth"
key = "random_signature_key_123456789"
expiry_days = 30
```

3. **Para generar contraseñas hasheadas:**

   **Opción A - Usando el script incluido (Recomendado):**
   ```bash
   # En tu computadora local
   pip install streamlit-authenticator bcrypt
   python generate_password.py
   ```

   **Opción B - Online:**
   - Usa [bcrypt-generator.com](https://bcrypt-generator.com/)
   - Ingresa la contraseña
   - Copia el hash generado
   - Pégalo en el campo `password`

4. **Guarda los Secrets** haciendo clic en "Save"

5. **Ahora sí, haz clic en "Deploy!"**

### Paso 4: Configuración de Persistencia de Datos

⚠️ **Importante:** Streamlit Cloud reinicia la aplicación periódicamente, lo que puede causar pérdida de datos del archivo `data/recibos.json`.

**Soluciones:**

#### Opción A: Usar Streamlit Secrets + Base de Datos Externa (Recomendado)
En el futuro podrías migrar a una base de datos como PostgreSQL o MongoDB Atlas (gratis).

#### Opción B: Aceptar que los datos son temporales
Para uso personal o demos, puedes aceptar que los datos se pierdan ocasionalmente.

#### Opción C: Descargar backups regularmente
Descarga el archivo `recibos.json` regularmente desde la sección de Historial.

### Paso 4: Acceder a tu Aplicación

Tu aplicación estará disponible en:
```
https://tu-usuario-generador-de-recibos-app-random123.streamlit.app
```

Puedes personalizar el dominio en la configuración de la app.

---

## 2. Railway

**Ventajas:**
- ✅ $5 USD de crédito gratis al mes
- ✅ Deploy automático desde GitHub
- ✅ Soporta persistencia de datos con volúmenes

### Paso 1: Crear cuenta en Railway

1. Ve a [railway.app](https://railway.app/)
2. Inicia sesión con GitHub

### Paso 2: Crear `railway.json`

Crea un archivo `railway.json` en la raíz del proyecto:

```json
{
  "$schema": "https://railway.app/railway.schema.json",
  "build": {
    "builder": "NIXPACKS"
  },
  "deploy": {
    "startCommand": "streamlit run app.py --server.port $PORT --server.address 0.0.0.0",
    "restartPolicyType": "ON_FAILURE",
    "restartPolicyMaxRetries": 10
  }
}
```

### Paso 3: Deploy

1. En Railway, haz clic en **"New Project"**
2. Selecciona **"Deploy from GitHub repo"**
3. Elige tu repositorio `generador_de_recibos`
4. Railway detectará automáticamente que es una app Python
5. Espera a que termine el deployment

### Paso 4: Configurar Variables de Entorno (Opcional)

En la pestaña **Variables**:
```
PORT=8501
```

### Paso 5: Configurar Volumen Persistente (Opcional)

Para que los datos no se pierdan:
1. Ve a la pestaña **"Settings"** de tu servicio
2. Scroll hasta **"Volumes"**
3. Haz clic en **"Add Volume"**
4. Mount Path: `/app/data`

---

## 3. Render

**Ventajas:**
- ✅ Plan gratis disponible
- ✅ SSL automático
- ✅ Deploy desde GitHub

### Paso 1: Crear cuenta en Render

1. Ve a [render.com](https://render.com/)
2. Inicia sesión con GitHub

### Paso 2: Crear archivo de configuración

Crea un archivo `render.yaml` en la raíz:

```yaml
services:
  - type: web
    name: generador-recibos
    runtime: python
    buildCommand: pip install -r requirements.txt
    startCommand: streamlit run app.py --server.port $PORT --server.address 0.0.0.0
    envVars:
      - key: PYTHON_VERSION
        value: 3.8.18
```

### Paso 3: Deploy

1. En Render, haz clic en **"New +"** → **"Web Service"**
2. Conecta tu repositorio de GitHub
3. Configura:
   - **Name:** generador-recibos
   - **Runtime:** Python 3
   - **Build Command:** `pip install -r requirements.txt`
   - **Start Command:** `streamlit run app.py --server.port $PORT --server.address 0.0.0.0`
4. Haz clic en **"Create Web Service"**

⚠️ **Nota:** El plan gratis se "duerme" después de 15 minutos de inactividad.

---

## 4. Heroku

**Ventajas:**
- ✅ Plataforma madura y confiable
- ⚠️ Ya no tiene plan gratuito (desde Nov 2022)

### Paso 1: Instalar Heroku CLI

**Windows:**
Descarga el instalador desde [devcenter.heroku.com](https://devcenter.heroku.com/articles/heroku-cli)

**macOS:**
```bash
brew tap heroku/brew && brew install heroku
```

**Linux:**
```bash
curl https://cli-assets.heroku.com/install.sh | sh
```

### Paso 2: Crear archivos de configuración

#### `setup.sh`
```bash
mkdir -p ~/.streamlit/

echo "\
[server]\n\
headless = true\n\
port = $PORT\n\
enableCORS = false\n\
\n\
[browser]\n\
serverAddress = \"0.0.0.0\"\n\
serverPort = $PORT\n\
" > ~/.streamlit/config.toml
```

#### `Procfile`
```
web: sh setup.sh && streamlit run app.py
```

### Paso 3: Deploy

```bash
# Iniciar sesión
heroku login

# Crear app
heroku create generador-recibos-app

# Agregar buildpack de Python
heroku buildpacks:set heroku/python

# Deploy
git push heroku main

# Abrir en navegador
heroku open
```

### Paso 4: Ver logs

```bash
heroku logs --tail
```

---

## 5. Docker

**Ventajas:**
- ✅ Portable y reproducible
- ✅ Ideal para servidores propios
- ✅ Control total del entorno

### Paso 1: Crear `Dockerfile`

```dockerfile
FROM python:3.8-slim

WORKDIR /app

# Instalar dependencias del sistema
RUN apt-get update && apt-get install -y \
    build-essential \
    curl \
    software-properties-common \
    && rm -rf /var/lib/apt/lists/*

# Copiar archivos
COPY requirements.txt .
COPY app.py .
COPY utils/ ./utils/

# Instalar dependencias de Python
RUN pip install --no-cache-dir -r requirements.txt

# Crear directorio de datos
RUN mkdir -p /app/data

# Exponer puerto
EXPOSE 8501

# Configurar Streamlit
RUN mkdir -p ~/.streamlit/
RUN echo "\
[server]\n\
headless = true\n\
port = 8501\n\
enableCORS = false\n\
\n\
[browser]\n\
serverAddress = \"0.0.0.0\"\n\
gatherUsageStats = false\n\
" > ~/.streamlit/config.toml

# Comando de inicio
CMD ["streamlit", "run", "app.py", "--server.port=8501", "--server.address=0.0.0.0"]
```

### Paso 2: Crear `docker-compose.yml`

```yaml
version: '3.8'

services:
  app:
    build: .
    ports:
      - "8501:8501"
    volumes:
      - ./data:/app/data
    restart: unless-stopped
    environment:
      - STREAMLIT_SERVER_PORT=8501
      - STREAMLIT_SERVER_ADDRESS=0.0.0.0
```

### Paso 3: Crear `.dockerignore`

```
venv/
__pycache__/
*.pyc
*.pyo
*.pyd
.Python
.git
.gitignore
.vscode/
.idea/
*.md
!README.md
.env
.DS_Store
```

### Paso 4: Construir y ejecutar

```bash
# Construir imagen
docker build -t generador-recibos .

# Ejecutar contenedor
docker run -p 8501:8501 -v $(pwd)/data:/app/data generador-recibos

# O usar docker-compose
docker-compose up -d

# Ver logs
docker-compose logs -f

# Detener
docker-compose down
```

### Acceder a la aplicación

```
http://localhost:8501
```

---

## 6. VPS/Servidor Propio

**Ventajas:**
- ✅ Control total
- ✅ Sin límites de uso
- ✅ Datos 100% bajo tu control

### Paso 1: Preparar el servidor (Ubuntu/Debian)

```bash
# Conectar al servidor
ssh usuario@tu-servidor.com

# Actualizar sistema
sudo apt update && sudo apt upgrade -y

# Instalar Python y pip
sudo apt install -y python3 python3-pip python3-venv git nginx

# Instalar certbot para SSL
sudo apt install -y certbot python3-certbot-nginx
```

### Paso 2: Clonar y configurar la aplicación

```bash
# Crear directorio
sudo mkdir -p /var/www/generador-recibos
sudo chown $USER:$USER /var/www/generador-recibos

# Clonar repositorio
cd /var/www/generador-recibos
git clone https://github.com/tu-usuario/generador_de_recibos.git .

# Crear entorno virtual
python3 -m venv venv
source venv/bin/activate

# Instalar dependencias
pip install -r requirements.txt
```

### Paso 3: Crear servicio systemd

Crea el archivo `/etc/systemd/system/generador-recibos.service`:

```ini
[Unit]
Description=Generador de Recibos - Streamlit App
After=network.target

[Service]
Type=simple
User=www-data
WorkingDirectory=/var/www/generador-recibos
Environment="PATH=/var/www/generador-recibos/venv/bin"
ExecStart=/var/www/generador-recibos/venv/bin/streamlit run app.py --server.port 8501 --server.address localhost

Restart=always
RestartSec=10

[Install]
WantedBy=multi-user.target
```

### Paso 4: Configurar nginx

Crea el archivo `/etc/nginx/sites-available/generador-recibos`:

```nginx
server {
    listen 80;
    server_name tu-dominio.com;

    location / {
        proxy_pass http://localhost:8501;
        proxy_http_version 1.1;
        proxy_set_header Upgrade $http_upgrade;
        proxy_set_header Connection "upgrade";
        proxy_set_header Host $host;
        proxy_set_header X-Real-IP $remote_addr;
        proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;
        proxy_set_header X-Forwarded-Proto $scheme;
        proxy_read_timeout 86400;
    }
}
```

### Paso 5: Activar y configurar SSL

```bash
# Activar sitio
sudo ln -s /etc/nginx/sites-available/generador-recibos /etc/nginx/sites-enabled/

# Verificar configuración
sudo nginx -t

# Reiniciar nginx
sudo systemctl restart nginx

# Configurar SSL con certbot
sudo certbot --nginx -d tu-dominio.com

# Iniciar servicio de la app
sudo systemctl start generador-recibos
sudo systemctl enable generador-recibos

# Ver estado
sudo systemctl status generador-recibos
```

### Paso 6: Comandos útiles

```bash
# Ver logs
sudo journalctl -u generador-recibos -f

# Reiniciar servicio
sudo systemctl restart generador-recibos

# Detener servicio
sudo systemctl stop generador-recibos

# Actualizar aplicación
cd /var/www/generador-recibos
git pull
sudo systemctl restart generador-recibos
```

---

## Consideraciones Importantes

### 🔒 Seguridad

1. **Nunca commitees datos sensibles** al repositorio
2. **Usa variables de entorno** para información sensible
3. **Configura HTTPS/SSL** en producción
4. **Limita el acceso** con autenticación si es necesario

### 💾 Persistencia de Datos

La aplicación usa un archivo JSON local (`data/recibos.json`). Para ambientes de producción:

**Opciones:**
- Usar volúmenes persistentes (Docker, Railway)
- Migrar a una base de datos (PostgreSQL, MongoDB)
- Implementar backups automáticos

### 📊 Monitoreo

Para aplicaciones en producción, considera:
- Logs centralizados
- Alertas de errores
- Monitoreo de uptime
- Backups automáticos

### 🚀 Optimizaciones

```python
# En app.py, agrega al inicio:
import streamlit as st

st.set_page_config(
    page_title="Generador de Recibos",
    page_icon="📄",
    layout="centered",
    initial_sidebar_state="collapsed"  # Optimización
)
```

---

## 👥 Gestión de Usuarios

### Agregar un Nuevo Usuario

#### En Streamlit Cloud:

1. **Genera el hash de la contraseña:**
   ```bash
   python generate_password.py
   ```

2. **Ve a tu app en Streamlit Cloud** → **Settings** → **Secrets**

3. **Agrega el nuevo usuario** en la sección `[credentials.usernames]`:
   ```toml
   [credentials.usernames.nuevo_usuario]
   email = "nuevo@ejemplo.com"
   name = "Nuevo Usuario"
   password = "$2b$12$HASH_GENERADO"
   ```

4. **Guarda los cambios** - la app se reiniciará automáticamente

#### En Local:

1. Ejecuta `python generate_password.py`
2. Copia el output al archivo `.streamlit/secrets.toml`
3. Guarda y reinicia la app

### Cambiar Contraseña de un Usuario

1. Genera un nuevo hash con `python generate_password.py`
2. Reemplaza el valor del campo `password` del usuario
3. Guarda los cambios

### Eliminar un Usuario

1. Borra la sección completa del usuario en `secrets.toml`
2. Guarda los cambios

### Usuarios por Defecto

El archivo `.streamlit/secrets.toml` incluye contraseñas de ejemplo que **DEBES CAMBIAR** antes de usar en producción.

⚠️ **Seguridad:** Los hashes en el archivo `secrets.toml` son solo ejemplos y no funcionan. Debes generar tus propios hashes reales.

---

## 📞 Solución de Problemas

### Error: "Port already in use"
```bash
# Encontrar proceso usando el puerto
lsof -i :8501
# Matar proceso
kill -9 <PID>
```

### Error: "ModuleNotFoundError" en producción
Asegúrate de que `requirements.txt` esté actualizado:
```bash
pip freeze > requirements.txt
```

### La app se reinicia constantemente
Revisa los logs para ver el error específico:
```bash
# Streamlit Cloud: Ver en dashboard
# Heroku: heroku logs --tail
# Docker: docker logs <container-id>
# VPS: sudo journalctl -u generador-recibos -f
```

### Los archivos PDF no se generan
Verifica permisos del directorio `data/`:
```bash
sudo chown -R www-data:www-data /var/www/generador-recibos/data
sudo chmod -R 755 /var/www/generador-recibos/data
```

### Error: "Error al cargar la configuración de autenticación"
**Causa:** El archivo `secrets.toml` no está configurado o tiene errores de sintaxis.

**Solución:**
1. Verifica que exista `.streamlit/secrets.toml` (local) o esté configurado en Streamlit Cloud
2. Verifica la sintaxis TOML (usa [toml-lint](https://www.toml-lint.com/))
3. Asegúrate de que tenga las secciones `[credentials]` y `[cookie]`

### Error: "Usuario o contraseña incorrectos" (siempre)
**Causa:** Los hashes de contraseña no son válidos.

**Solución:**
1. Los hashes de ejemplo en `secrets.toml` NO funcionan
2. Debes generar hashes reales con `python generate_password.py`
3. Copia los hashes generados al archivo `secrets.toml`

### No puedo ver mis recibos antiguos después de implementar autenticación
**Causa:** Los recibos antiguos están en `data/recibos.json` pero la app ahora usa `data/recibos_username.json`

**Solución:**
```bash
# Copia los recibos antiguos al archivo del usuario
cp data/recibos.json data/recibos_tuusername.json
```

---

## 🎯 Recomendación Final

Para esta aplicación específica, **recomendamos Streamlit Community Cloud** para empezar:

✅ Es gratis
✅ Es simple (3 clicks para deploy)
✅ Es perfecto para apps Streamlit
✅ Incluye SSL automático
✅ Deploy automático con cada push a GitHub

Si necesitas mayor control o persistencia de datos garantizada, usa **Railway** o un **VPS propio**.

---

## 📚 Recursos Adicionales

- [Documentación de Streamlit Cloud](https://docs.streamlit.io/streamlit-community-cloud)
- [Railway Docs](https://docs.railway.app/)
- [Render Docs](https://render.com/docs)
- [Docker Docs](https://docs.docker.com/)
- [Nginx Docs](https://nginx.org/en/docs/)

---

**¡Buena suerte con tu deployment! 🚀**

Si tienes problemas, revisa los logs y la documentación oficial de cada plataforma.
