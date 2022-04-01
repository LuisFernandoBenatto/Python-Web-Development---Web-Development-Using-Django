def main(a, b):
    print("Aula_2")

    inputValue = int(input("Deseja inserir os valores de forma manual? \n" +
                       "Use 1 para SIM \n" + 
                       "Use 0 para NÃO \n" + 
                       "----------------> "))
    if(inputValue != 0): 
        a = int(input("Valor 1: "))
        b = int(input("Valor 2: "))
    soma = a + b
    sub = a - b
    mult = a * b
    div = a / b
    rest = a % b

    print(soma, sub, mult, div, rest)

    print(type(soma), type(sub), type(mult), type(div), type(rest))

    print(str(soma), str(sub), type(str(mult)), type(int(div)), str(rest))

    print("Soma: " + str(soma),
        "Subtração: " + str(sub),
        "Multiplicação: " + str(mult),
        "Divisão: " + str(div),
        "Resto: " + str(rest))

    print("Soma: {}".format(soma),
        "Subtração: {}".format(sub),
        "Multiplicação: {}".format(mult),
        "Divisão: {}".format(div),
        "Resto: {}".format(rest))

    print("Soma: {} Subtração: {} Multiplicação: {} Divisão: {} Resto: {}"
        .format(soma, sub, mult, div, rest))

    print("Soma: {soma} Subtração: {sub} Multiplicação: {mult} Divisão: {div} Resto: {rest}"
        .format(soma=soma, sub=sub, mult=mult, div=div, rest=rest))

if __name__ == '__main__':
    main(15, 5)