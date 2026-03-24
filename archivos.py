from servicios import *
import csv 
header = ["nombre", "precio", "cantidad"]
def guardar_csv(inventario, ruta, incluir_header=True):
    if not inventario:
        print("No hay productos para guardar.")
        return
    with open(ruta, mode='a', newline='') as archivo:
        escritor_csv = csv.DictWriter(archivo, fieldnames=header)
        if incluir_header:
            escritor_csv.writeheader()
        for producto in inventario:
            escritor_csv.writerow(producto)
        print(f"Inventario guardado en: {ruta}")

def cargar_csv(ruta,inventario, sobrescribir=True):
    new_inventario = []
    if not sobrescribir:
        print("Cargando inventario sin sobrescribir el actual.")
        with open(ruta, mode='r', newline='') as archivo:
                lector_csv = csv.DictReader(archivo)
                for fila in lector_csv:
                    producto = {
                        "nombre": fila["nombre"],
                        "precio": float(fila["precio"]),
                        "cantidad": int(fila["cantidad"])
                    }
                    if buscar_producto(inventario, producto["nombre"]):                
                        producto_encontrado = buscar_producto(inventario, producto["nombre"])   
                        suma = producto_encontrado["cantidad"] + producto["cantidad"]
                        actualizar_producto(inventario, producto["nombre"], producto_encontrado["precio"], suma)
                    else:
                        new_inventario.append(producto)
        print("el usuario fusionó el inventario actual")
        return inventario
    else:
        inventario = []
        try:
            with open(ruta, mode='r', newline='') as archivo:
                lector_csv = csv.DictReader(archivo)
                for fila in lector_csv:
                    producto = {
                        "nombre": fila["nombre"],
                        "precio": float(fila["precio"]),
                        "cantidad": int(fila["cantidad"])
                    }
                    inventario.append(producto)
                    new_inventario=inventario
        except FileNotFoundError:
            print(f"No se encontró el archivo: {ruta}")
        except Exception as e:
             print(f"Error al cargar el archivo: {e}")
        
        print("el usuario sobrescribió el inventario actual")
       
   
    print(f"Productos cargados: {new_inventario}") 
    return inventario
