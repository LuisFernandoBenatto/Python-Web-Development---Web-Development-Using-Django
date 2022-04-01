import Aula_7_metodos_funcoes_classes
from Aula_7_metodos_funcoes_classes import Televisao, Classe_Calculadora_2
from Aula_8_contador_de_letras import Contador_de_letras

if __name__ == '__main__':
    televisao = Aula_7_metodos_funcoes_classes.Televisao()
    
    print(televisao.ligada)
    televisao.power()
    print(televisao.ligada)

    print("\n\n") 
    televisao_2 = Televisao()

    print(televisao_2.ligada)
    televisao.power()
    print(televisao_2.ligada)

    print("\n\n") 
    calculadora_2 = Classe_Calculadora_2()

    print(calculadora_2.soma(987, 321),
          calculadora_2.sub(963, 852), 
          calculadora_2.mult(753, 951), 
          calculadora_2.div(369, 123), 
          calculadora_2.resto(487, 263))

    print("\n\n")      
    lista = ["cachorro", "gato", "arara", "lobo", "onça", "leão", "aranha", "tigre", "puma", "elefante"]
    contador = Contador_de_letras()
    print(contador.contador_de_letras(lista))