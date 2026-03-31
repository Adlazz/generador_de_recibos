from reportlab.lib.pagesizes import letter
from reportlab.lib.units import inch
from reportlab.pdfgen import canvas
from reportlab.lib import colors
from reportlab.platypus import Table, TableStyle
from reportlab.lib.utils import ImageReader
from num2words import num2words
from datetime import datetime
import os


def numero_a_letras(numero):
    """
    Convierte un número a su representación en letras en español.
    """
    try:
        # Separar parte entera y decimal
        partes = str(numero).split('.')
        entero = int(partes[0])

        # Convertir a letras
        letras = num2words(entero, lang='es').upper()

        # Agregar centavos si existen
        if len(partes) > 1:
            centavos = partes[1][:2].ljust(2, '0')
            return f"{letras} PESOS {centavos}/100 M.N."
        else:
            return f"{letras} PESOS 00/100 M.N."
    except:
        return "CANTIDAD NO VÁLIDA"


def generar_pdf_recibo(datos_recibo, qr_buffer, nombre_archivo):
    """
    Genera un PDF estilo talonario de recibo con todos los datos y el código QR.

    datos_recibo debe contener:
    - numero_recibo
    - fecha
    - nombre_pagador
    - concepto
    - monto
    - metodo_pago
    - nombre_receptor
    - hash_seguridad
    """
    # Crear directorio de salida si no existe
    os.makedirs('data', exist_ok=True)
    ruta_completa = os.path.join('data', nombre_archivo)

    # Tamaño de recibo estilo talonario: 7.5" x 4.5" (más compacto)
    recibo_width = 7.5 * inch
    recibo_height = 4.5 * inch

    # Crear el canvas
    c = canvas.Canvas(ruta_completa, pagesize=(recibo_width, recibo_height))

    # Colores para el diseño
    color_header = colors.HexColor('#2C3E50')
    color_accent = colors.HexColor('#3498DB')
    color_border = colors.HexColor('#95A5A6')

    # Márgenes
    margen_x = 0.4 * inch
    margen_y = 0.35 * inch

    # ========== BORDE DECORATIVO ==========
    c.setStrokeColor(color_border)
    c.setLineWidth(2)
    c.roundRect(0.15*inch, 0.15*inch, recibo_width - 0.3*inch, recibo_height - 0.3*inch, 8)

    # ========== ENCABEZADO CON FONDO ==========
    # Rectángulo de fondo para el encabezado (con más espacio arriba)
    c.setFillColor(color_header)
    c.roundRect(margen_x, recibo_height - margen_y - 0.7*inch,
                recibo_width - 2*margen_x, 0.55*inch, 5, fill=1, stroke=0)

    # Título del recibo (centrado verticalmente en la caja)
    c.setFillColor(colors.white)
    c.setFont("Helvetica-Bold", 16)
    c.drawString(margen_x + 0.15*inch, recibo_height - margen_y - 0.42*inch, "RECIBO")

    # Número de recibo en el encabezado
    c.setFont("Helvetica-Bold", 11)
    c.drawRightString(recibo_width - margen_x - 0.15*inch,
                     recibo_height - margen_y - 0.42*inch,
                     f"No. {datos_recibo['numero_recibo']:04d}")

    # ========== FECHA (alineada a la derecha, debajo del header) ==========
    c.setFillColor(colors.black)
    c.setFont("Helvetica", 9)
    c.drawRightString(recibo_width - margen_x, recibo_height - margen_y - 0.85*inch,
                     f"Fecha: {datos_recibo['fecha']}")

    # ========== SECCIÓN PRINCIPAL ==========
    y_pos = recibo_height - margen_y - 1.15*inch

    # RECIBÍ DE
    c.setFont("Helvetica-Bold", 10)
    c.setFillColor(color_accent)
    c.drawString(margen_x, y_pos, "RECIBÍ DE:")

    c.setFillColor(colors.black)
    c.setFont("Helvetica", 10)
    # Línea decorativa debajo del nombre
    nombre_width = c.stringWidth(datos_recibo['nombre_pagador'], "Helvetica", 10)
    c.drawString(margen_x + 1*inch, y_pos, datos_recibo['nombre_pagador'])
    c.setStrokeColor(color_accent)
    c.setLineWidth(0.5)
    c.line(margen_x + 1*inch, y_pos - 2, margen_x + 1*inch + nombre_width, y_pos - 2)

    # CONCEPTO
    y_pos -= 0.35*inch
    c.setFont("Helvetica-Bold", 10)
    c.setFillColor(color_accent)
    c.drawString(margen_x, y_pos, "CONCEPTO:")

    c.setFillColor(colors.black)
    c.setFont("Helvetica", 9)
    c.drawString(margen_x + 1*inch, y_pos, datos_recibo['concepto'])

    # ========== CAJA DE MONTO (destacada) ==========
    y_pos -= 0.55*inch

    # Rectángulo con el monto (con más altura para mejor espaciado)
    c.setFillColor(colors.HexColor('#ECF0F1'))
    c.setStrokeColor(color_accent)
    c.setLineWidth(1.5)
    c.roundRect(margen_x, y_pos - 0.15*inch, 2.5*inch, 0.55*inch, 5, fill=1, stroke=1)

    # Etiqueta "LA CANTIDAD DE:" (con más espacio arriba)
    c.setFillColor(color_accent)
    c.setFont("Helvetica-Bold", 8)
    c.drawString(margen_x + 0.1*inch, y_pos + 0.28*inch, "LA CANTIDAD DE:")

    # Monto en grande (centrado verticalmente)
    c.setFillColor(color_header)
    c.setFont("Helvetica-Bold", 16)
    c.drawString(margen_x + 0.1*inch, y_pos + 0.05*inch, f"${datos_recibo['monto']:,.2f}")

    # CANTIDAD EN LETRAS (debajo de la caja)
    y_pos -= 0.25*inch
    c.setFillColor(colors.black)
    c.setFont("Helvetica", 7)
    letras = numero_a_letras(datos_recibo['monto'])
    c.drawString(margen_x, y_pos, f"({letras})")

    # MÉTODO DE PAGO
    y_pos -= 0.25*inch
    c.setFont("Helvetica-Bold", 8)
    c.setFillColor(color_accent)
    c.drawString(margen_x, y_pos, "MÉTODO DE PAGO:")
    c.setFillColor(colors.black)
    c.setFont("Helvetica", 8)
    c.drawString(margen_x + 1.1*inch, y_pos, datos_recibo.get('metodo_pago', 'N/A'))

    # ========== FIRMA ==========
    y_pos = margen_y + 0.6*inch
    c.setStrokeColor(colors.black)
    c.setLineWidth(1)
    c.line(margen_x, y_pos, margen_x + 2.2*inch, y_pos)

    c.setFont("Helvetica", 9)
    c.drawString(margen_x, y_pos - 0.15*inch, datos_recibo.get('nombre_receptor', 'Receptor'))
    c.setFont("Helvetica-Oblique", 7)
    c.setFillColor(colors.HexColor('#7F8C8D'))
    c.drawString(margen_x, y_pos - 0.28*inch, "Firma y nombre de quien recibe")

    # ========== CÓDIGO QR (derecha) ==========
    qr_size = 1.3 * inch
    qr_x = recibo_width - margen_x - qr_size - 0.1*inch
    qr_y = recibo_height - margen_y - 2.9*inch

    # Cuadro para el QR
    c.setFillColor(colors.white)
    c.setStrokeColor(color_border)
    c.setLineWidth(1)
    c.roundRect(qr_x - 0.08*inch, qr_y - 0.08*inch,
                qr_size + 0.16*inch, qr_size + 0.3*inch, 5, fill=1, stroke=1)

    # Dibujar QR
    qr_buffer.seek(0)
    qr_image = ImageReader(qr_buffer)
    c.drawImage(qr_image, qr_x, qr_y,
                width=qr_size, height=qr_size, preserveAspectRatio=True, mask='auto')

    # Texto "CÓDIGO DE VERIFICACIÓN"
    c.setFillColor(color_accent)
    c.setFont("Helvetica-Bold", 6)
    c.drawCentredString(qr_x + qr_size/2, qr_y - 0.18*inch, "CÓDIGO DE VERIFICACIÓN")

    # ========== HASH DE SEGURIDAD (abajo) ==========
    c.setFillColor(colors.HexColor('#95A5A6'))
    c.setFont("Courier", 6)
    hash_text = f"Hash: {datos_recibo['hash_seguridad'][:24]}..."
    c.drawCentredString(recibo_width / 2, 0.28*inch, hash_text)

    # ========== NOTA AL PIE ==========
    c.setFont("Helvetica-Oblique", 6)
    c.drawCentredString(recibo_width / 2, 0.19*inch,
                       "Este recibo es un documento de control interno sin validez fiscal oficial")

    # Guardar PDF
    c.save()

    return ruta_completa
