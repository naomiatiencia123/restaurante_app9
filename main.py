from modelos.producto import Producto
from modelos.usuario import Usuario
from servicios.restaurante import Restaurante


restaurante = Restaurante()


# ==========================================
# FUNCIONES PARA PRODUCTOS
# ==========================================

def registrar_producto() -> None:
    print("\n--- REGISTRAR PRODUCTO ---")

    codigo = input("Código: ").strip()
    nombre = input("Nombre: ").strip()
    categoria = input("Categoría: ").strip()

    try:
        precio = float(input("Precio: "))

        if precio < 0:
            print("El precio no puede ser negativo.")
            return

    except ValueError:
        print("El precio debe ser un número.")
        return

    producto = Producto(codigo, nombre, categoria, precio)

    if restaurante.registrar_producto(producto):
        print("Producto registrado correctamente.")
    else:
        print("Ya existe un producto con ese código.")


def buscar_producto() -> None:
    print("\n--- BUSCAR PRODUCTO ---")

    codigo = input("Ingrese el código del producto: ").strip()

    producto = restaurante.buscar_producto(codigo)

    if producto is None:
        print("Producto no encontrado.")
    else:
        print("\nProducto encontrado:")
        print(producto)


def actualizar_producto() -> None:
    print("\n--- ACTUALIZAR PRODUCTO ---")

    codigo = input("Ingrese el código del producto: ").strip()

    producto = restaurante.buscar_producto(codigo)

    if producto is None:
        print("Producto no encontrado.")
        return

    print("Ingrese los nuevos datos:")

    nombre = input("Nuevo nombre: ").strip()
    categoria = input("Nueva categoría: ").strip()

    try:
        precio = float(input("Nuevo precio: "))

        if precio < 0:
            print("El precio no puede ser negativo.")
            return

    except ValueError:
        print("El precio debe ser un número.")
        return

    actualizado = restaurante.actualizar_producto(
        codigo,
        nombre,
        categoria,
        precio
    )

    if actualizado:
        print("Producto actualizado correctamente.")
    else:
        print("No se pudo actualizar el producto.")


def eliminar_producto() -> None:
    print("\n--- ELIMINAR PRODUCTO ---")

    codigo = input("Ingrese el código del producto: ").strip()

    if restaurante.eliminar_producto(codigo):
        print("Producto eliminado correctamente.")
    else:
        print("Producto no encontrado.")


def listar_productos() -> None:
    print("\n--- LISTA DE PRODUCTOS ---")

    productos = restaurante.listar_productos()

    if not productos:
        print("No existen productos registrados.")
        return

    for producto in productos:
        print(producto)


# ==========================================
# FUNCIONES PARA USUARIOS
# ==========================================

def registrar_usuario() -> None:
    print("\n--- REGISTRAR USUARIO ---")

    identificacion = input("Identificación: ").strip()
    nombre = input("Nombre: ").strip()
    correo = input("Correo: ").strip()

    usuario = Usuario(
        identificacion,
        nombre,
        correo
    )

    if restaurante.registrar_usuario(usuario):
        print("Usuario registrado correctamente.")
    else:
        print("Ya existe un usuario con esa identificación.")


def listar_usuarios() -> None:
    print("\n--- LISTA DE USUARIOS ---")

    usuarios = restaurante.listar_usuarios()

    if not usuarios:
        print("No existen usuarios registrados.")
        return

    for usuario in usuarios:
        print(usuario)


# ==========================================
# FUNCIÓN PARA CATEGORÍAS
# ==========================================

def mostrar_categorias() -> None:
    print("\n--- CATEGORÍAS ---")

    categorias = restaurante.obtener_categorias()

    if not categorias:
        print("No existen categorías registradas.")
        return

    for categoria in sorted(categorias):
        print(f"- {categoria}")


# ==========================================
# MENÚ PRINCIPAL
# ==========================================

def mostrar_menu() -> None:
    print("\n========================================")
    print("        SISTEMA DE RESTAURANTE")
    print("========================================")
    print("1. Registrar producto")
    print("2. Buscar producto")
    print("3. Actualizar producto")
    print("4. Eliminar producto")
    print("5. Listar productos")
    print("----------------------------------------")
    print("6. Registrar usuario")
    print("7. Listar usuarios")
    print("----------------------------------------")
    print("8. Mostrar categorías")
    print("9. Salir")
    print("========================================")


# Tupla: contiene las opciones estables del menú.
OPCIONES_MENU = (
    "1",
    "2",
    "3",
    "4",
    "5",
    "6",
    "7",
    "8",
    "9"
)


# Diccionario: relaciona cada opción con la función correspondiente.
ACCIONES_MENU = {
    "1": registrar_producto,
    "2": buscar_producto,
    "3": actualizar_producto,
    "4": eliminar_producto,
    "5": listar_productos,
    "6": registrar_usuario,
    "7": listar_usuarios,
    "8": mostrar_categorias
}


# ==========================================
# PROGRAMA PRINCIPAL
# ==========================================

def ejecutar_programa() -> None:
    while True:
        mostrar_menu()

        opcion = input("Seleccione una opción: ").strip()

        if opcion not in OPCIONES_MENU:
            print("Opción inválida. Seleccione una opción del 1 al 9.")
            continue

        if opcion == "9":
            print("Gracias por utilizar el sistema.")
            break

        accion = ACCIONES_MENU[opcion]
        accion()


if __name__ == "__main__":
    ejecutar_programa()