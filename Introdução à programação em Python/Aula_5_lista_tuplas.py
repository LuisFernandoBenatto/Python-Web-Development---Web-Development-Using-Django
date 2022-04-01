def main():
    lista = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]
    lista_de_animal = ["cachorro", "gato", "coelho", "rato", "cobra", 
                       "aranha", "peixe", "galinha", "vaca", "porco"]
    
    print("Soma da lista: {}".format(sum(lista)))
    soma = 0
    for l in lista:
        print(l)
        soma += l 
    print("Soma da lista: {}".format(soma))

    print("Maior valor da lista: {}".format(max(lista)))
    print("Menor valor da lista: {}".format(min(lista)))
    print("\n\n")

    for animal in lista_de_animal:
        print(animal)
    print("Maior valor da lista: {}".format(max(lista_de_animal)))
    print("Menor valor da lista: {}".format(min(lista_de_animal)))

    animal = 'lobo'
    if(animal in lista_de_animal):
        print("Existe {} nessa lista!".format(animal))
    else:
        print("Não existe {} nessa lista!".format(animal))
    
    nova_lista = lista_de_animal * 5
    print(nova_lista)
    print("\n\n")

def listas():
    lista_aleatoria = ['banana', 'laranja', 'mamão', 'maça', 'melancia', 'limão', 'pera', 'uvas']
    lista_aleatoria.append('tomate')
    print(lista_aleatoria)

    lista_aleatoria.pop()
    print(lista_aleatoria)

    lista_aleatoria.pop(2) #removendo da lista referenciando a posicao
    print(lista_aleatoria)

    lista_aleatoria.remove('banana') 
    print(lista_aleatoria)
    print("\n\n")

def ordenarLista():
    lista_ordenada = [35, 67, 41, 24, 38, 20, 112, 80, 1, 19, 11, 57]
    lista_ordenada.sort()
    print(lista_ordenada)

    lista_ordenada.reverse()
    print(lista_ordenada)
    print("\n\n")

def tuplas():
    # Listas imutaveis
    tupla = ('banana', 'laranja', 'mamão', 'maça', 'melancia', 'limão', 'pera', 'uvas')
    tupla_2 = (35, 67, 41, 24, 38, 20, 112, 80, 1, 19, 11, 57)

    print(tupla, tupla_2)

    # tupla[0] = 'banana maça' # erro!!!

    lista_de_animal = ["cachorro", "gato", "coelho", "rato", "cobra", 
                       "aranha", "peixe", "galinha", "vaca", "porco"]

    print(len(tupla), len(tupla_2))
    tupla_animal = tuple(lista_de_animal)
    print(type(tupla_animal))
    print(tupla_animal)

    lista_numerica = list(tupla_2)
    print(type(lista_numerica))
    print(lista_numerica)

    print("\n\n")

if __name__ == '__main__':
    main()
    listas()
    ordenarLista()
    tuplas()