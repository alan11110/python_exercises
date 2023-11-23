#Exercício Python 093: Crie um programa que gerencie o aproveitamento de um jogador de futebol. O programa vai ler o nome do jogador e quantas partidas ele jogou. 
#Depois vai ler a quantidade de gols feitos em cada partida. No final, tudo isso será guardado em um dicionário, incluindo o total de gols feitos durante o campeonato.

infos ={}# simbolo dicionario
gols = []
infos['Nome'] = str(input('Digite o nome do jogar: '))
infos['Qtd partidas'] = input(f' Quantas partidas o jogador {infos["Nome"]}: ')

for i in range (int(infos['Qtd partidas'])):
    gols.append =  input(f'Quantos gols o {infos["Nome"]}  fez na {i+1} partida?: ')
    
print(gols)
