import random
from time import sleep
from operator import itemgetter

print('Crie um programa onde 4 jogadores joguem um dado e  tenham resultado aleatórios Guarde esses resultados em um dicionário. No final  coloque esse dicionário em ordem. Sabendo que o vencedor tirou o maior numero no dado')


dado1= random.randint(0,6)
dado2= random.randint(0,6)
dado3 =random.randint(0,6)
dado4= random.randint(0,6)
increment = 1

jogadoresdic = {'Jogador 1': dado1,'Jogador 2': dado2,'Jogador 3': dado3,'Jogador 4': dado4}

ranking = sorted(jogadoresdic.items(), key=itemgetter(1), reverse=True)

for i,c in jogadoresdic.items():
    print(f'O {i} tirou {c} no dado...')


for a,b in range (ranking):
    print(f'Em {a+1}º Lugar - Jogador {b[0]}, Pontos {b[1]} ')



