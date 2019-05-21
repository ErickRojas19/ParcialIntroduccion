import math

menu = 0
while menu != ("9"):
    print("Bienvenido a la calculadora de el tiche diego sentada :'v : ")
    print("\t1 - Decimal a Binario.")
    print("\t2 - Decimal a binario usando diferentes bases.")
    print("\t3 - Octal a binario.")
        
    print("\t4 - Hexadecimal a binario.")
    print("\t9 - Digite el 9 para salir :D .")
    menu = input ("Digite una de las opciones: ")
    if menu == ("1"):
        numeroDecimal=0 
        numeroBinario="" 
        resto = 0 
        print ("Número decimal a binario") 
        numeroDecimal=int(input('Introduce número decimal:')) 
        print ("Número decimal leido: ",numeroDecimal) 
        while (numeroDecimal>=2):
            resto = numeroDecimal % 2 
            numeroDecimal=(int)(numeroDecimal/2) 
            numeroBinario+=(str)(resto) 
        numeroBinario+=(str)(numeroDecimal) 
        lista=list(numeroBinario) 
        lista.reverse() 
        print ("Número binario obtenido: ",lista)
    
    elif menu == ("2"):
        newmenu = 0
        while newmenu != ("9"):
            print("Selecciones la base que desea utilizar: ")
            print("\t1 - Binario a base 8. ")
            print("\t2 - Binario a base 10. ")
            print("\t3 - Binario a base 16. ")
            print("\t9 - Para elegir la base otra vez. ")
            newmenu = input("Digite la operación aca: ")
            if newmenu == "1":
                binario_8 = int(input("Digite el numero en binario para pasar a decimal base 8 (Octal): "))
                if binario_8 == "9":
                    exit()
                else:
                    a = int(input(binario_8, 2))
                    print(binario_8 ,"Octal=",oct(a))
            if newmenu == "2":
                decimal_new = int(input("Digite el numero binario: "))
                acu = decimal_new
                plus = 0
                cj = 0
                binario_10 = decimal_new
                while cj < acu:
                    si_num = binario_10/10
                    binario_10 = int(binario_10/10)
                    if si_num == 0 or si_num == 1:
                        plus=plus + 2**cj * si_num
                    cj+cj+1
                    print(plus)
            elif newmenu == "3":
                a = int(binario_8, 2)
                binario_16 = int(input("Digite un binario a convertir a Hexadecimal: "))
                if binario_16 == "9":
                    exit()
                else:
                    a =int(binario_16, 2)
                    print(binario_16,"En Hexadecimal: ", hex(a))
    elif menu == ("3"):

        print("Digite 9 para salir.");
        octal = input("Digite un numero para en base 8: ");
        if octal == ("9"):
            exit();
        else:
            dec = str(int(octal, 8));
            decm = int(dec);
            print(octal,"En binario =",bin(decm));
    
    elif menu == ("4"):

        print("Digite el 9 para salir. ");
        hexdec = input("Digite un numero de la forma Hexadecimal: ");
        if hexdec == ("9"):
            exit();
        else:
            dec = int(hexdec, 16);
            print(hexdec,"En binario =",bin(dec));