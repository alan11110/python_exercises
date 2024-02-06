# Exercício Python 100: Faça um programa que tenha uma lista chamada números e duas funções chamadas sorteia() e somaPar(). A primeira função vai sortear 5 números e vai colocá-los dentro da lista e a segunda função vai mostrar a soma entre todos os valores pares sorteados pela função anterior.

from time import sleep
import random
números = []

def sorteia(a):
  print('Sorteando 5 valores...')
  for i in range (0,5):
     a.append(random.randrange(1,20,1 ))
     sleep(1)
  print(a)

def somaPar(a):
   soma_pares = 0
   cont_pares = 0
   for i in a:
      if i % 2 == 0:
         soma_pares += i
         cont_pares += 1
   print(f'Nesta lista há {cont_pares} números pares, a soma deles tem um total de {soma_pares}.')

sorteia(números)
somaPar(números)



