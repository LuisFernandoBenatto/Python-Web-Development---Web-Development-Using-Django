class Forcando_excecoes:
    def __init__(self):
        pass
    def forcando_excecoes(self, indice, a):
        lista = [0, 1, 2, 3]
        try:
            numero = lista[indice] #IndexError: list index out of range
            x = a  #NameError: name 'a' is not defined
        except IndexError:
            print("Erro ao acessar um indice inválido da lista!!!")
        # except NameError: 
        #     print("Erro, variavel não definida!")
        except BaseException as ex:
            print("Erro desconhecido. Erro: {}".format(ex))
        else: 
            print("Executa quando não ocerre nenhuma exceção")
        finally: 
            print("Sempre executa!!!")
        return numero, x
    def forcando_excecoes_divisao(self, dividendo, divisor):
        try:
            quociente  = dividendo / divisor
        except ZeroDivisionError:
            print("Não é possível realizar uma divisao por zero!")
        else: 
            print("Executa quando não ocerre nenhuma exceção!")
        finally: 
            print("Sempre executa!!!")
        return quociente #ZeroDivisionError: division by zero

class Forcando_excecoes_em_arquivos:
    def __init__(self):
        pass
    def excecoes_em_arquivos(self):
        try:
            self.arquivo = open("temp/arquivo.txt", "r")
            self.arquivo.write("Texto que não será gravado, pois esta apenas lendo o arquivo e não escrevendo")
            self.arquivo.close()
        except Exception as ex:
            print("Erro: {}".format(ex))
        else: 
            print("Nenhuma excecoes ocorrida!")
        finally:
            self.arquivo.close()

if __name__ == '__main__':
    excecoes = Forcando_excecoes()
    # print(excecoes.forcando_excecoes_divisao(30, 0)) #ZeroDivisionError: division by zero
    print(excecoes.forcando_excecoes_divisao(30, 5)) 
    # print(excecoes.forcando_excecoes(4)) #IndexError: list index out of range
    print(excecoes.forcando_excecoes(0, 5)) 

    excecoes_arquivo = Forcando_excecoes_em_arquivos()
    excecoes_arquivo.excecoes_em_arquivos()