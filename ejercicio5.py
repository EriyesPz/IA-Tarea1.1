""" 📘 Ejercicio 5: Sumar ventas por producto
Dado el siguiente diccionario:
ventas = {
 'Producto': ['A', 'B', 'A', 'C', 'B', 'A'],
 'Cantidad': [10, 5, 7, 3, 2, 8]
}
Agrupa las cantidades por producto y muestra la suma total de ventas por cada uno.
# Salida esperada:
# {'A': 25, 'B': 7, 'C': 3} """

def sumarVentasPorProducto(ventas):
    resumen = {}

    for i in range(len(ventas['Producto'])):
        producto = ventas['Producto'][i]
        cantidad = ventas['Cantidad'][i]
        if producto in resumen:
            resumen[producto] += cantidad
        else:
            resumen[producto] = cantidad
    return resumen

ventas = {
    'Producto': ['A', 'B', 'A', 'C', 'B', 'A'],
    'Cantidad': [10, 5, 7, 3, 2, 8]
}

resultado = sumarVentasPorProducto(ventas)
print(f"Total de ventas por producto: {resultado}")