# 🛒 Sistema de Inventario / Compra en Python

Este proyecto es un programa sencillo en Python que simula un sistema de
compra donde el usuario puede ingresar productos, cantidades y precios.

El sistema calcula automáticamente el costo total y genera un recibo
final de compra.

------------------------------------------------------------------------

## 📌 Características

-   Solicita el nombre del cliente
-   Permite agregar múltiples productos
-   Valida que:
    -   El nombre del producto tenga solo letras
    -   El precio sea un número válido mayor que 0
    -   La cantidad sea un número entero mayor que 0
-   Calcula automáticamente:
    -   El costo por producto
    -   El subtotal acumulado
    -   El total final de la compra
-   Muestra el estado de la compra en tiempo real
-   Genera un recibo final

------------------------------------------------------------------------

## ⚙️ Funcionamiento del programa

El programa funciona mediante un menú interactivo en consola.

Opciones disponibles:

1 - Agregar producto\
2 - Salir y generar recibo

Cada vez que el usuario agrega un producto, el sistema calcula su costo
y actualiza el subtotal.

------------------------------------------------------------------------

## 🧩 Estructura del código

El programa está compuesto por 3 funciones principales y un bloque
principal del programa.

### 1. pedir_producto()

Se encarga de solicitar: - Nombre del producto - Precio del producto

Incluye validaciones para asegurar que: - El nombre solo tenga letras -
El precio sea un número válido mayor que 0

### 2. pedir_cantidad()

Solicita la cantidad de productos que el usuario desea comprar.

Valida que: - Sea un número entero - Sea mayor que 0

### 3. mostrar_estado(detalle, total)

Muestra el estado actual de la compra, incluyendo:

-   Lista de productos agregados
-   Cantidad de cada producto
-   Costo por producto
-   Subtotal acumulado

------------------------------------------------------------------------

## ▶️ Ejemplo de uso

Ingrese su nombre: José

1 - Agregar producto 2 - Salir

Seleccione una opción: 1

Ingrese el nombre del producto: Manzana\
Ingrese el precio del producto: 2\
Ingrese la cantidad: 3

------------------------------------------------------------------------

## 🧾 Recibo final

========= RECIBO DE COMPRA =========\
Cliente: José

Manzana x3 = \$6.00

TOTAL A PAGAR: \$6.00

¡Gracias por su compra!
