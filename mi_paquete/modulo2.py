import importlib

try:
    entrega1 = importlib.import_module("entrega1")

    class Cliente:
        def __init__(self):
            self.nombre = entrega1.nombre
            self.apellido = entrega1.apellido
            self.correo = entrega1.correo
            self.direccion = entrega1.direccion

        def hacer_compra(self, producto):
            print(f"{self.nombre} ha comprado {producto}")

        def mostrar_info(self):
            print(f"Nombre: {self.nombre} {self.apellido}")
            print(f"Correo: {self.correo}")
            print(f"Dirección: {self.direccion}")

        def __str__(self):
            return f"{self.nombre} {self.apellido}"

    class ClientePremium(Cliente):
        def __init__(self):
            super().__init__()
            self.puntos = entrega1.puntos

        def obtener_descuento(self, descuento):
            print(f"{self.nombre} ha obtenido un descuento del {descuento}%")

        def mostrar_info(self):
            super().mostrar_info()
            print(f"Puntos de Cliente Premium: {self.puntos}")

    # Ejemplo de uso
    cliente1 = Cliente()
    cliente1.hacer_compra("Producto A")
    cliente1.mostrar_info()

    cliente2 = ClientePremium()
    cliente2.hacer_compra("Producto B")
    cliente2.mostrar_info()
    cliente2.obtener_descuento(10)

    # Imprimimos el nombre de los clientes utilizando __str__()
    print(f"\nNombre del cliente 1: {cliente1}")
    print(f"Nombre del cliente 2: {cliente2}")

except ModuleNotFoundError:
    print("No se encontró el archivo 'entrega1.py'. Asegúrate de que el archivo existe en la misma carpeta.")
