
def analizar_ventas(lista):
    mayor = max(lista)
    menor = min(lista)
    promedio = sum(lista) / len(lista)
    return mayor, menor, promedio


print("\nAnalisis de ventas")

ventas = [1200, 850, 1020, 2100, 1750, 980]

print("Lista de ventas:", ventas)

mayor, menor, promedio = analizar_ventas(ventas)

print("La venta mayor es:", mayor)
print("La venta menor es:", menor)
print("El promedio de ventas es:", promedio)
