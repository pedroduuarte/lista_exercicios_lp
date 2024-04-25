"""QUESTÃO 5:
Faça um Programa que peça os 3 lados de um triângulo. O programa deverá
informar se os valores podem ser um triângulo. Indique, caso os lados
formem um triângulo, se o mesmo é: equilátero, isósceles ou escaleno. Dicas:
Três lados formam um triângulo quando a soma de quaisquer dois lados for
maior que o terceiro;
Triângulo Equilátero: três lados iguais;
Triângulo Isósceles: quaisquer dois lados iguais;
Triângulo Escaleno: três lados diferentes;"""

side1=float(input('Informe aqui o tamanho do primeiro lado(em cm): '))
side2=float(input('Informe aqui o tamanho do primeiro lado(em cm): '))
side3=float(input('Informe aqui o tamanho do primeiro lado(em cm): '))
if side1+side2>side3 and side1+side3>side2 and side2+side3>side1: 
    print('Seus lados formam um triângulo.')
    if side1==side2 and side1==side3: 
        print('O seu triângulo é: Equilátero.')
    elif side1==side2 or side2==side3 or side1==side3: 
        print('E o seu triângulo é: Isósceles.')
    else: print('E o seu triângulo é: Escaleno.')
else: print('Os seus lados não formam um triângulo')