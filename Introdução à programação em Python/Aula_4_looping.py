from ast import While

def main(entrada, entrada_2):
    print("Aula_4")

    inputValue = int(input("Deseja inserir os valores de forma manual? \n" +
                       "Use 1 para SIM \n" + 
                       "Use 0 para NÃO \n" + 
                       "----------------> "))
    if(inputValue != 0): 
        entrada = int(input("Entre com o número: "))
        entrada_2 = int(input("Entre com o número: "))
    # Número primo
    contador = 0
    for x in range(1, entrada + 1):
        resto = entrada % x
        if(resto == 0):
            contador += 1
    if(contador == 2): 
        print("Esse número {} é primo".format(entrada))
    else:
        print("Esse número {} NÃO é primo".format(entrada))

    # Achar os 100 primeiros numeros primos
    for number in range(entrada_2 + 1):
        contador = 0
        for x in range(1, number + 1):
            resto = number % x
            if(resto == 0):
                contador += 1
        if(contador == 2): 
            print("Esse número {} é primo".format(number))
        # else:
        #     print("Esse número {} NÃO é primo".format(number))

def forInRange(a):
    # for x in range(100):
    #     print(x)
    for x in range(0, a):
        print(x)
    # for x in "Arquivo de texto":
    #     print(x)

def loopWhile(a):
    while(a < 100):
        print(a)
        a += 10

if __name__ == '__main__':
    main(6793, 100)
    forInRange(10)
    loopWhile(10)