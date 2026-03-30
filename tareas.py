import json
import os

# ─────────────────────────────────────────────
# FUNCIONES DE GESTIÓN DE TAREAS
# ─────────────────────────────────────────────

def agregar_tarea(tareas):
    titulo = input("Ingrese el nombre de la tarea: ").strip().lower()
    # MEJORA: .strip() elimina espacios al inicio y al final antes de validar
    # Sin esto, " comprar leche" y "comprar leche" serían tareas distintas

    if not titulo:
        # CONSIDERACIÓN FALTANTE: validar que el título no esté vacío
        print("El título no puede estar vacío.")
        return

    for tarea in tareas:
        if tarea["titulo"] == titulo:
            print("La tarea ya existe.")
            return

    descripcion = input("Ingrese la descripción: ").strip().lower()
    # MEJORA: también aplicar .strip() a la descripción por consistencia

    tareas.append({
        "titulo": titulo,
        "descripcion": descripcion,
        "completada": False
    })
    print("Tarea agregada correctamente.")


def completar_tarea(tareas, titulo_tarea):
    # MEJORA: normalizar la entrada antes de comparar, igual que al agregar
    titulo_tarea = titulo_tarea.strip().lower()

    for tarea in tareas:
        if tarea['titulo'] == titulo_tarea:
            if not tarea['completada']:
                tarea['completada'] = True
                print("Tarea completada")
            else:
                print("La tarea ya está completada")
            return
    print("Tarea no encontrada")


def eliminar_tarea(tareas, titulo_tarea):
    # MEJORA: normalizar la entrada antes de comparar
    titulo_tarea = titulo_tarea.strip().lower()

    for tarea in tareas:
        if tarea['titulo'] == titulo_tarea:
            # CONSIDERACIÓN FALTANTE: pedir confirmación antes de eliminar
            # para evitar borrados accidentales
            confirmacion = input(f"¿Está seguro que desea eliminar '{titulo_tarea}'? (s/n): ").strip().lower()
            if confirmacion == 's':
                tareas.remove(tarea)
                print("Tarea eliminada.")
            else:
                print("Eliminación cancelada.")
            return
    print("Tarea no encontrada")


def listar_tareas(tareas):
    # CONSIDERACIÓN FALTANTE: extraer la lógica de mostrar tareas a su propia
    # función. Tener lógica importante dentro del while dificulta reutilizarla
    # y hace el menú más difícil de leer.
    print("\n--- Lista de Tareas ---")
    if not tareas:
        print("No hay tareas agregadas.")
        return

    # MEJORA: mostrar un índice numerado para identificar tareas fácilmente
    for i, tarea in enumerate(tareas, start=1):
        estado = "✔ Completada" if tarea['completada'] else "✘ Pendiente"
        print(f"{i}. [{estado}] {tarea['titulo'].capitalize()} — {tarea['descripcion'].capitalize()}")

    # MEJORA: mostrar un resumen al final
    completadas = sum(1 for t in tareas if t['completada'])
    print(f"\nTotal: {len(tareas)} tarea(s) | Completadas: {completadas} | Pendientes: {len(tareas) - completadas}")


def guardar_tareas(tareas, ruta):
    # CONSIDERACIÓN FALTANTE: verificar que haya tareas antes de guardar
    if not tareas:
        print("No hay tareas para guardar.")
        return

    try:
        # CONSIDERACIÓN FALTANTE: manejar errores de escritura con try/except
        # El archivo puede no ser escribible por permisos o disco lleno
        with open(ruta, 'w', encoding='utf-8') as archivo:
            json.dump(tareas, archivo, indent=4, ensure_ascii=False)
        print(f"Tareas guardadas correctamente en '{ruta}'.")
    except IOError as e:
        print(f"Error al guardar el archivo: {e}")


def cargar_tareas(ruta):
    try:
        with open(ruta, 'r', encoding='utf-8') as archivo:
            datos = json.load(archivo)

            # CONSIDERACIÓN FALTANTE: validar que el archivo JSON tenga el
            # formato esperado (lista de diccionarios con las claves correctas)
            # Un archivo corrupto o incorrecto puede romper todo el programa
            if not isinstance(datos, list):
                print("El archivo no tiene el formato esperado (debe ser una lista).")
                return []

            claves_requeridas = {"titulo", "descripcion", "completada"}
            for item in datos:
                if not isinstance(item, dict) or not claves_requeridas.issubset(item.keys()):
                    print("Una o más tareas en el archivo tienen un formato inválido.")
                    return []

            print(f"Se cargaron {len(datos)} tarea(s) correctamente.")
            return datos

    except FileNotFoundError:
        print("Archivo no encontrado.")
        return []
    except json.JSONDecodeError:
        # CONSIDERACIÓN FALTANTE: manejar archivos JSON con formato inválido
        # Si el archivo está corrupto, json.load() lanza esta excepción
        print("El archivo no tiene un formato JSON válido.")
        return []


def obtener_ruta(mensaje):
    # CONSIDERACIÓN FALTANTE: centralizar la construcción de rutas en una
    # función para no repetir la misma lógica en las opciones 5 y 6
    ruta_name = input(mensaje).strip()
    if not ruta_name.endswith('.json'):
        # MEJORA: agregar extensión automáticamente si el usuario la omite
        ruta_name += '.json'
    return os.path.join(os.path.dirname(__file__), ruta_name)


# ─────────────────────────────────────────────
# PROGRAMA PRINCIPAL
# ─────────────────────────────────────────────

def main():
    # CONSIDERACIÓN FALTANTE: envolver el programa en una función main()
    # Es una buena práctica en Python: separa el código ejecutable de las
    # definiciones y permite importar este módulo desde otros archivos
    # sin que el menú se ejecute automáticamente.

    tareas = []

    while True:
        # MEJORA: usar 'while True' con 'break' es más claro que manejar
        # el valor de 'opcion' como condición de salida
        print("\n--- Menú de Tareas ---")
        print("1. Agregar tarea")
        print("2. Mostrar tareas")
        print("3. Completar tarea")
        print("4. Eliminar tarea")
        print("5. Guardar tareas en archivo")
        print("6. Cargar tareas desde archivo")
        print("7. Salir")

        try:
            opcion = int(input("Seleccione una opción: "))
        except ValueError:
            print("Debe ingresar un número del 1 al 7.")
            continue

        # CONSIDERACIÓN FALTANTE: validar que la opción esté dentro del rango
        if opcion < 1 or opcion > 7:
            print("Opción inválida. Ingrese un número del 1 al 7.")
            continue

        if opcion == 1:
            agregar_tarea(tareas)
        elif opcion == 2:
            listar_tareas(tareas)
        elif opcion == 3:
            titulo_tarea = input("Ingrese el nombre de la tarea a completar: ")
            completar_tarea(tareas, titulo_tarea)
        elif opcion == 4:
            titulo_tarea = input("Ingrese el nombre de la tarea a eliminar: ")
            eliminar_tarea(tareas, titulo_tarea)
        elif opcion == 5:
            ruta = obtener_ruta("Ingrese el nombre del archivo JSON para guardar: ")
            guardar_tareas(tareas, ruta)
        elif opcion == 6:
            ruta = obtener_ruta("Ingrese el nombre del archivo JSON para cargar: ")
            # CONSIDERACIÓN FALTANTE: advertir al usuario que cargar un archivo
            # reemplaza las tareas actuales que no hayan sido guardadas
            if tareas:
                confirmacion = input("Esto reemplazará las tareas actuales. ¿Continuar? (s/n): ").strip().lower()
                if confirmacion != 's':
                    print("Carga cancelada.")
                    continue
            tareas = cargar_tareas(ruta)
        elif opcion == 7:
            # CONSIDERACIÓN FALTANTE: advertir si hay tareas sin guardar al salir
            if tareas:
                confirmacion = input("¿Desea salir sin guardar las tareas? (s/n): ").strip().lower()
                if confirmacion != 's':
                    continue
            print("Saliendo del programa.")
            break


# CONSIDERACIÓN FALTANTE: bloque de entrada estándar de Python
# Garantiza que main() solo se ejecute si este archivo se corre directamente,
# no si se importa como módulo desde otro script
if __name__ == "__main__":
    main()