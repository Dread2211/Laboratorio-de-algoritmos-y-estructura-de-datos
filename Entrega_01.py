nombre = input("ingrese su nombre: ")
sueldobasico = int(input("ingrese su sueldo: "))
canthijos = int(input("ingrese cantidad de hijos: "))

asignacionFamiliar = 1500 * canthijos
jub = (sueldobasico * 11) / 100
obraSocial = (sueldobasico * 3) / 100
presentismo = (sueldobasico *10) / 100
sueldoneto = sueldobasico - jub - obraSocial + asignacionFamiliar

print("el resultado es: ",sueldoneto)

