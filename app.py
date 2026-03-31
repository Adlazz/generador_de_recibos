import streamlit as st
import json
import os
from datetime import datetime
from utils.qr_generator import generar_qr
from utils.pdf_generator import generar_pdf_recibo


# Configuración de la página
st.set_page_config(
    page_title="Generador de Recibos",
    page_icon="📄",
    layout="centered"
)


def cargar_recibos():
    """Carga el historial de recibos desde el archivo JSON"""
    archivo_recibos = 'data/recibos.json'
    if os.path.exists(archivo_recibos):
        try:
            with open(archivo_recibos, 'r', encoding='utf-8') as f:
                return json.load(f)
        except:
            return []
    return []


def guardar_recibo(datos_recibo):
    """Guarda un nuevo recibo en el archivo JSON"""
    archivo_recibos = 'data/recibos.json'
    os.makedirs('data', exist_ok=True)

    recibos = cargar_recibos()
    recibos.append(datos_recibo)

    with open(archivo_recibos, 'w', encoding='utf-8') as f:
        json.dump(recibos, f, ensure_ascii=False, indent=2)


def obtener_siguiente_numero():
    """Obtiene el siguiente número de recibo disponible"""
    recibos = cargar_recibos()
    if recibos:
        return max([r.get('numero_recibo', 0) for r in recibos]) + 1
    return 1


# INTERFAZ PRINCIPAL
st.title("📄 Generador de Recibos")
st.markdown("---")

# Tabs para organizar la interfaz
tab1, tab2 = st.tabs(["Nuevo Recibo", "Historial"])

with tab1:
    st.subheader("Generar Nuevo Recibo")

    # Número de recibo (automático pero editable)
    numero_recibo = st.number_input(
        "Número de Recibo",
        min_value=1,
        value=obtener_siguiente_numero(),
        step=1,
        help="Número correlativo del recibo"
    )

    # Fecha
    col1, col2 = st.columns(2)
    with col1:
        fecha = st.date_input(
            "Fecha de Pago",
            value=datetime.now(),
            help="Fecha en que se realizó el pago"
        )

    # Convertir fecha a string
    fecha_str = fecha.strftime("%d/%m/%Y")

    # Datos del pagador
    st.markdown("#### Datos del Pagador")
    nombre_pagador = st.text_input(
        "Nombre de quien pagó",
        placeholder="Ej: Juan Pérez García",
        help="Nombre completo de la persona o empresa que realizó el pago"
    )

    # Concepto
    st.markdown("#### Concepto del Pago")
    concepto = st.text_input(
        "Concepto",
        value="Honorarios Mes Abril 2026",
        placeholder="Ej: Honorarios Mes Abril 2026",
        help="Descripción del servicio o concepto del pago"
    )

    # Monto
    monto = st.number_input(
        "Monto ($)",
        min_value=0.0,
        value=0.0,
        step=100.0,
        format="%.2f",
        help="Monto total del pago"
    )

    # Método de pago
    metodo_pago = st.selectbox(
        "Método de Pago",
        ["Efectivo", "Transferencia Bancaria", "Depósito", "Cheque", "Otro"],
        help="Forma en que se realizó el pago"
    )

    # Datos del receptor
    st.markdown("#### Datos del Receptor (Quien recibe el pago)")
    nombre_receptor = st.text_input(
        "Nombre del Receptor",
        placeholder="Ej: María López",
        help="Tu nombre o el de la persona que recibe el pago"
    )

    # Botón para generar recibo
    st.markdown("---")
    if st.button("🎯 Generar Recibo", type="primary", use_container_width=True):
        # Validaciones
        errores = []
        if not nombre_pagador:
            errores.append("- Nombre del pagador")
        if not concepto:
            errores.append("- Concepto del pago")
        if monto <= 0:
            errores.append("- Monto (debe ser mayor a 0)")
        if not nombre_receptor:
            errores.append("- Nombre del receptor")

        if errores:
            st.error("Por favor completa los siguientes campos:\n" + "\n".join(errores))
        else:
            with st.spinner("Generando recibo..."):
                try:
                    # Generar código QR
                    qr_buffer, hash_seguridad = generar_qr(
                        numero_recibo,
                        fecha_str,
                        str(monto),
                        nombre_pagador,
                        concepto
                    )

                    # Preparar datos del recibo
                    datos_recibo = {
                        'numero_recibo': numero_recibo,
                        'fecha': fecha_str,
                        'nombre_pagador': nombre_pagador,
                        'concepto': concepto,
                        'monto': monto,
                        'metodo_pago': metodo_pago,
                        'nombre_receptor': nombre_receptor,
                        'hash_seguridad': hash_seguridad,
                        'fecha_generacion': datetime.now().strftime("%Y-%m-%d %H:%M:%S")
                    }

                    # Generar PDF
                    nombre_archivo = f"recibo_{numero_recibo:04d}_{fecha.strftime('%Y%m%d')}.pdf"
                    ruta_pdf = generar_pdf_recibo(datos_recibo, qr_buffer, nombre_archivo)

                    # Guardar en base de datos JSON
                    guardar_recibo(datos_recibo)

                    # Mostrar éxito
                    st.success(f"✅ Recibo #{numero_recibo:04d} generado exitosamente!")

                    # Botón de descarga
                    with open(ruta_pdf, 'rb') as pdf_file:
                        st.download_button(
                            label="📥 Descargar Recibo PDF",
                            data=pdf_file,
                            file_name=nombre_archivo,
                            mime="application/pdf",
                            use_container_width=True
                        )

                    # Mostrar información del hash
                    with st.expander("🔒 Información de Seguridad"):
                        st.code(f"Hash de verificación: {hash_seguridad}", language=None)
                        st.caption("Este código único garantiza la autenticidad del recibo")

                except Exception as e:
                    st.error(f"❌ Error al generar el recibo: {str(e)}")

with tab2:
    st.subheader("Historial de Recibos")

    recibos = cargar_recibos()

    if recibos:
        # Ordenar por número de recibo descendente
        recibos_ordenados = sorted(recibos, key=lambda x: x.get('numero_recibo', 0), reverse=True)

        # Mostrar estadísticas
        col1, col2, col3 = st.columns(3)
        with col1:
            st.metric("Total Recibos", len(recibos))
        with col2:
            total_monto = sum([r.get('monto', 0) for r in recibos])
            st.metric("Monto Total", f"${total_monto:,.2f}")
        with col3:
            if recibos_ordenados:
                st.metric("Último Recibo", f"#{recibos_ordenados[0]['numero_recibo']:04d}")

        st.markdown("---")

        # Buscador
        busqueda = st.text_input("🔍 Buscar recibo", placeholder="Por nombre, concepto o número...")

        # Filtrar recibos
        if busqueda:
            recibos_filtrados = [
                r for r in recibos_ordenados
                if busqueda.lower() in r.get('nombre_pagador', '').lower()
                or busqueda.lower() in r.get('concepto', '').lower()
                or busqueda in str(r.get('numero_recibo', ''))
            ]
        else:
            recibos_filtrados = recibos_ordenados

        # Mostrar recibos
        for recibo in recibos_filtrados:
            with st.expander(
                f"Recibo #{recibo.get('numero_recibo', 0):04d} - {recibo.get('nombre_pagador', 'N/A')} - ${recibo.get('monto', 0):,.2f}"
            ):
                col1, col2 = st.columns(2)
                with col1:
                    st.write(f"**Fecha:** {recibo.get('fecha', 'N/A')}")
                    st.write(f"**Pagador:** {recibo.get('nombre_pagador', 'N/A')}")
                    st.write(f"**Concepto:** {recibo.get('concepto', 'N/A')}")
                with col2:
                    st.write(f"**Monto:** ${recibo.get('monto', 0):,.2f}")
                    st.write(f"**Método:** {recibo.get('metodo_pago', 'N/A')}")
                    st.write(f"**Receptor:** {recibo.get('nombre_receptor', 'N/A')}")

                st.caption(f"🔒 Hash: {recibo.get('hash_seguridad', 'N/A')[:16]}...")

                # Botón para regenerar PDF
                nombre_archivo = f"recibo_{recibo.get('numero_recibo', 0):04d}_{recibo.get('fecha', '').replace('/', '')}.pdf"
                ruta_pdf = os.path.join('data', nombre_archivo)

                if os.path.exists(ruta_pdf):
                    with open(ruta_pdf, 'rb') as pdf_file:
                        st.download_button(
                            label="📥 Descargar PDF",
                            data=pdf_file,
                            file_name=nombre_archivo,
                            mime="application/pdf",
                            key=f"download_{recibo.get('numero_recibo', 0)}"
                        )
    else:
        st.info("📭 No hay recibos generados aún. Crea tu primer recibo en la pestaña 'Nuevo Recibo'.")


# Footer
st.markdown("---")
st.caption("💡 Sistema de Generación de Recibos - Control No Oficial")
