"""
horas = int(input("Horas trabajadas: "))
valorhora = int(input("Cuánto gana por hora: "))
valorapagar = horas * valorhora 
#vamos a dar subsidio de 200k a los que ganen menos de 1.500#
if valorapagar < 1500000:
    valorapagar += 200000    
else:
    valorapagar += 100000
print("El valor a recibir es: ", valorapagar)
"""
edad = int(input("Qué edad tiene: "))
if edad <= 0:
    print("Edad invalida")
else: 
    if edad < 6:
        print("Primera infancia")
    elif edad >=6 and edad <13:
        print("Niñez")
    elif edad >= 13 and edad <18:
        print("Adolescencia")
if edad >100:
     print ("Edad invalida")
else:
    if edad >18:
        print("Adulto")
