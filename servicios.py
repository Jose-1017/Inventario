def agregar_producto():
    """
    Solicita al usuario el nombre y el precio de un producto.

    Valida que el precio sea un numero mayor que cero,
    repitiendo la solicitud hasta obtener un valor valido.

    Retorna:
        tuple: (nombre_producto: str, precio: float)
    """
    # validar nombre    
    nombre_producto = input("\nIngrese el nombre del producto: ")

    # validar precio 
    precio=0
    while precio <= 0:
         try:
              precio = float(input("\nIngrese el precio del producto: "))
              if precio <= 0:
                   print("Error: el precio debe ser mayor que 0.")
         except ValueError:
              print("Error: debe ingresar un numero valido.")

    return nombre_producto, precio


def pedir_cantidad():
    """
    Solicita al usuario una cantidad entera mayor que cero.

    Repite la solicitud si el valor ingresado es invalido
    o menor o igual a cero.

    Retorna:
        int: cantidad ingresada por el usuario
    """
    # Validar cantidad 
    try:
        cantidad = int(input("\nIngrese la cantidad: "))
        while cantidad <= 0:
            print("Debe ingresar un numero valido.")
            cantidad = int(input("\nIngrese la cantidad: "))
    except ValueError:
        print("Error: debe ingresar un numero valido.")
    return cantidad

def mostrar_inventario(inventario):
    """
    Muestra en consola todos los productos del inventario.

    Si el inventario esta vacio, informa al usuario.
    Cada producto se muestra con su nombre, precio y cantidad.

    Parametros:
        inventario (list[dict]): lista de productos con claves
                                 'nombre', 'precio' y 'cantidad'

    Retorna:
        None
    """
    if not inventario:
        print("\nEl inventario esta vacio.")
    else:
        print("\n--- Inventario ---")
        for datos in inventario:
            print(f"Nombre: {datos['nombre']} | Precio: ${datos['precio']} | Cantidad: {datos['cantidad']}")

def calcular_estadisticas(inventario):
    """
    Calcula y muestra estadisticas generales del inventario.

    Calcula:
        - valor_total: suma de (precio * cantidad) de cada producto
        - unidades_totales: suma de todas las cantidades
        - producto_mas_caro: producto con el mayor precio unitario
        - producto_mayor_stock: producto con la mayor cantidad

    Si el inventario esta vacio, informa al usuario y retorna None.

    Parametros:
        inventario (list[dict]): lista de productos con claves
                                 'nombre', 'precio' y 'cantidad'

    Retorna:
        dict: {
            'valor_total' 
            'unidades_totales'
            'producto_mas_caro'
            'producto_mayor_stock'
        }
        None: si el inventario esta vacio
    """
    if not inventario:
        print("\nNo hay estadisticas que calcular.")
        return

    total_inventario = 0
    cantidad_total = 0

    for producto in inventario:
        total_inventario += producto['precio'] * producto['cantidad']
        cantidad_total += producto['cantidad']

    max_cantidad = max(inventario, key = lambda p: p['cantidad'])
    max_precio = max(inventario, key = lambda p: p['precio'])
    
    print("prueba")

    print("\n--- Estadisticas ---")
    print(f"Valor total del inventario: ${total_inventario:.2f}")
    print(f"Cantidad total de productos: {cantidad_total}")
    print(f"{max_cantidad['nombre']} {max_cantidad['cantidad']} y  {max_precio['nombre']} {max_precio['precio']}")

    return total_inventario, cantidad_total, max_cantidad, max_precio


def buscar_producto(inventario,nombre_producto):  
    """
    Busca un producto por nombre en el inventario.

    Parametros:
        inventario (list): lista de productos
        nombre (str): nombre del producto a buscar

    Retorna:
        dict | None: producto encontrado o None si no existe
    """
    for producto in inventario:         
        if producto['nombre'] == nombre_producto:
            print("El producto existe")           
            return  producto
    return None
    
def actualizar_producto(inventario, nombre_producto, nuevo_precio, nueva_cantidad):
    """
    Actualiza el precio y la cantidad de un producto existente.

    Busca el producto por nombre. Si no existe, informa al usuario.
    Si existe, reemplaza su precio y cantidad con los nuevos valores
    y muestra el producto actualizado.

    Parametros:
        inventario (list[dict]): lista de productos con claves
                                 'nombre', 'precio' y 'cantidad'
        nombre_producto (str): nombre del producto a actualizar
        nuevo_precio (float): nuevo precio unitario del producto
        nueva_cantidad (int): nueva cantidad en inventario

    Retorna:
        None
    """
    producto_encontrado = buscar_producto(inventario, nombre_producto)
    if producto_encontrado is None:
        print("Producto no existe")
    else:
        producto_encontrado['precio'] = nuevo_precio
        producto_encontrado['cantidad'] = nueva_cantidad
        print(f"producto actualizado {producto_encontrado}")

def eliminar_producto(inventario, nombre_producto):
    """
    Elimina un producto del inventario por su nombre.

    Busca el producto y lo elimina de la lista si existe.
    Si no se encuentra, informa al usuario con un mensaje.

    Parametros:
        inventario (list[dict]): lista de productos con claves
                                 'nombre', 'precio' y 'cantidad'
        nombre_producto (str): nombre del producto a eliminar

    Retorna:
        None
    """
    producto_encontrado = buscar_producto(inventario, nombre_producto)
    if producto_encontrado is None:
        print("Producto no existe")
    else:
        inventario.remove(producto_encontrado)
        print('Producto eliminado')

