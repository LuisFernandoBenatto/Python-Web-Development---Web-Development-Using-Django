def conjunto():
    novo_conjunto = {0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 11, 15}
    print(novo_conjunto)

    novo_conjunto.add(20)
    novo_conjunto.add(30)
    print("Adiconando: {}".format(novo_conjunto))

    novo_conjunto.discard(30)
    print("Descartando: {}".format(novo_conjunto))

    novo_conjunto_2 = {10, 11, 12, 13, 14, 15, 16, 17, 18, 19}
    conjunto_uniao = novo_conjunto.union(novo_conjunto_2)
    print("União: {}".format(conjunto_uniao))

    novo_conjunto.add(21)
    novo_conjunto.add(12)
    novo_conjunto.add(13)
    novo_conjunto.add(14)
    conjunto_interseccao = novo_conjunto.intersection(novo_conjunto_2)
    print("Interseccao: {}".format(conjunto_interseccao))

    conjunto_diferenca = novo_conjunto.difference(novo_conjunto_2)
    conjunto_diferenca_2 = novo_conjunto_2.difference(novo_conjunto)
    print("Diferença de 1 para 2: {}".format(conjunto_diferenca), 
          "Diferença de 2 para 1: {}".format(conjunto_diferenca_2))

    conjunto_diferenca_simetrica = novo_conjunto.symmetric_difference(novo_conjunto_2)
    print("Difereça Simétrica: {}".format(conjunto_diferenca_simetrica))

    print("\n\n")
    conjunto_a = {0, 1, 2, 3, 4}
    conjunto_b = {0, 1, 2, 3, 4, 5, 6, 7, 8, 9}
    conjunto_subset_1 = conjunto_b.issubset(conjunto_a)
    conjunto_subset_2 = conjunto_a.issubset(conjunto_b)
    print("Conjunto b é um subconjunto de a: {}".format(conjunto_subset_1), #False
          "Conjunto a é um subconjunto de b: {}".format(conjunto_subset_2)) #True
    
    conjunto_superset_1 = conjunto_b.issuperset(conjunto_a)
    conjunto_superset_2 = conjunto_a.issuperset(conjunto_b)
    print("Conjunto b é um superconjunto de a: {}".format(conjunto_superset_1), #True
          "Conjunto a é um superconjunto de b: {}".format(conjunto_superset_2)) #False

    print("\n\n")

    lista = ["cachorro", "gato", "coelho", "rato", "cobra", 
             "aranha", "peixe", "galinha", "vaca", "porco",
             "cachorro", "gato", "coelho", "rato", "cobra", 
             "aranha", "peixe", "galinha", "vaca", "porco"]
    print(lista)
    
    conjunto_animais = set(lista)
    print(conjunto_animais)

    lista_animais = list(conjunto_animais)
    print(lista_animais)

    print("\n\n")
if __name__ == '__main__':
    conjunto()