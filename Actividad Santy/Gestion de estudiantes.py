
estudiantes = []

def agregar_estudiante(nombre, nota):
    estudiante = {
        "nombre": nombre,
        "nota": nota
    }
    estudiantes.append(estudiante)
    
def mostrar_estudiantes():
    print("\nLista de estudiantes:")
    for e in estudiantes:
        print("Nombre:", e["nombre"], "- Nota:", e["nota"])

def calcular_promedio():
    suma = 0
    for e in estudiantes:
        suma = suma + e["nota"]
    
    if len(estudiantes) > 0:
        promedio = suma / len(estudiantes)
    else:
        promedio = 0
    
    return promedio

print("\nGestion de estudiantes")

cantidad = int(input("¿Cuántos estudiantes desea agregar?: "))

for i in range(cantidad):
    nombre = input("Nombre del estudiante: ")
    nota = float(input("Nota del estudiante: "))
    agregar_estudiante(nombre, nota)

mostrar_estudiantes()

print("El promedio general es:", calcular_promedio())
