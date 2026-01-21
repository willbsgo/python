numero_1 = float(input("qual o primeiro numero "))
numero_2 = float(input("qual o segundo numero "))
numero_3 = float(input("qual o terceiro numero "))

if numero_1 > numero_2:
    maior = numero_1

else:
    maior = numero_2

if numero_3 > maior:
    maior = numero_3

print(f"o maior numero é {maior}")

if numero_1 < numero_2:
    menor = numero_1

else:
    menor = numero_2

if numero_3 < menor:
    menor = numero_3

print(f"o menor numero é {menor}")