"""
i = 1
while i <= 10:
    print(i)
    i = i +1
"""
"""
i=1
while i <= 10:
    print (3*i)
    i += 1
"""
"""
user=int(input("ingrese la tabla de multiplicacion deseada: "))
x = 1
while x <= 10:
    print(user*x)
    x +=1
"""
"""
user=int(input("ingrese la tabla de multiplicacion deseada: "))
x= 1
while x <= 10:
    print(user,"X",x,"=",user*x)
    x += 1 
"""
"""
numero= int(input("ingrese el numero divisible: "))
x=1
while x<=100:
    if x % numero == 0:
     print(x)
    x += 1
"""
"restaurante riquiti"
cuentaperros= 0
cuentahamburguesas= 0
cuentasalchis=0
cuentapizzas=0
opcion= 0
menu= """
1. perro 10000
2. hamburguesa 18000
3. salchi 14000
4. pizza 10000
terminar
"""
print(menu)
while opcion != 5:
    opcion= int(input("opcion: "))
    if opcion == 1:
     cuentaperros += 10000
    elif opcion==2:
        cuentahamburguesas+= 18000
    elif opcion ==3:
        cuentasalchis+= 14000
    elif opcion == 4:
        cuentapizzas+= 10000
print("El valor de la cuenta es:en perros", cuentaperros,",en hamburguesas",cuentahamburguesas,",en salchis", cuentasalchis,",en pizzas",cuentapizzas)