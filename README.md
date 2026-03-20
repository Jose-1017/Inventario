# 🛒 Sistema de Inventario y Compra en Python

Este proyecto es una aplicación en consola desarrollada en Python que simula un sistema básico de compras e inventario. Permite al usuario ingresar productos, calcular costos y visualizar un resumen de compra.

---

## 📌 Características

* Ingreso de nombre del cliente
* Registro de productos con:

  * Nombre
  * Precio
  * Cantidad
* Cálculo automático del costo total
* Almacenamiento de múltiples productos en un inventario
* Validación de datos (evita errores de entrada)
* Visualización del estado de compra
* Generación de recibo final

---

## 🧠 Lógica del Programa

El sistema está dividido en funciones para mejorar la organización y reutilización del código:

### 🔹 `pedir_producto()`

* Solicita el nombre del producto (solo letras)
* Solicita el precio (número positivo)

### 🔹 `pedir_cantidad()`

* Solicita la cantidad (número entero positivo)

### 🔹 `mostrar_estado(detalle, total)`

* Muestra el resumen actual de la compra
* Presenta el subtotal acumulado

---

## ⚙️ Funcionamiento

El programa utiliza un menú interactivo:

```
1 - Agregar producto
2 - Mostrar inventario
3 - Calcular estadística
4 - Salir
```

### ✔️ Opción 1:

* Permite ingresar productos
* Calcula el costo total
* Guarda los datos en un diccionario (inventario)

### ✔️ Opción 2:

* Muestra todos los productos registrados
* Si no hay productos, indica que el inventario está vacío

### ✔️ Opción 3:

* Muestra el estado actual de la compra

### ✔️ Opción 4:

* Finaliza el programa y muestra el recibo

---

## 🗂️ Estructura de Datos

El inventario se almacena como un diccionario:

```python
inventario = {
    "producto": {
        "precio": valor,
        "cantidad": cantidad
    }
}


## 🧾 Ejemplo de salida

```
--- Inventario ---
Manzana -> Precio: $2000, Cantidad: 3
Pan -> Precio: $1500, Cantidad: 2

Subtotal acumulado: $9000.00

