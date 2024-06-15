import pandas 


jogos = pandas.read_excel('historico_jogos_ms.xlsx')
contagens = {}

for i in range(len(jogos)):
    for num in jogos.loc[i][1:]:
        contagens[num] = contagens.get(num, 0) + 1

contagens = dict(sorted(contagens.items(), key=lambda item: item[1]))

for pos, num in enumerate(contagens):
    print(f'Número \033[33m{num}\033[m: \
    sorteado \033[36m{contagens[num]}\033[m vezes \
    (\033[32m{60-pos}°\033[m lugar)')
    