from decimal import DivisionByZero


class Error(Exception):
    def __init__(self):
        pass

class InputError(Error):
    def __init__(self, message):
        self.message = message

class Personalizar_excecao():
    def __init__(self):
        pass
    def personalizar_excecao(self, lista, contador):
        try: 
            result = sum(lista) / contador
            return result
        except ZeroDivisionError:
            print("Não é possível realizar uma divisao por zero!")

if __name__ == '__main__':
    personalizar_excecao = Personalizar_excecao()

    contador = 0
    lista = []
    while(True):
        try:
            x = int(input("Entre com um valor de 0 a 10: "))
            if(x > 10):
                raise InputError("Valor não pode ser maior do que 10")
            elif(x < 0):
                raise InputError("Valor não pode ser menor do que 0")
            else:
                lista.append(x)
                contador += 1
                print(contador, lista)
        except ValueError:
            print("Valor inválido. Deve-se digitar apenas números!")
            break
        except InputError as ex:
            print(ex)

    print(personalizar_excecao.personalizar_excecao(lista, contador))