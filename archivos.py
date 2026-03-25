from servicios import *
import csv 
header = ["nombre", "precio", "cantidad"]
def guardar_csv(inventario, ruta, incluir_header=True):
    if not inventario:
        print("No hay productos para guardar.")
        return
    with open(ruta, mode='a', newline='', encoding='utf-8') as archivo:
        escritor_csv = csv.DictWriter(archivo, fieldnames=header)
        if incluir_header:
            escritor_csv.writeheader()
        for producto in inventario:
            escritor_csv.writerow(producto)
        print(f"Inventario guardado en: {ruta}")


def cargar_csv(ruta, inventario, sobrescribir=True):
    new_inventario = []
    filas_invalidas = 0

    def fila_valida(fila):
        claves = ["nombre", "precio", "cantidad"]

        # Validar estructura
        if not fila or not all(k in fila for k in claves):
            return False

        # Validar vacíos
        if not fila["nombre"] or not fila["precio"] or not fila["cantidad"]:
            return False

        # Validar tipos
        try:
            float(fila["precio"])
            int(fila["cantidad"])
        except ValueError:
            return False

        return True

    try:
        with open(ruta, mode='r', newline='', encoding='utf-8') as archivo:
            lector_csv = csv.DictReader(archivo)

            if not sobrescribir:
                print("Cargando inventario sin sobrescribir el actual.")

                for fila in lector_csv:
                    if not fila_valida(fila):
                        filas_invalidas += 1
                        continue

                    producto = {
                        "nombre": fila["nombre"],
                        "precio": float(fila["precio"]),
                        "cantidad": int(fila["cantidad"])
                    }

                    producto_encontrado = buscar_producto(inventario, producto["nombre"])

                    if producto_encontrado:
                        suma = producto_encontrado["cantidad"] + producto["cantidad"]
                        actualizar_producto(
                            inventario,
                            producto["nombre"],
                            producto_encontrado["precio"],
                            suma
                        )
                    else:
                        new_inventario.append(producto)

                inventario.extend(new_inventario)
                print("El usuario fusionó el inventario actual")

            else:
                inventario = []

                for fila in lector_csv:
                    if not fila_valida(fila):
                        filas_invalidas += 1
                        continue

                    producto = {
                        "nombre": fila["nombre"],
                        "precio": float(fila["precio"]),
                        "cantidad": int(fila["cantidad"])
                    }

                    inventario.append(producto)
                    new_inventario = inventario

                print("El usuario sobrescribió el inventario actual")

    except FileNotFoundError:
        print(f"No se encontró el archivo: {ruta}")
    except Exception as e:
        print(f"Error al cargar el archivo: {e}")

    print(f"Productos cargados: {new_inventario}")
    if filas_invalidas > 0:
        print(f"{filas_invalidas} filas inválidas omitidas")
    else:
        print("No hubo filas inválidas")

    return inventario
