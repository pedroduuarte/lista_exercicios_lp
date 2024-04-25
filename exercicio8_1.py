""" QUESTÃO 1: 
O IMC (índice de massa corpórea) indica o grau de obesidade de uma pessoa. Este
índice é obtido pelo peso (em kg) dividido pelo quadrado da altura (em metros). A
tabela a seguir apresenta as faixas deste índice:

Faça um programa que solicita o peso e a altura de uma pessoa, calcule o IMC,
apresente o seu valor e a avaliação."""


weigh=float(input('Coloque aqui o seu peso (em kg): '))
high=float(input('Coloque aqui a sua altura (em m): '))
imc=weigh/high**2
if imc<20: 
    print(f'Seu IMC é: {imc:.3F}. Sua avaliação de IMC é: ABAIXO DO NORMAL.')
elif imc>=20 and imc<25:
    print(f'Seu IMC é: {imc:.3F}. Sua avaliação de IMC é: NORMAL.')
elif imc>=25 and imc<30: 
    print (f'Seu IMC é: {imc:.3F}. Sua avaliação de IMC é: SOBREPESO.')
elif imc>=30 and imc<35: 
    print(f'Seu IMC é: {imc:.3F}. Sua avaliação de IMC é: OBESIDADE LEVE.')
elif imc>=35 and imc<40:
    print(f'Seu IMC é: {imc:.3F}. Sua avaliação de IMC é: OBESIDADE MODERADA.')
else: 
    print (f'Seu IMC é {imc:.3F}. Sua avaliação de IMC é: OBESIDADE MÓRBIDA.')
     