from servicios import *
import csv 
header = ["nombre", "precio", "cantidad"]
def guardar_csv(inventario, ruta, incluir_header=True):
    """
    Guarda el inventario en un archivo CSV.

    Parametros:
        inventario (list): lista de productos
        ruta (str): ruta del archivo
        incluir_header (bool): indica si se escribe encabezado

    Retorna:
        None
    """
    if not inventario:
        print("No hay productos para guardar.")
        return
    with open(ruta, mode='w', newline='', encoding='utf-8') as archivo:
        escritor_csv = csv.DictWriter(archivo, fieldnames=header)
        if incluir_header:
            escritor_csv.writeheader()
        for producto in inventario:
            escritor_csv.writerow(producto)
        print(f"Inventario guardado en: {ruta}")


def cargar_csv(ruta, inventario, sobrescribir=True):
    """
    Carga productos desde un archivo CSV hacia el inventario.

    Valida que el archivo tenga extension .csv y encabezado correcto
    (nombre,precio,cantidad). Las filas invalidas se omiten y se
    acumula un contador de errores que se informa al final.

    Modos de carga:
        - sobrescribir=True: reemplaza el inventario actual por el
          contenido del CSV.
        - sobrescribir=False: fusiona el CSV con el inventario actual.
          Si un producto ya existe, suma su cantidad y conserva el
          precio actual. Si no existe, lo agrega.

    Maneja los errores:
        FileNotFoundError, UnicodeDecodeError, ValueError y
        excepciones genericas, informando al usuario sin cerrar
        el programa.

    Parametros:
        ruta (str): ruta completa del archivo CSV a leer
        inventario (list[dict]): lista actual de productos con claves
                                 'nombre', 'precio' y 'cantidad'
        sobrescribir (bool): determina el modo de carga (por defecto True)

    Retorna:
        list[dict]: inventario resultante tras la carga
    """

    # Validar que sea archivo CSV usando split
    if ruta.split(".")[-1].lower() != "csv":
        print("Error: El archivo debe ser CSV")
        return inventario
    
    new_inventario = []
    filas_invalidas = 0

    def fila_valida(fila):
        """
        Valida que una fila del CSV tenga estructura y datos correctos.

        Verifica que la fila no esta vacia, que contenga las claves
        'nombre', 'precio' y 'cantidad', que ningun valor sea vacio,
        que precio sea convertible a float y cantidad a int, y que
        ambos sean valores no negativos.

        Parametros:
            fila (dict): fila leida por csv.DictReader

        Retorna:
            bool: True si la fila es valida, False en caso contrario
        """
        
        claves = ["nombre", "precio", "cantidad"]

        # Validar estructura
        if not fila:
            return False
        for clave in claves:
            if clave not in fila:
                return False
            
        # Validar vacios
        if not fila["nombre"] or not fila["precio"] or not fila["cantidad"]:
            return False
        
        # Validar tipos y negativos
        try:
            precio = float(fila["precio"])
            cantidad = int(fila["cantidad"])

            if precio < 0 or cantidad < 0:
                return False

        except ValueError:
            return False

        return True

    try:
        with open(ruta, mode='r', newline='', encoding='utf-8') as archivo:
            lector_csv = csv.DictReader(archivo)
            # Validar encabezado
            if lector_csv.fieldnames != ["nombre", "precio", "cantidad"]:
                print("Error: encabezado invalido. Debe ser: nombre,precio,cantidad")
                return inventario

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
                        # sumar precios y cantidades
                        suma = producto_encontrado["cantidad"] + producto["cantidad"]
                        actualizar_producto(inventario, producto["nombre"], producto_encontrado["precio"], suma)
                    else:
                        new_inventario.append(producto)

                inventario.extend(new_inventario)
                print("El usuario fusiono el inventario actual")

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

                print("El usuario sobrescribio el inventario actual")

    except FileNotFoundError:
        print(f"No se encontro el archivo: {ruta}")

    except UnicodeDecodeError:
        print("Error: problema de codificacion del archivo")

    except ValueError:
        print("Error: datos invalidos en el archivo")

    except Exception as e:
        print(f"Error inesperado: {e}")

    print(f"Productos cargados: {new_inventario}")

    if filas_invalidas > 0:
        print(f"{filas_invalidas} filas invalidas omitidas")
    else:
        print("No hubo filas invalidas")

    return inventario
