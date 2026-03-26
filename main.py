from servicios import *
from archivos import * 
import os 



# PROGRAMA PRINCIPAL
nombre = input("\nIngrese su nombre: ")
opcion = total= recibo = 0
detalle = "" 
inventario = []

while opcion != 9: 

    print("\n1 - Agregar producto")
    print("2 - Mostrar inventario")
    print("3 - Calcular estadistica")
    print("4 - Buscar producto")
    print("5 - Actualizar producto")
    print("6 - Eliminar producto")
    print("7 - Guardar CSV")
    print("8 - Cargar CSV")
    print("9 - Salir")

    try:
        opcion = int(input("\nSeleccione una opcion: "))
    except ValueError:
        print("Debe ingresar un numero valido.")
        continue

    if opcion==1:
          nombre_producto, precio = agregar_producto()
          cantidad = pedir_cantidad()     
          # Guardar multiples productos
          producto_existente = buscar_producto(inventario, nombre_producto)

          if producto_existente:
            # Si ya existe, sumamos cantidad
            producto_existente["cantidad"] += cantidad
            producto_existente["precio"] = precio  
            print("Producto actualizado (se sumo la cantidad)")
          else:
            # Si no existe, lo agregamos
            inventario.append({
                  "nombre": nombre_producto,
                  "precio": precio,
                  "cantidad": cantidad
            })
            print("Producto agregado correctamente")
        
    elif opcion == 2:
            mostrar_inventario(inventario)

    elif opcion == 3:
            calcular_estadisticas(inventario)
    elif opcion == 4:
          nombre_producto = input("Escriba nombre del producto:  ")
          buscar_producto(inventario, nombre_producto)

    elif opcion == 5:
          nombre_producto = input("Escriba nombre del producto:  ")
          nuevo_precio = float(input("ingrese nuevo precio:  "))
          nueva_cantidad = int(input("Ingrese nueva cantidad:  "))
          actualizar_producto(inventario, nombre_producto, nuevo_precio, nueva_cantidad)

    elif opcion == 6: 
           nombre_producto = input("Escriba nombre del producto:  ")
           eliminar_producto(inventario, nombre_producto)
    elif opcion == 7:
             ruta_name = input("Ingresa el nombre del archivo CSV: ")
             ruta = os.path.join(os.path.dirname(__file__), ruta_name)
             guardar_csv(inventario, ruta)
             
    elif opcion == 8:
            ruta_name = input("Ingresa el nombre del archivo CSV: ")
            ruta = os.path.join(os.path.dirname(__file__), ruta_name)
            cargar = input("¿Desea cargar el inventario desde el CSV? Esto sobrescribirá el inventario actual. (s/n): ").lower()
            if cargar == 's':
                  inventario = cargar_csv(ruta, inventario, True)
            else:
                  cargar_csv(ruta, inventario, False)
    elif opcion == 9:
            break
    else:
         print("Opción incorrecta")

for i in inventario:
      total = i ["precio"] * i["cantidad"]
      detalle += (f"{i['nombre']} x {i['cantidad']} = ${total}\n")
      recibo += total


# RECIBO FINAL
print("\n========= RECIBO DE COMPRA =========")
print(f"Cliente: {nombre}\n")
print(detalle)
print(f"TOTAL A PAGAR:   ${recibo:.2f}")
print("\n¡Gracias por su compra!")

