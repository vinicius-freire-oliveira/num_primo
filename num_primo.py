n = int(input('Digite um número: '))

# Inicializa o contador de divisores
p = 0

# Loop para verificar se o número é primo
for c in range(1, n + 1):
    if n % c == 0:
        p += 1

# Verifica se o número de divisores é igual a 2, indicando que é primo
if p == 2:
    print('PRIMO')
else:
    print('NÃO É PRIMO')
