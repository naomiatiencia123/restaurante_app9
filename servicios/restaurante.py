from modelos.producto import Producto
from modelos.usuario import Usuario


class Restaurante:
    def __init__(self) -> None:
        self.productos: list[Producto] = []
        self.usuarios: list[Usuario] = []

    # ==============================
    # PRODUCTOS
    # ==============================

    def registrar_producto(self, producto: Producto) -> bool:
        for producto_existente in self.productos:
            if producto_existente.codigo == producto.codigo:
                return False

        self.productos.append(producto)
        return True

    def buscar_producto(self, codigo: str) -> Producto | None:
        for producto in self.productos:
            if producto.codigo == codigo:
                return producto

        return None

    def actualizar_producto(
        self,
        codigo: str,
        nombre: str,
        categoria: str,
        precio: float
    ) -> bool:

        producto = self.buscar_producto(codigo)

        if producto is None:
            return False

        producto.nombre = nombre
        producto.categoria = categoria
        producto.precio = precio

        return True

    def eliminar_producto(self, codigo: str) -> bool:
        producto = self.buscar_producto(codigo)

        if producto is None:
            return False

        self.productos.remove(producto)
        return True

    def listar_productos(self) -> list[Producto]:
        return self.productos

    # ==============================
    # USUARIOS
    # ==============================

    def registrar_usuario(self, usuario: Usuario) -> bool:
        for usuario_existente in self.usuarios:
            if usuario_existente.identificacion == usuario.identificacion:
                return False

        self.usuarios.append(usuario)
        return True

    def listar_usuarios(self) -> list[Usuario]:
        return self.usuarios

    # ==============================
    # CATEGORÍAS
    # ==============================

    def obtener_categorias(self) -> set[str]:
        categorias = set()

        for producto in self.productos:
            categorias.add(producto.categoria)

        return categorias