"""
QUESTÃO 3:
Faça um programa para o cálculo de uma folha de pagamento, sabendo que os
descontos são do Imposto de Renda, que depende do salário bruto (conforme
alíquotas abaixo) e 3% para o Sindicato e que o FGTS corresponde a 11% do
Salário Bruto, mas não é descontado (é a empresa que deposita). O Salário Líquido
corresponde ao Salário Bruto menos os descontos. O programa deverá pedir ao
usuário o valor da sua hora e a quantidade de horas trabalhadas no mês.
Salário Bruto até 900 (inclusive) - isento
Salário Bruto até 1500 (inclusive) - desconto de 5%
Salário Bruto até 2500 (inclusive) - desconto de 10%
Salário Bruto acima de 2500 - desconto de 20%
Imprima na tela as informações, dispostas conforme
o exemplo ao lado. No exemplo o valor da hora é 5 e
a quantidade de hora é 220."""

worked_hours=float(input('Insira aqui a quantidade de horas trabalhadas esse mês: '))
value_per_hour=float(input('Insira aqui o valor da hora trabalhada na sua empresa: '))
brute_salary=worked_hours*value_per_hour
inss=brute_salary*0.10
sindicato=brute_salary*0.03
fgts=brute_salary*0.11
if brute_salary>=0 and brute_salary<=900:
    ir=0
elif brute_salary>900 and brute_salary<=1500:
    ir=brute_salary*0.05
elif brute_salary>1500 and brute_salary<=2500: 
    ir=brute_salary*0.10
else: ir=brute_salary*0.20
total_descounts=inss+sindicato+fgts+ir
liquid_salary=brute_salary-total_descounts
print(f'''Salário Bruto       : R$ {brute_salary:.2f}
(-)IR               : R$ {ir:.2f}
(-)INSS (10%)       : R$ {inss:.2f}
(-)Sindicato (3%)   : R$ {sindicato:.2f}
(-)FGTS(11%)        : R$ {fgts:.2f}
Total de descontos  : R$ {total_descounts:.2f}
Salário Líquido     : R$ {liquid_salary:.2f}''')
