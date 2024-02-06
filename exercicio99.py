

# Exercício Python 099: Faça um programa que tenha uma função chamada maior(), que receba vários parâmetros com valores inteiros. Seu programa tem que analisar todos os valores e dizer qual deles é o maior.

#CORREÇÃO Guanabara
# def maior (* núm):
#   cont = maior = 0
#   print('='*90)
#   print('Analisando os valores passados...')
#   for valor in núm:
#     print(f'{valor}', end=' ')
#     cont += 1
#     if cont == 0:
#       maior = valor
#     else:
#       if valor > maior:
#         maior = valor
#   print(f'\nTotal de números digitados: {cont}, sendo o maio número: {maior}')
  
# maior( 0,1,2,3,4,5,6,2,34)
# maior(3,5,6,0)


#Codigo desenvolvido
def maior (* varios):
  num_maior = max(varios)
  contagem = len(varios)
  print(f'Foram inseridos {contagem} números, sendo eles:')
  for i in varios:
    print(i,end=' ')
  print(f'\nO maior número digitado foi o número: {num_maior}')

maior(4,5,6,3,9)