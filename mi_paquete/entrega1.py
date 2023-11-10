# Función para almacenar la información de usuario y contraseña en un diccionario
def registrar_usuario(base_datos, usuario, contraseña, nombre, apellido, correo, direccion):
    base_datos[usuario] = {"contraseña": contraseña, "nombre": nombre, "apellido": apellido, "correo": correo, "direccion": direccion}
    print(f"Usuario {usuario} registrado con éxito.")

# Función para iniciar sesión
def iniciar_sesion(base_datos, usuario, contraseña):
    if usuario in base_datos and base_datos[usuario]["contraseña"] == contraseña:
        print(f"Bienvenido, {usuario}!")
    else:
        print("Inicio de sesión fallido. Verifica tu usuario y contraseña.")

# Función para mostrar todos los usuarios registrados
def mostrar_usuarios(base_datos):
    print("Usuarios registrados:")
    for usuario, datos in base_datos.items():
        print(f"Usuario: {usuario}, Contraseña: {datos['contraseña']}, Nombre: {datos['nombre']}, Apellido: {datos['apellido']}, Correo: {datos['correo']}, Dirección: {datos['direccion']}")

# Base de datos de usuarios (diccionario)
base_de_datos_usuarios = {}

while True:
    print("\nMenú:")
    print("1. Registrar Usuario")
    print("2. Iniciar Sesión")
    print("3. Mostrar Usuarios Registrados")
    print("4. Salir")

    opcion = input("Ingrese el número de opción: ")

    if opcion == "1":
        usuario = input("Ingrese el nombre de usuario: ")
        contraseña = input("Ingrese la contraseña: ")
        nombre = input("Ingrese su nombre: ")
        apellido = input("Ingrese su apellido: ")
        correo = input("Ingrese su correo: ")
        direccion = input("Ingrese su dirección: ")
        registrar_usuario(base_de_datos_usuarios, usuario, contraseña, nombre, apellido, correo, direccion)

    elif opcion == "2":
        usuario = input("Ingrese el nombre de usuario: ")
        contraseña = input("Ingrese la contraseña: ")
        iniciar_sesion(base_de_datos_usuarios, usuario, contraseña)

    elif opcion == "3":
        mostrar_usuarios(base_de_datos_usuarios)

    elif opcion == "4":
        print("¡Hasta luego!")
        break

    else:
        print("Opción no válida. Por favor, elija una opción válida.")
        print("Opción no válida. Por favor, elija una opción válida.")