import shutil
import os

class Arquivos:
    def __init__(self):
        pass
    def criar_arquivo(self, nome_arquivo, operacao, texto):
        self.arquivo = open(nome_arquivo, operacao)
        self.arquivo.write(texto)
        self.arquivo.close()
    def atualizar_arquivo(self, nome_arquivo, operacao, novo_texto):
        self.arquivo = open(nome_arquivo, operacao)
        self.arquivo.write(novo_texto)
        self.arquivo.close()
    def ler_arquivo(self, nome_arquivo):
        self.arquivo = open(nome_arquivo, "r")
        conteudo = self.arquivo.read()
        print(conteudo)
        self.arquivo.close()
    def mover_arquivo(self, nome_arquivo, endereco):
        shutil.move(nome_arquivo, endereco)
    def copiar_arquivo(self, nome_arquivo, endereco):
        shutil.copy(nome_arquivo, endereco)
    def remover_arquivo(self, nome_arquivo):
        if(os.path.exists(nome_arquivo)):
            os.remove(nome_arquivo)


class Calcular_media:
    def __init__(self):
        pass
    def media_notas(self, nome_do_arquivo):
        self.arquivo = open(nome_do_arquivo, "r")
        aluno_nota = self.arquivo.read()
        # print(aluno_nota)
        lista_media = []
        aluno_nota = aluno_nota.split("\n")
        for x in aluno_nota:
            lista_notas = x.split(",")
            # print(lista_notas)
            aluno = lista_notas[5]
            # print(aluno)
            y = 0
            while(y < 7): 
                lista_notas.pop(0)
                y += 1
            # print(lista_notas)
            media = lambda notas: sum([float(i) for i in notas]) / 4
            # print(media(lista_notas)) 
            lista_media.append({aluno: media(lista_notas)})
        return lista_media


if __name__ == '__main__':
    arquivo = Arquivos()
    nome_arquivo = "temp/arquivo.txt"
    nome_arquivo_2 = "temp/arquivo_2.txt"
    arquivo.criar_arquivo(nome_arquivo, "w",
        "Minha primeira linha no arquivo! \n" +
        "Minha segunda linha no arquivo! \n" +
        "Lorem ipsum dolor sit amet consectetur adipisicing elit. \n" + 
        "Minus iusto totam adipisci ipsam aliquam, in velit hic vel beatae officia. \n" +
        "Architecto, dolores iste? A amet, dolor culpa quidem deserunt harum? \n\n"
    )
    arquivo.atualizar_arquivo(nome_arquivo, "a", "Atualizando arquivo\n")

    arquivo.ler_arquivo(nome_arquivo)

    # arquivo.copiar_arquivo(nome_arquivo, "C:/Users/Public/Documents")
    # arquivo.mover_arquivo(nome_arquivo, "C:/Users/Public/Downloads")

    arquivo.criar_arquivo(nome_arquivo_2, "w", "test")
    arquivo.remover_arquivo(nome_arquivo_2)

    arquivo_notas = Arquivos()
    nome_arquivo_notas = "temp/notas.txt"
    # alunos_turma_a = [
    #     {
    #         "Codigo":"01",
    #         "RA":"202211113030001",
    #         "Nome":"Patrick",
    #         "Notas":"10, 10, 5.5, 6.7"
    #     }, {
    #         "Codigo":"02",
    #         "RA":"202211113030002",
    #         "Nome":"Eduarda",
    #         "Notas":"9.8, 7.5, 6.3, 5.7"
    #     }
    # ]
    # alunos_turma_b = [
    #     {
    #         "Codigo":"39",
    #         "RA":"202211113030039",
    #         "Nome":"Rafael",
    #         "Notas":"10, 10, 5.5, 6.7"
    #     }, {
    #         "Codigo":"38",
    #         "RA":"202211113030038",
    #         "Nome":"Daniela",
    #         "Notas":"9.8, 7.5, 6.3, 5.7"
    #     }
    # ]
    aluno_1_turma_a = 'Codigo,01,RA,202211113030001,Nome,Patrick,Notas,10,10,5.5,6.7\n'
    aluno_2_turma_a = 'Codigo,02,RA,202211113030002,Nome,Eduarda,Notas,9.8,7.5,6.3,5.7\n'
    aluno_1_turma_b = 'Codigo,39,RA,202211113030039,Nome,Rafael,Notas,10,10,5.5,6.7\n'
    aluno_2_turma_b = 'Codigo,38,RA,202211113030038,Nome,Daniela,Notas,9.8,7.5,6.3,5.7'

    arquivo.criar_arquivo(nome_arquivo_notas, "w", str(aluno_1_turma_a))
    arquivo.atualizar_arquivo(nome_arquivo_notas, "a", str(aluno_2_turma_a))
    arquivo.atualizar_arquivo(nome_arquivo_notas, "a", str(aluno_1_turma_b))
    arquivo.atualizar_arquivo(nome_arquivo_notas, "a", str(aluno_2_turma_b))
    arquivo.ler_arquivo(nome_arquivo_notas)

    media = Calcular_media()
    media.media_notas(nome_arquivo_notas)

    print(media.media_notas(nome_arquivo_notas))