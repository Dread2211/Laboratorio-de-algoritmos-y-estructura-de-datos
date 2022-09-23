import random
n = int(input("ingrese el numero de productos: "))
preciotot=0
num = random.randint(1,5)
for x in range (n):
    producto = int(input("ingrese el precio de los productos: "))
    preciotot=preciotot+producto
    if preciotot>10000: 
        print("su compra aplica para el descuento")
        print(num)
        if num==1:
            print("su compra no tiene descuento")
        else:
            if num==2:
                preciodesc=preciotot*0.15
                print("su precio es de:", preciodesc)
            else:
                if num==3:
                    preciodesc=preciotot*0.40
                    print("su precio es de:",preciodesc)
                else:
                    if num==4:
                        preciodesc=preciotot*0.55
                        print("su precio es de: ",preciodesc)
                    elif num==5:
                                preciodesc=preciotot*0.65
                                print("su precio es de: ",preciodesc)
else:
    print("su compra no supera los $10.000 asi que no se le puede aplicar la promocion")
