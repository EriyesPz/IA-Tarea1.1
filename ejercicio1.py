""" Cree un programa que reciba una lista de números y devuelva el número mayor sin usar la función
max().

# Entrada: [3, 9, 4, 1, 15]
# Salida esperada: 15
 """

def encontrarNumeroMayor(lista):
    if not lista:
        return "La lista está vacía"
    mayor = lista[0]
    for numero in lista:
        if numero > mayor:
            mayor = numero
    return mayor
        

numeros = [3, 9, 4, 1, 15, 7, 2]

resultado = encontrarNumeroMayor(numeros)

print(f"El número mayor de la lista {numeros} es: {resultado}")