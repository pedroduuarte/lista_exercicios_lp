"""QUESTÃO 4:
Elabore um algoritmo que calcule o que deve ser pago por um produto,
considerando o preço normal de etiqueta e a escolha da condição de
pagamento. Utilize os códigos a seguir para ler qual acondição de
pagamento escolhida e efetuar o cálculo adequado:
Código Condição de pagamento
 1 À vista em dinheiro ou cheque, recebe 10% de desconto
 2 À vista no cartão de crédito, recebe 15% de desconto
 3 Em duas vezes, preço normal de etiqueta sem juros
 4 Em três vezes, preço normal de etiqueta mais juros de 10%
 5 Em seis vezes, preço normal de etiqueta mais juros de 20%"""

price=float(input('Informe aqui o preço do produto: R$ '))
payment=float(input('Informe aqui o código de pagamento escolhido pelo cliente (1 a 5): '))

if payment == 1:
    price1 = price-(price/100)*10 
elif payment == 2: 
    price1 = price-(price/100)*15	
elif payment == 3: 
    price1 = price	
elif payment == 4: 
    price1 = (price/100)*10+price	
elif payment == 5:
    price1 = (price/100)*20+price
else: print('O código de pagamento é inválido.')
print(f'Preço final: R$ {price1}')