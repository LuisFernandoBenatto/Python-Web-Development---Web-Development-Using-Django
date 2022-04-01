# Funções anônimas
contador_letras = lambda lista: [len(x) for x in lista]

soma = lambda a, b: a + b
sub = lambda a, b: a - b

calculadora = {
    'soma': lambda a, b: a + b,
    'sub': lambda a, b: a - b,
    'div': lambda a, b: a / b,
    'mult': lambda a, b: a * b,
    'resto': lambda a, b: a % b,
}

if __name__ == "__main__":
    lista = ["cachorro", "gato", "arara", "lobo", "onça", "leão", "aranha", "tigre", "puma", "elefante"]
    print(contador_letras(lista))

    print(soma(743, 256))
    print(sub(743, 256))

    soma = calculadora['soma']
    sub = calculadora['sub']
    div = calculadora['div']
    mult = calculadora['mult']
    resto = calculadora['resto']

    print(soma(743, 256))
    print(sub(743, 256))
    print(div(743, 256))
    print(mult(743, 256))
    print(resto(743, 256))