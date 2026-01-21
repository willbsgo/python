numero_1 = input("qual o primeiro numero ")
numero_2 = input("qual o segundo numero ")
numero_3 = input("qual o terceiro numero ")

if numero_1 > numero_2 and numero_1 > numero_3:
    print (f"{numero_1}")

if numero_2 > numero_1 and numero_1 > numero_3:
    print (f"{numero_2}") 

else:
     print (f"{numero_3}")      
