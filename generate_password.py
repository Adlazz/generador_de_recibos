"""
Script auxiliar para generar hashes de contraseñas
para el sistema de autenticación del generador de recibos.

Uso:
    python generate_password.py

Luego ingresa el username y password cuando se te solicite.
El script generará el hash que debes copiar en .streamlit/secrets.toml
"""

import bcrypt

def generar_hash_password():
    """Genera un hash bcrypt para una contraseña"""
    print("\n" + "="*60)
    print("  GENERADOR DE PASSWORDS PARA GENERADOR DE RECIBOS")
    print("="*60 + "\n")

    username = input("Ingresa el username (ej: juan_perez): ").strip()
    nombre = input("Ingresa el nombre completo (ej: Juan Perez): ").strip()
    email = input("Ingresa el email (ej: juan@ejemplo.com): ").strip()
    password = input("Ingresa la contrasena: ").strip()

    if not username or not password or not nombre or not email:
        print("\nError: Todos los campos son obligatorios")
        return

    # Generar hash usando bcrypt directamente
    salt = bcrypt.gensalt()
    hashed_password = bcrypt.hashpw(password.encode('utf-8'), salt)
    hashed_password_str = hashed_password.decode('utf-8')

    print("\n" + "="*60)
    print("  HASH GENERADO EXITOSAMENTE")
    print("="*60 + "\n")

    print("Copia y pega lo siguiente en .streamlit/secrets.toml:\n")
    print("-"*60)
    print(f"""
[credentials.usernames.{username}]
email = "{email}"
name = "{nombre}"
password = "{hashed_password_str}"
""")
    print("-"*60)

    print("\nPara Streamlit Cloud:")
    print("1. Ve a tu app en share.streamlit.io")
    print("2. Settings > Secrets")
    print("3. Agrega el bloque de arriba en la seccion [credentials.usernames]")
    print("\n" + "="*60 + "\n")

if __name__ == "__main__":
    try:
        generar_hash_password()
    except KeyboardInterrupt:
        print("\n\nOperacion cancelada por el usuario")
    except Exception as e:
        print(f"\nError: {str(e)}")
