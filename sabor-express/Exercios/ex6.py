idade = int(input('Digite sua idade: '))

if idade == 0 or idade <= 12:
    print('Criança')
elif idade == 13 or idade <= 18:
    print('Adolecente')
else:
    print('Adulto')