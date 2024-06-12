# Coletamos o número
num = int(input('Insira um número inteiro: '))

# Números inteiros iguais ou abaixo de 1 não são primos
if num > 1:
    primo = True  # Suponha que o número é primo
    for i in range(2, num):
        # Verificamos se o número é divisível por algum outro número entre 2 e num - 1
        if (num % i) == 0:
            primo = False  # Se for divisível, não é primo
            break

    # Se nenhum divisor foi encontrado, o número é primo
    if primo:
        print(f'{num} é um número primo')
    else:
        print(f'{num} não é um número primo')
else:
    print(f'{num} não é um número primo')
