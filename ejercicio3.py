""" 📘 Ejercicio 3: Cree un programa que elimine los elementos repetidos de una
lista y devuelva una nueva lista con elementos únicos ordenados.
# Entrada: [4, 2, 7, 4, 2, 1, 9, 7]
# Salida esperada: [1, 2, 4, 7, 9]
 """

def eliminarRepetidosOrdenados(lista):
    if not isinstance(lista, list):
        return "Ingrese una lista"
    lista_unica = []
    
    for elemento in lista:
        if elemento not in lista_unica:
            lista_unica.append(elemento)
    return sorted(lista_unica)

lista = [4, 2, 7, 4, 2, 1, 9, 7]
print(f"La lista sin elementos repetidos y ordenada es: {eliminarRepetidosOrdenados(lista)}")
