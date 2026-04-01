# 📄 Generador de Recibos

**Sistema profesional de generación de recibos con código QR de seguridad**

Aplicación web intuitiva para generar recibos de honorarios personalizados con diseño tipo talonario, numeración automática, conversión de montos a letras y código QR único de verificación.

![Python](https://img.shields.io/badge/Python-3.8+-blue.svg)
![Streamlit](https://img.shields.io/badge/Streamlit-1.31-red.svg)
![License](https://img.shields.io/badge/License-MIT-green.svg)

---

## ✨ Características

- 🎨 **Diseño Profesional**: Recibos estilo talonario con formato compacto (7.5" x 4.5")
- 🔢 **Numeración Automática**: Sistema correlativo de números de recibo
- 💰 **Monto en Letras**: Conversión automática de números a texto en español
- 🔒 **Código QR de Seguridad**: Hash SHA-256 único para verificar autenticidad
- 📊 **Historial Completo**: Registro de todos los recibos generados
- 🔍 **Búsqueda Inteligente**: Filtrado por nombre, concepto o número
- 📥 **Descarga PDF**: Exportación individual de cada recibo
- 📈 **Estadísticas**: Total de recibos y monto acumulado

---

## 🚀 Instalación

### Requisitos Previos
- Python 3.8 o superior
- pip (gestor de paquetes de Python)

### Paso 1: Clonar el Repositorio
```bash
git clone https://github.com/tu-usuario/generador_de_recibos.git
cd generador_de_recibos
```

### Paso 2: Crear Entorno Virtual (Recomendado)
```bash
# Windows
python -m venv venv
venv\Scripts\activate

# macOS/Linux
python3 -m venv venv
source venv/bin/activate
```

### Paso 3: Instalar Dependencias
```bash
pip install -r requirements.txt
```

### Paso 4: Ejecutar la Aplicación
```bash
streamlit run app.py
```

La aplicación se abrirá automáticamente en tu navegador en `http://localhost:8501`

---

## 📖 Guía de Uso

### 1️⃣ Generar un Nuevo Recibo

1. **Accede a la pestaña "Nuevo Recibo"**

2. **Completa los campos requeridos:**
   - **Número de Recibo**: Se genera automáticamente (puedes editarlo si es necesario)
   - **Fecha de Pago**: Selecciona la fecha en que se realizó el pago
   - **Nombre del Pagador**: Nombre completo de quien realizó el pago
   - **Concepto**: Descripción del servicio (ej. "Honorarios Mes Abril 2026")
   - **Monto**: Cantidad pagada en números
   - **Método de Pago**: Selecciona entre Efectivo, Transferencia, Depósito, etc.
   - **Nombre del Receptor**: Tu nombre o de quien recibe el pago

3. **Haz clic en "🎯 Generar Recibo"**

4. **Descarga el PDF** usando el botón que aparecerá

### 2️⃣ Ver el Historial

1. **Accede a la pestaña "Historial"**

2. **Visualiza estadísticas:**
   - Total de recibos generados
   - Monto total acumulado
   - Número del último recibo

3. **Busca recibos específicos:**
   - Escribe en el buscador el nombre del pagador, concepto o número
   - Los resultados se filtrarán automáticamente

4. **Descarga recibos anteriores:**
   - Expande el recibo que desees
   - Haz clic en "📥 Descargar PDF"

---

## 📁 Estructura del Proyecto

```
generador_de_recibos/
├── app.py                    # Aplicación principal de Streamlit
├── requirements.txt          # Dependencias de Python
├── .gitignore               # Archivos excluidos de git
├── README.md                # Este archivo
├── utils/                   # Módulos auxiliares
│   ├── __init__.py
│   ├── pdf_generator.py     # Generación de PDFs
│   └── qr_generator.py      # Generación de códigos QR
├── data/                    # Archivos generados (auto-creado)
│   ├── recibos.json         # Base de datos de recibos
│   └── recibo_*.pdf         # PDFs generados
└── venv/                    # Entorno virtual (no incluido en git)
```

---

## 🎨 Ejemplo de Recibo Generado

El recibo incluye:

- ✅ Encabezado con fondo oscuro y número de recibo
- ✅ Borde decorativo redondeado
- ✅ Fecha del pago
- ✅ Datos del pagador con línea decorativa
- ✅ Concepto del servicio
- ✅ Caja destacada con el monto en números y letras
- ✅ Método de pago
- ✅ Espacio para firma del receptor
- ✅ Código QR con hash de verificación
- ✅ Nota legal al pie

---

## 🔒 Seguridad del Recibo

Cada recibo incluye un **código QR con hash SHA-256** único generado a partir de:
- Número de recibo
- Fecha
- Monto
- Nombre del pagador

Este hash garantiza que:
- ✅ El recibo no ha sido alterado
- ✅ Los datos son auténticos
- ✅ Se puede verificar la integridad del documento

El código QR contiene toda la información del recibo en formato JSON para validación rápida.

---

## ⚙️ Configuración Avanzada

### Cambiar el Puerto de la Aplicación
```bash
streamlit run app.py --server.port 8080
```

### Ejecutar en Modo Producción
```bash
streamlit run app.py --server.headless true
```

### Personalizar Tema
Crea un archivo `.streamlit/config.toml`:
```toml
[theme]
primaryColor = "#3498DB"
backgroundColor = "#FFFFFF"
secondaryBackgroundColor = "#F0F2F6"
textColor = "#262730"
font = "sans serif"
```

---

## 🛠️ Tecnologías Utilizadas

| Tecnología | Uso |
|------------|-----|
| **Streamlit** | Framework de interfaz web |
| **ReportLab** | Generación de PDFs profesionales |
| **qrcode** | Creación de códigos QR |
| **num2words** | Conversión de números a letras en español |
| **Pillow** | Procesamiento de imágenes |
| **hashlib** | Generación de hash SHA-256 de seguridad |

---

## 📊 Casos de Uso

### Freelancers y Profesionales Independientes
- Generar recibos de honorarios por servicios
- Llevar control de ingresos mensuales
- Tener respaldo documental de pagos recibidos

### Pequeños Negocios
- Recibos de compra-venta
- Control interno de operaciones
- Historial de clientes y transacciones

### Arrendadores
- Recibos de renta mensual
- Comprobantes de pago de servicios
- Control de inquilinos

### Prestadores de Servicios
- Pagos de consultoría
- Servicios profesionales (diseño, desarrollo, etc.)
- Clases particulares

---

## ❓ Preguntas Frecuentes (FAQ)

### ¿Los recibos generados tienen validez fiscal oficial?
No, estos recibos son para **control interno** y no tienen validez fiscal oficial.

### ¿Puedo editar un recibo ya generado?
No, los recibos son inmutables una vez generados para mantener la integridad del sistema. Si necesitas corregir algo, genera un nuevo recibo.

### ¿Dónde se almacenan mis datos?
Los datos se guardan localmente en el archivo `data/recibos.json`. No se envía información a servidores externos.

### ¿Puedo personalizar el diseño del recibo?
Actualmente el diseño es fijo.

### ¿Cómo puedo respaldar mi información?
Simplemente copia la carpeta `data/` a un lugar seguro. Contiene todos los recibos y el historial.

### ¿Funciona sin internet?
Sí, la aplicación funciona completamente offline una vez instalada.

### ¿Puedo usar esto en mi empresa?
Sí, este proyecto es open-source bajo licencia MIT. Puedes usarlo libremente.

---

## 🐛 Solución de Problemas

### Error: "ModuleNotFoundError"
**Solución:** Asegúrate de haber instalado las dependencias:
```bash
pip install -r requirements.txt
```

### Error: "Port 8501 is already in use"
**Solución:** Cierra otras instancias de Streamlit o usa otro puerto:
```bash
streamlit run app.py --server.port 8502
```

### Los PDFs no se generan
**Solución:** Verifica que tengas permisos de escritura en la carpeta `data/`:
```bash
# Windows
icacls data /grant Users:F

# macOS/Linux
chmod -R 755 data/
```

### El código QR no aparece en el PDF
**Solución:** Reinstala Pillow:
```bash
pip uninstall Pillow
pip install Pillow==10.2.0
```

---

---

## 🤝 Contribuciones

Las contribuciones son bienvenidas. Para cambios importantes:

1. Fork el proyecto
2. Crea una rama para tu feature (`git checkout -b feature/AmazingFeature`)
3. Commit tus cambios (`git commit -m 'Add: nueva funcionalidad'`)
4. Push a la rama (`git push origin feature/AmazingFeature`)
5. Abre un Pull Request

---

## 📝 Changelog

### v1.0.0 (Marzo 2026)
- ✅ Generación de recibos en PDF
- ✅ Diseño estilo talonario profesional
- ✅ Código QR de seguridad
- ✅ Historial de recibos
- ✅ Búsqueda y filtrado
- ✅ Numeración automática
- ✅ Conversión de monto a letras

---

## 📄 Licencia

Este proyecto está bajo la Licencia MIT. Ver el archivo `LICENSE` para más detalles.

```
MIT License

Copyright (c) 2026 [Tu Nombre]

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:
...
```

---

## 👤 Autor

**Tu Nombre**
- GitHub: [@tu-usuario](https://github.com/tu-usuario)
- Email: tu-email@ejemplo.com

---

## 🙏 Agradecimientos

- [Streamlit](https://streamlit.io/) - Por el framework de desarrollo
- [ReportLab](https://www.reportlab.com/) - Por la librería de generación de PDFs
- [num2words](https://github.com/savoirfairelinux/num2words) - Por la conversión a letras

---

## 📞 Soporte

Si tienes problemas o preguntas:

1. Revisa la sección [FAQ](#-preguntas-frecuentes-faq)
2. Busca en [Issues](https://github.com/tu-usuario/generador_de_recibos/issues) si alguien ya reportó el problema
3. Abre un nuevo Issue con detalles específicos

---

## ⭐ ¿Te gusta el proyecto?

Si este proyecto te resulta útil, considera:
- ⭐ Darle una estrella en GitHub
- 🐛 Reportar bugs
- 💡 Sugerir nuevas funcionalidades
- 🤝 Contribuir con código
- 📢 Compartirlo con otros

---

<div align="center">

**Hecho con ❤️ y Python**

[📖 Documentación](README.md) · [🐛 Reportar Bug](https://github.com/tu-usuario/generador_de_recibos/issues) · [✨ Nueva Feature](https://github.com/tu-usuario/generador_de_recibos/issues)

</div>
