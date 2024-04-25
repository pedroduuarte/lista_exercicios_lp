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
