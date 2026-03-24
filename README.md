# 📦 Sistema de Gestión de Inventario en Python

Aplicación de consola desarrollada en Python para gestionar un inventario de productos. Permite agregar, buscar, actualizar, eliminar productos y guardar/cargar la información mediante archivos CSV.

---

## 🚀 Funcionalidades

- ✅ Agregar productos al inventario  
- 📋 Mostrar inventario completo  
- 📊 Calcular estadísticas del inventario  
- 🔍 Buscar productos por nombre  
- ✏️ Actualizar productos  
- ❌ Eliminar productos  
- 💾 Guardar inventario en CSV  
- 📂 Cargar inventario desde CSV  
- 🔄 Fusionar o sobrescribir datos  

---

## 🧱 Estructura del Proyecto

```
proyecto/
│
├── inventario.py     # Programa principal (menú)
├── servicios.py      # Funciones del sistema
├── archivos.py       # Manejo de archivos CSV
└── inventario.csv    # Base de datos en CSV
```

---

## 🧠 Estructura de Datos

El inventario se maneja como una lista de diccionarios:

```python
{
    "nombre": str,
    "precio": float,
    "cantidad": int
}
```

---

## ⚙️ Instalación y Ejecución

1. Tener Python 3 instalado  
2. Clonar el repositorio o descargar los archivos  
3. Ejecutar el programa:

```bash
python inventario.py
```

---

## 📌 Menú del Programa

```
1 - Agregar producto
2 - Mostrar inventario
3 - Calcular estadistica
4 - Buscar producto
5 - Actualizar producto
6 - Eliminar producto
7 - Guardar CSV
8 - Cargar CSV
9 - Salir
```

---

## 💾 Manejo de CSV

### Guardar datos

```python
guardar_csv(inventario, ruta)
```

### Cargar datos

```python
cargar_csv(ruta, inventario, sobrescribir=True)
```

- `True`: reemplaza el inventario actual  
- `False`: fusiona con el inventario existente  

---

## 📊 Estadísticas

- 💰 Valor total del inventario  
- 📦 Cantidad total de productos  
- 🔝 Producto con mayor cantidad  
- 💎 Producto con mayor precio  

---

## 🧩 Funciones principales

### servicios.py

- `agregar_producto()`
- `pedir_cantidad()`
- `mostrar_inventario()`
- `calcular_estadisticas()`
- `buscar_producto()`
- `actualizar_producto()`
- `eliminar_producto()`

### archivos.py

- `guardar_csv()`
- `cargar_csv()`

---

## ⚠️ Validaciones

- Precio mayor a 0  
- Cantidad mayor a 0  
- Manejo de errores en archivos  
- Verificación de productos existentes  
