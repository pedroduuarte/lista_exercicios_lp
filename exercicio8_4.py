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