horas = int(input("Horas trabajadas: ")) 
vrhoras = int(input("Cuánto gana por horas: "))
vrapagar = horas * vrhoras
género =(input("Ingrese su género (hombre/mujer): ")).strip().lower()
F = "mujer"
M = "hombre"
if vrapagar < 1500000:
    if género == "mujer":
      vrapagar += 200000
    elif género == "hombre":
        vrapagar += 100000
if vrapagar >1500000 and vrapagar <200000:
        vrapagar += 50000
else:
    vrapagar >= 2000000
    vrapagar +=0
print("El valor a pagar es de",vrapagar)