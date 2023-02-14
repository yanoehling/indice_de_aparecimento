from operator import itemgetter
cont = {}
y = 1
a = open('jogos.txt')
num = a.read().replace('\n', ' ').split()
for c in range(1, 61):
    cont[str(c)] = num.count(str(c))
print(f'{"Pos.":<6}{"Nº":<8}{"Quant."}')
print('-' * 21)
for k, v in sorted(cont.items(), key=itemgetter(1), reverse=True):
    print(f'{f"{y}º":<6}\033[33m{k:<9}\033[32m{v}\033[m')
    y += 1
print('-' * 21)
