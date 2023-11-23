print('Exercício 90 - Média de alunos com 2 inputs e usando dicionários e listas')
 # items no dicionario siginifica todos os campos
 #keys significa o titulo
 #value significa o conteudo


status_aluno = {}
dados_aluno = []

nome = str(input('Digite o nome do(a) aluno(a): '))
media_aluno = input('Digite a média do(a) aluno(a): ')
dados_aluno.append(nome)
dados_aluno.append(media_aluno)

status_aluno ={'Nome': nome, 'Média': media_aluno}


for i,v in status_aluno.items():
      print(f'{i} do(a) aluno(a) é: {v}')

if media_aluno >= '7':
    print(f'{status_aluno["Nome"]} está aprovado(a) !!!')
else:
    print(f'Infelizmente {status_aluno["Nome"]} está reprovado(a)')
