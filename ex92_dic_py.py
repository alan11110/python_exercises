#Exercicio 92 dicionarios
print('Crie um programa que leia nome, ano de nascimento e carteira de trabalho e cadastre-o (com idade) em um dicionário. Se por acaso a CTPS for diferente de ZERO, / o dicionário receberá também o ano de contratação e o salário. Calcule e acrescente, além da idade, com quantos anos a pessoa vai se aposentar')
from datetime import datetime


ano = datetime.now().year


infos ={}#simbolo dicionario
infos['Nome'] = str(input('Digite aqui seu nome: '))
infos['Idade'] = ano - int(input('Digite aqui o ano de nascimento: '))
infos['Carteira de Trabalho'] = int(input('Digite o número da carteira de trabalho ou 0 caso não tenha: '))

if infos['Carteira de Trabalho'] != 0:
        infos['Ano contratação'] = int(input('Digite o ano de contratação: '))
        infos['Salario '] = float(input('Digite o salário: R$ '))
        infos['Aposentadoria'] =  infos['Idade'] + 35
        print('Analisando...')
        for k,v in infos.items():
            print(f'{k} tem o valor de {v}')
else:
    print(infos)

