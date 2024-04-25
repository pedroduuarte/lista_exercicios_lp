"""QUESTÃO 2:
 Solicite um número ao usuário. Se for divisível por 3, informe “é divisível por 3”. Se
for divisível por 4, informe “é divisível por 4”. Se for divisível por 3 e 4, informe “É
divisível tanto por 3 quanto por 4”."""


number=float(input('Digite o seu número: '))
if number%3 ==0 and number%4==0:
    print('O número é divisível por 3 e por 4.')
elif number%3==0 and number%4!=0: 
    print('O número é divisível por 3.')
elif number%3!=0 and number%4==0: 
    print('O número é divisível por 4.')
else: print('O número não é divisível nem por 3 nem por 4.')