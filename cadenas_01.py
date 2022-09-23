numero_de_empleados = int(input("ingrese el numero de empleados: "))
for i in range (numero_de_empleados):
       nombre=input("ingrese su nombre:")
       print(nombre[0:3])

       dni=input("ahora ingrese su dni:")
       print(dni[5:8])

       print("Su nombre es:",nombre)
       print ("Su dni es:",dni)
       user=nombre[0:3] + dni[5:8]
       print ("Su usuario es:",user)



