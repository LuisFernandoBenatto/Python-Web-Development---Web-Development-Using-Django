def media():
    print("Média de notas")
    quantNotas = float(input("Qual a quantidade de notas? \n" + "----------------> "))
    soma = 0
    quantNotas_2 = quantNotas
    while(quantNotas_2 > 0):
        nota = float(input("Qual foi valor da sua nota: "))
        while(nota > 10):
            nota = float(input("Nota não aceita, as notas variam de 0 a 10.\n "+ "Qual foi valor da sua nota: "))
        soma += nota
        quantNotas_2 -= 1

    media = soma / quantNotas
    print("Média: {}".format(media))

if __name__ == '__main__':
    media()