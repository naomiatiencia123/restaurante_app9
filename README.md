# restaurante_app

## Nombre del estudiante

**JAMIE NAOMI ATIENCIA VASQUEZ**

## Descripción del sistema

`restaurante_app` es un sistema de administración básica para un restaurante desarrollado en Python aplicando Programación Orientada a Objetos.

El sistema permite administrar productos y usuarios mediante un menú interactivo por consola. Se pueden registrar, buscar, actualizar, eliminar y listar productos, además de registrar y listar usuarios.

El proyecto utiliza una estructura modular para separar los modelos, los servicios y la interacción con el usuario.

## Estructura del proyecto

```text
restaurante_app/
│
├── modelos/
│   ├── __init__.py
│   ├── producto.py
│   └── usuario.py
│
├── servicios/
│   ├── __init__.py
│   └── restaurante.py
│
├── main.py
└── README.md
```

## Responsabilidad de los componentes

### modelos/producto.py

Contiene la clase `Producto`, que representa un producto del restaurante.

Sus principales datos son:

* Código
* Nombre
* Categoría
* Precio

### modelos/usuario.py

Contiene la clase `Usuario`, que representa una persona registrada en el sistema.

Sus principales datos son:

* Identificación
* Nombre
* Correo

### servicios/restaurante.py

Contiene la clase `Restaurante`, encargada de administrar las colecciones de productos y usuarios.

También contiene las operaciones para:

* Registrar productos
* Buscar productos
* Actualizar productos
* Eliminar productos
* Listar productos
* Registrar usuarios
* Listar usuarios
* Obtener categorías únicas

### main.py

Es el punto de entrada del programa.

Se encarga de:

* Mostrar el menú.
* Solicitar información mediante `input()`.
* Crear objetos `Producto` y `Usuario`.
* Utilizar los métodos de `Restaurante`.
* Mostrar los resultados al usuario.
* Validar entradas incorrectas.

## Estructuras de datos utilizadas

### Lista (`list`)

Se utilizan listas para almacenar las colecciones dinámicas de productos y usuarios.

En `Restaurante` se utilizan:

```python
self.productos: list[Producto] = []
self.usuarios: list[Usuario] = []
```

Estas listas permiten agregar, buscar, actualizar, eliminar y listar los objetos registrados.

### Tupla (`tuple`)

Se utiliza una tupla para almacenar las opciones disponibles del menú:

```python
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
```

La tupla representa información estable del menú que no necesita modificarse durante la ejecución del programa.

### Diccionario (`dict`)

Se utiliza un diccionario para relacionar cada opción del menú con la función que debe ejecutarse:

```python
ACCIONES_MENU = {
    "1": registr
```
