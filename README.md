# 📦 Sistema de Gestión de Inventario

Sistema de gestión de inventario por consola desarrollado en Python. Permite realizar operaciones CRUD sobre productos, calcular estadísticas del inventario y persistir los datos mediante archivos CSV.

---

## 🗂️ Estructura del proyecto

```
inventario/
├── inventario.py      # Programa principal y menú de opciones
├── servicios.py       # Funciones CRUD y estadísticas
├── archivos.py        # Funciones de persistencia CSV
└── README.md
```

---

## ✨ Funcionalidades

| Opción | Descripción |
|--------|-------------|
| 1 | Agregar producto (si ya existe, suma la cantidad) |
| 2 | Mostrar inventario completo |
| 3 | Calcular estadísticas del inventario |
| 4 | Buscar producto por nombre |
| 5 | Actualizar precio y cantidad de un producto |
| 6 | Eliminar un producto |
| 7 | Guardar inventario en archivo CSV |
| 8 | Cargar inventario desde archivo CSV |
| 9 | Salir y ver recibo final |

---

## 📋 Requisitos

- Python 3.8 o superior
- No requiere librerías externas (solo módulos de la biblioteca estándar: `csv`, `os`)

---

## 📁 Formato del archivo CSV

El sistema lee y escribe archivos CSV con el siguiente encabezado:

```
nombre,precio,cantidad
Manzana,1500.0,10
Leche,3200.5,5
Pan,800.0,20
```

**Reglas de validación al cargar:**
- El encabezado debe ser exactamente `nombre,precio,cantidad`
- `precio` debe ser un número mayor o igual a cero
- `cantidad` debe ser un entero mayor o igual a cero
- Las filas inválidas se omiten y se informa cuántas fueron ignoradas

---

## 🧩 Módulos

### `servicios.py`

Contiene las funciones principales de negocio:

- `agregar_producto()` — solicita y valida nombre y precio
- `pedir_cantidad()` — solicita y valida una cantidad entera positiva
- `mostrar_inventario(inventario)` — muestra todos los productos
- `calcular_estadisticas(inventario)` — retorna valor total, unidades totales, producto más caro y de mayor stock
- `buscar_producto(inventario, nombre_producto)` — retorna el producto o `None`
- `actualizar_producto(inventario, nombre_producto, nuevo_precio, nueva_cantidad)` — actualiza un producto existente
- `eliminar_producto(inventario, nombre_producto)` — elimina un producto de la lista

### `archivos.py`

Contiene las funciones de persistencia:

- `guardar_csv(inventario, ruta, incluir_header)` — guarda el inventario en un CSV
- `cargar_csv(ruta, inventario, sobrescribir)` — carga desde un CSV con opción de sobrescribir o fusionar

---

## 🔄 Lógica de carga CSV

Al cargar un archivo CSV el sistema pregunta al usuario qué acción tomar:

- **Sobrescribir (`s`)**: reemplaza el inventario actual por el contenido del archivo.
- **Fusionar (`n`)**: combina el CSV con el inventario actual. Si un producto ya existe, suma su cantidad; si no existe, lo agrega.

---

## 📊 Estadísticas disponibles

Al seleccionar la opción 3, el sistema calcula y muestra:

- 💰 **Valor total del inventario** — suma de `precio × cantidad` de todos los productos
- 📦 **Unidades totales** — suma de todas las cantidades
- 🏷️ **Producto más caro** — nombre y precio unitario más alto
- 📈 **Producto con mayor stock** — nombre y cantidad más alta

---

## 🧾 Recibo final

Al salir del programa (opción 9), se genera automáticamente un resumen con todos los productos registrados durante la sesión y el total a pagar:

```
========= RECIBO DE COMPRA =========
Cliente: Jose 

Manzana x 10 = $15000.0
Leche x 5 = $16002.0

TOTAL A PAGAR:   $31002.0

¡Gracias por su compra!
```

---

## ⚠️ Manejo de errores

El programa captura y gestiona los siguientes errores sin cerrar la aplicación:

- Entrada no numérica en precio, cantidad u opción del menú
- Archivo CSV no encontrado (`FileNotFoundError`)
- Archivo CSV con codificación inválida (`UnicodeDecodeError`)
- Archivo sin extensión `.csv`
- Encabezado CSV incorrecto
- Filas con datos inválidos o incompletos

