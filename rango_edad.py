def comparacion_edad(edad):
    if (edad < 18):
        return "Esa persona es menor de edad"
    if (edad > 18 and edad < 65):
        return "Esa persona es adulta"
    if (edad > 65 and edad < 110):
        return "Esa persona es un adulto mayor"
    else:
        return "Esa persona esta muerta"

edad1 = int(input("Dime una edad:"))

print(comparacion_edad(edad1))
