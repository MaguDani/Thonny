def multiplo (numero):
    if (numero % 3 == 0):
        return "Tu numero es múltiplo de 3"
    else:
        return "Tu número no es múltiplo de 3"
    
num = int(input("Dime un número: "))

print(multiplo(num))
