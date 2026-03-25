def agregar_producto():
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
              print("Error: debe ingresar un número válido.")

    return nombre_producto, precio


def pedir_cantidad():
    # Validar cantidad 
    cantidad = int(input("\nIngrese la cantidad: "))
    while cantidad<=0:                     
        print("Debe ingresar un número válido.")
        cantidad = int(input("\nIngrese la cantidad: "))
    return cantidad

def mostrar_inventario(inventario):
    if not inventario:
        print("\nEl inventario está vacío.")
    else:
        print("\n--- Inventario ---")
        for datos in inventario:
            print(f"Nombre: {datos['nombre']} | Precio: ${datos['precio']} | Cantidad: {datos['cantidad']}")

def calcular_estadisticas(inventario):
    if not inventario:
        print("\nNo hay estadísticas que calcular.")
        return

    total_inventario = 0
    cantidad_total = 0

    for producto in inventario:
        total_inventario += producto['precio'] * producto['cantidad']
        cantidad_total += producto['cantidad']

    max_cantidad = max(inventario, key = lambda p: p['cantidad'])
    max_precio = max(inventario, key = lambda p: p['precio'])
    
    print("prueba")

    print("\n--- Estadísticas ---")
    print(f"Valor total del inventario: ${total_inventario:.2f}")
    print(f"Cantidad total de productos: {cantidad_total}")
    print(f"{max_cantidad['nombre']} {max_cantidad['cantidad']} y  {max_precio['nombre']} {max_precio['precio']}")


def buscar_producto(inventario,nombre_producto):  
    for producto in inventario:         
        if producto['nombre'] == nombre_producto:
            print("El producto existe")           
            return  producto
    return None
    
def actualizar_producto(inventario, nombre_producto, nuevo_precio, nueva_cantidad):
    producto_encontrado = buscar_producto(inventario, nombre_producto)
    if producto_encontrado is None:
        print("Producto no existe")
    else:
        producto_encontrado['precio'] = nuevo_precio
        producto_encontrado['cantidad'] = nueva_cantidad
        print(f"producto actualizado {producto_encontrado}")

def eliminar_producto(inventario, nombre_producto):
    producto_encontrado = buscar_producto(inventario, nombre_producto)
    if producto_encontrado is None:
        print("Producto no existe")
    else:
        inventario.remove(producto_encontrado)
        print('Producto eliminado')

