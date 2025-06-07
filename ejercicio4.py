""" 📘 Ejercicio 4: Escriba un programa que solicite ingresar el nombre de varios
estudiantes y su nota, y lo almacene en un diccionario. Al final, muestra los
datos almacenados.
# Entrada:
# Nombre: Ana | Nota: 90
# Nombre: Luis | Nota: 85
# Nombre: Juan | Nota: 92
# Salida esperada:
# {'Ana': 90, 'Luis': 85, 'Juan': 92} """

def ingresar_estudiantes():
    estudiantes = {}

    while True:
        ingresar = input("¿Desea ingresar un estudiante? (si/no): ").lower()
        if ingresar not in ("si"):
            break

        nombre = input("Ingrese el nombre del estudiante: ").strip()
        if not nombre:
            print("El nombre no puede estar vacio.")
            continue
        nota = float(input(f"Ingrese la nota de {nombre}: "))

        estudiantes[nombre] = nota

    return estudiantes

estudiantes = ingresar_estudiantes()

print(f"Datos de los estudiantes ingresados son: {estudiantes}")