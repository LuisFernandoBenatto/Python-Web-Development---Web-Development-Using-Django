def main(a, b, c):
    print("Aula_3")

    inputValue = int(input("Deseja inserir os valores de forma manual? \n" +
                       "Use 1 para SIM \n" + 
                       "Use 0 para NÃO \n" + 
                       "----------------> "))
    if(inputValue != 0): 
        a = int(input("Valor 1: "))
        b = int(input("Valor 2: "))
        c = int(input("Valor 3: "))
    
    if(a > b and a > c):
        print("O maior valor é A: {}".format(a))
    elif(b > c and b > c):
        print("O maior valor é B: {}".format(b))
    else:
        print("O maior valor é C: {}".format(c))


    if(a == b and a == c):
        print("Os valores A, B e C são iguais: {a} = {b} = {c}".format(a=a, b=b, c=c))
    elif(a == b):
        print("Os valores A e B são iguais: {a} = {b}".format(a=a, b=b))
    elif(a == c):
        print("Os valores A e C são iguais: {a} = {c}".format(a=a, c=c))
    elif(b == c):
        print("Os valores B e C são iguais: {b} = {c}".format(b=b, c=c))
    else:
        print("Os valores A, B e C são diferentes: {a} != {b} != {c}".format(a=a, b=b, c=c))

    resto_a = a % 2
    if(resto_a == 0):
        print("Número é par!")
    else:
        print("Número é impar!")
    
    resto_b = b % 2
    resto_c = c % 2
    if(resto_a == 0 or resto_b == 0 or resto_c == 0):
        print("Foi digitado um número par")
    else:
        print("Nenhum número par digitado!")

    if(resto_a == 0 or not resto_b != 0 or not resto_c != 0):
        print("Foi digitado um número par")
    else:
        print("Nenhum número par digitado!")

def media(a, b, c, d):
    print("\n\n\nMédia de 4 notas")
    inputValue = int(input("Deseja inserir os valores de forma manual? \n" +
                       "Use 1 para SIM \n" + 
                       "Use 0 para NÃO \n" + 
                       "----------------> "))
    if(inputValue != 0): 
        a = int(input("Nota 1: "))
        if(a > 10):
            a = int(input("Valor digitado errado. Nota 1: "))
        b = int(input("Nota 2: "))
        if(b > 10):
            b = int(input("Valor digitado errado. Nota 2: "))
        c = int(input("Nota 3: "))
        if(c > 10):
            c = int(input("Valor digitado errado. Nota 3: "))
        d = int(input("Nota 4: "))
        if(d > 10):
            d = int(input("Valor digitado errado. Nota 4: "))
    
    media = (a + b + c + d) / 4
    print("Média: {}".format(media))

    if(media >= 7.0):
        print("Aprovado")
    elif(media < 7.0 and media >= 4.0):
        print("Exame")
    else:
        print("Reprovado")

if __name__ == '__main__':
    main(15, 5, 20)
    media(10, 10, 10, 10)