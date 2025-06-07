""" 📘 Ejercicio 2: Escriba un programa que solicite un número al usuario y
muestre la tabla de multiplicar del 1 al 10 de ese número.
# Entrada: 3
# Salida esperada:
# 3 x 1 = 3
# 3 x 2 = 6
# ...
# 3 x 10 = 30 """

def tablaMultiplicar(numero):
    if not isinstance(numero, int):
        return "Por favor, ingrese un numero entero"
    tabla = []
    for i in range(1, 11):
        resultado = numero * i
        tabla.append(resultado)
    return tabla

numero = 3

print(f"La tabla del numero {numero} es: {tablaMultiplicar(numero)}")