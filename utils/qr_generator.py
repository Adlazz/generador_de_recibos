import qrcode
import hashlib
import json
from io import BytesIO


def generar_hash_seguridad(numero_recibo, fecha, monto, nombre_pagador):
    """
    Genera un hash SHA-256 único basado en los datos del recibo
    para garantizar la autenticidad del documento.
    """
    datos = f"{numero_recibo}|{fecha}|{monto}|{nombre_pagador}"
    hash_obj = hashlib.sha256(datos.encode('utf-8'))
    return hash_obj.hexdigest()


def generar_qr(numero_recibo, fecha, monto, nombre_pagador, concepto):
    """
    Genera un código QR con los datos del recibo y un hash de seguridad.
    Retorna la imagen del QR en formato BytesIO.
    """
    hash_seguridad = generar_hash_seguridad(numero_recibo, fecha, monto, nombre_pagador)

    # Crear datos del QR en formato JSON
    datos_qr = {
        "numero_recibo": numero_recibo,
        "fecha": fecha,
        "monto": monto,
        "pagador": nombre_pagador,
        "concepto": concepto,
        "hash": hash_seguridad[:16]  # Primeros 16 caracteres del hash
    }

    # Convertir a JSON string
    qr_content = json.dumps(datos_qr, ensure_ascii=False)

    # Generar QR
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=10,
        border=4,
    )
    qr.add_data(qr_content)
    qr.make(fit=True)

    img = qr.make_image(fill_color="black", back_color="white")

    # Convertir a BytesIO
    img_buffer = BytesIO()
    img.save(img_buffer, format='PNG')
    img_buffer.seek(0)

    return img_buffer, hash_seguridad


def verificar_qr(datos_recibo, hash_proporcionado):
    """
    Verifica si el hash del recibo coincide con el hash generado.
    """
    hash_calculado = generar_hash_seguridad(
        datos_recibo['numero_recibo'],
        datos_recibo['fecha'],
        datos_recibo['monto'],
        datos_recibo['nombre_pagador']
    )
    return hash_calculado == hash_proporcionado
