#Exercício Python 093: Crie um programa que gerencie o aproveitamento de um jogador de futebol. O programa vai ler o nome do jogador e quantas partidas ele jogou. 
#Depois vai ler a quantidade de gols feitos em cada partida. No final, tudo isso será guardado em um dicionário, incluindo o total de gols feitos durante o campeonato.

infos ={}# simbolo dicionario
gols = []
n_gol = 0
soma = int() 
increment = 0

infos['Nome'] = str(input('Digite o nome do jogador: '))
qtd_partida = int(input(f' Quantas partidas o jogador {infos["Nome"]} jogou?  '))
for i in range (0, qtd_partida):
    n_gol =int(input(f'Quantos gols o {infos["Nome"]}  fez na {i+1} partida? '))
    gols.append(n_gol)
    soma = n_gol + soma
print('=-'*40)
infos['Qtd gols por partida'] = gols
infos['total'] = int(0)
infos['total'] = soma
print(infos)
print('=-'*40)
for k,v in infos.items():
    print(f'O campo {k} tem o valor {v}')
print('=-'*40)
print(f'O Jogador {infos["Nome"]} jogou {qtd_partida} partidas.')
for k in range (1, qtd_partida+1):
    print(f'-> Na partida {k}, fez {infos["Qtd gols por partida"][increment]} gols.')
    increment += 1
print(f'Foi um total de {infos["total"]} gols.')
