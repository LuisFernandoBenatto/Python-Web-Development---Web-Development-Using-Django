class Contador_de_letras:
    def __init__(self):
        pass
    def contador_de_letras(self, lista_de_palavras):
        contador = []
        for x in lista_de_palavras:
            quantidade = len(x)
            contador.append(quantidade)
        return contador

if __name__ == '__main__':
    lista = ["cachorro", "gato", "arara", "lobo", "onça", "leão", "aranha", "tigre", "puma", "elefante"]
    contador = Contador_de_letras()
    print("Total de letra de cada palavra da lista: {}".format(contador.contador_de_letras(lista)))