
def convertir_temperatura(c):
    f = (c * 9/5) + 32
    k = c + 273.15
    return f, k

print("Conversion de grados")
celsius = float(input("temperatura en grados Celsius: "))

fahrenheit, kelvin = convertir_temperatura(celsius)

print("En Fahrenheit es:", fahrenheit)
print("En Kelvin es:", kelvin)
