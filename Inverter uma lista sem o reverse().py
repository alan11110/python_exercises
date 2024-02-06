lista = [5, 4, 3, 2, 1]

def invertido(a):
    

    reversed_list = lista[::-1]
    #start: Índice inicial da fatia.
# stop: Índice final da fatia (não inclusivo).
# step: Passo, que determina a diferença entre os índices selecionados.
# Quando start e stop são omitidos, eles assumem valores padrão que cobrem toda a lista. No entanto, ao usar um passo negativo, você pode inverter a ordem dos elementos.

# No caso de lista[::-1]:

# start: Omissão (: antes do primeiro :).
# stop: Omissão (: entre os dois :).
# step: -1 (indicando que a sequência deve ser percorrida em ordem reversa).
# Portanto, lista[::-1] cria uma nova lista que contém todos os elementos de lista, mas na ordem inversa.
    print(f' Lista invertida= {reversed_list}')
    

print(f'Lista normal= {lista} ')
invertido(lista)