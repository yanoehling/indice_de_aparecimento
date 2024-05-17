from operator import itemgetter

numeros = {}
cont = 60
jogos = open('jogos.txt')
num = jogos.read().replace('\n', ' ').split()

for c in range(1, 61):
    numeros[str(c)] = num.count(str(c))
print(f'{"Rank.":<13}{"Nº":<8}{"Aparecimentos"}')
print('-' * 21)

for k, v in sorted(numeros.items(), key=itemgetter(1)):
    print(f'{f"{cont}º lugar":<13}\033[33m{k:<9}\033[32m{v}\033[m')
    cont -= 1
print('-' * 21)
