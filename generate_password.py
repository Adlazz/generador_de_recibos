"""
Script auxiliar para generar hashes de contraseñas
para el sistema de autenticación del generador de recibos.

Uso:
    python generate_password.py

Luego ingresa el username y password cuando se te solicite.
El script generará el hash que debes copiar en .streamlit/secrets.toml
"""

import bcrypt
import streamlit_authenticator as stauth

def generar_hash_password():
    """Genera un hash bcrypt para una contraseña"""
    print("\n" + "="*60)
    print("  GENERADOR DE PASSWORDS PARA GENERADOR DE RECIBOS")
    print("="*60 + "\n")

    username = input("Ingresa el username (ej: juan_perez): ").strip()
    nombre = input("Ingresa el nombre completo (ej: Juan Pérez): ").strip()
    email = input("Ingresa el email (ej: juan@ejemplo.com): ").strip()
    password = input("Ingresa la contraseña: ").strip()

    if not username or not password or not nombre or not email:
        print("\n❌ Error: Todos los campos son obligatorios")
        return

    # Generar hash usando streamlit-authenticator
    hashed_password = stauth.Hasher([password]).generate()[0]

    print("\n" + "="*60)
    print("  ✅ HASH GENERADO EXITOSAMENTE")
    print("="*60 + "\n")

    print("Copia y pega lo siguiente en .streamlit/secrets.toml:\n")
    print("-"*60)
    print(f"""
[credentials.usernames.{username}]
email = "{email}"
name = "{nombre}"
password = "{hashed_password}"
""")
    print("-"*60)

    print("\nPara Streamlit Cloud:")
    print("1. Ve a tu app en share.streamlit.io")
    print("2. Settings > Secrets")
    print("3. Agrega el bloque de arriba en la sección [credentials.usernames]")
    print("\n" + "="*60 + "\n")

if __name__ == "__main__":
    try:
        generar_hash_password()
    except KeyboardInterrupt:
        print("\n\n❌ Operación cancelada por el usuario")
    except Exception as e:
        print(f"\n❌ Error: {str(e)}")
