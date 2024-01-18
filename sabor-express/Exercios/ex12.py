try:
    numero_usuario = int(input('Digite um numero inteiro: '))
    for multiplicador in range(1,11):
        resultado = numero_usuario * multiplicador
        print(f'\n{numero_usuario} X {multiplicador} = {resultado}')
except:
    print('Numero digitado invalido')
        