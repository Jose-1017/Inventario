📦 Sistema de Gestión de Inventario en Python

Este proyecto es una aplicación de consola desarrollada en Python que permite gestionar un inventario de productos. Incluye funcionalidades para agregar, buscar, actualizar, eliminar productos y persistir la información en archivos CSV.

🚀 Funcionalidades
✅ Agregar productos al inventario
📋 Mostrar inventario completo
📊 Calcular estadísticas del inventario
🔍 Buscar productos por nombre
✏️ Actualizar precio y cantidad de productos
❌ Eliminar productos
💾 Guardar inventario en archivo CSV
📂 Cargar inventario desde archivo CSV
🔄 Fusión o sobrescritura de inventario al cargar datos
🧱 Estructura del Proyecto
📁 proyecto/
│
├── inventario.py     # Programa principal (menú interactivo)
├── servicios.py      # Lógica del negocio (funciones del inventario)
├── archivos.py       # Manejo de archivos CSV
└── inventario.csv    # Archivo de almacenamiento de datos
🧠 Estructura de Datos

El inventario se maneja como una lista de diccionarios:

{
    "nombre": str,
    "precio": float,
    "cantidad": int
}

⚙️ Instalación y Ejecución
Asegúrate de tener Python instalado (3.x)
Clona o descarga el proyecto
Ejecuta el archivo principal:
python inventario.py

📌 Uso del Programa
Al ejecutar el programa, se mostrará un menú interactivo:

1 - Agregar producto
2 - Mostrar inventario
3 - Calcular estadistica
4 - Buscar producto
5 - Actualizar producto
6 - Eliminar producto
7 - Guardar CSV
8 - Cargar CSV
9 - Salir

Selecciona una opción ingresando el número correspondiente.

💾 Manejo de Archivos CSV
Guardar inventario
guardar_csv(inventario, ruta)
Guarda los productos en un archivo CSV
Puede incluir encabezados automáticamente
Cargar inventario
cargar_csv(ruta, inventario, sobrescribir=True)
sobrescribir=True: reemplaza el inventario actual
sobrescribir=False: fusiona los datos con el inventario existente
📊 Estadísticas Calculadas
💰 Valor total del inventario
📦 Cantidad total de productos
🔝 Producto con mayor cantidad
💎 Producto con mayor precio
🧩 Funciones Principales
📌 servicios.py
agregar_producto()
pedir_cantidad()
mostrar_inventario()
calcular_estadisticas()
buscar_producto()
actualizar_producto()
eliminar_producto()
📌 archivos.py
guardar_csv()
cargar_csv()
⚠️ Validaciones Incluidas
Precio debe ser mayor a 0
Cantidad debe ser mayor a 0
Manejo de errores al leer archivos
Validación de existencia de productos# Inventario
