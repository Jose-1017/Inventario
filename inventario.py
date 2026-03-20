def pedir_producto():
    # validar nombre    
    while True:
        nombre_producto = input("\nIngrese el nombre del producto: ")
        if nombre_producto.isalpha():
            break
        else:
            print("Error: el nombre debe contener solo letras.")

    # validar precio    
    while True:
        try:
            precio = float(input("\nIngrese el precio del producto: "))
            if precio > 0:
                break
            else:
                print("El precio debe ser mayor que 0.")
        except ValueError:
            print("Error: debe ingresar un número válido.")

    return nombre_producto, precio


def pedir_cantidad():
    # Validar cantidad 
    while True:
        try:
            cantidad = int(input("\nIngrese la cantidad: "))
            if cantidad > 0:
                return cantidad
            else:
                print("La cantidad debe ser mayor que 0.")
        except ValueError:
            print("Debe ingresar un número válido.")


def mostrar_estado(detalle, total):
    print("\n--- Estado actual de la compra ---")
    print(detalle)
    print(f"Subtotal acumulado: ${total:.2f}")


# PROGRAMA PRINCIPAL
nombre = input("\nIngrese su nombre: ")
total = 0
opcion = 0
detalle = "" 
inventario = {}

while opcion != 4: 

    print("\n1 - Agregar producto")
    print("2 - Mostrar inventario")
    print("3 - Calcular estadistica")
    print("4 - Salir")

    try:
        opcion = int(input("\nSeleccione una opción: "))
    except ValueError:
        print("Debe ingresar un número válido.")
        continue

    match opcion:
        case 1:
            nombre_producto, precio = pedir_producto()
            cantidad = pedir_cantidad()          
            costo_total = precio * cantidad
            total += costo_total

            detalle += f"{nombre_producto} x{cantidad} = ${costo_total:.2f}\n"

            # Guardar múltiples productos
            inventario[nombre_producto] = {
                "precio": precio,
                "cantidad": cantidad
            }

        case 2:
            if not inventario:
                print("\nEl inventario está vacío.")
            else:
                print("\n--- Inventario ---")
                for producto, datos in inventario.items():
                    print(f"{producto} -> Precio: ${datos['precio']}, Cantidad: {datos['cantidad']}")

        case 3:
            mostrar_estado(detalle, total)

        case 4:
            break

        case _:
            print("Opción incorrecta")


# RECIBO FINAL
mostrar_estado(detalle, total)
print("\n========= RECIBO DE COMPRA =========")
print(f"Cliente: {nombre}\n")
print(detalle)
print(f"TOTAL A PAGAR:   ${total:.2f}")
print("\n¡Gracias por su compra!")
# El codigo simula la compra de X producto donde el usuario puede ingresar su nombre, nombre del producto y valor.
# Automaticamente el sistema calculara su costo total teniendo en cuenta el valor ingresado x la cantidad de productos.
# El codigo se compone por 3 funciones y 1 codigo principal.
# Los nombres de las funciones son: pedir_producto (), pedir_cantidad() y mostrar_estado()
# En la funcion pedir_producto() se encarga de solicitar el nombre y precio del producto.
# En la funcion pedir_cantidad() se encarga de solicitar la cantidad que desea llevar de dicho producto.
# En la funcion mostrar_estado() se encarga de mostrar al usuario los productos ingresados, su valor unitario y total.
# En el código principal solicitamos el nombre del usuario.
# Luego se muestra un menú donde puede agregar productos o salir.
# Cada vez que agrega un producto se calcula su costo según el precio y la cantidad.
# El sistema acumula el total y guarda el detalle de los productos ingresados.
# Después de cada producto se muestra el estado actual de la compra.
# Al finalizar, se imprime el recibo con el total a pagar. 
