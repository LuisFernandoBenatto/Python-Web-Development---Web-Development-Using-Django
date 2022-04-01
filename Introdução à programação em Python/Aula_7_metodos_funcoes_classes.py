class Classe_Calculadora:
    # print("Função tem retono explícito!")
    def __init__(self, num1, num2):
        self.valor_a = num1
        self.valor_b = num2
    def soma(self):
        return self.valor_a + self.valor_b
    def sub(self):
        return self.valor_a - self.valor_b
    def div(self):
        return self.valor_a / self.valor_b
    def mult(self):
        return self.valor_a * self.valor_b
    def resto(self):
        return self.valor_a % self.valor_b

class Classe_Calculadora_2:
    def __init__(self):
        pass

    def soma(self, valor_a, valor_b):
        return valor_a + valor_b
    def sub(self, valor_a, valor_b):
        return valor_a - valor_b
    def div(self, valor_a, valor_b):
        return valor_a / valor_b
    def mult(self, valor_a, valor_b):
        return valor_a * valor_b
    def resto(self, valor_a, valor_b):
        return valor_a % valor_b

class Televisao:
    # print("Métodos não tem um retorno explícito!")      
    def __init__(self):
        self.ligada = False
        self.canal = 1
    def power(self):
        if(self.ligada):
            self.ligada = False
        else:
            self.ligada = True
    def trocar_canal(self):
        if(self.ligada):
            self.canal += 1
            if(self.canal > 30):
                self.canal = 1
        else:
            print("Televisão desligada")
    def voltar_canal(self):
        if(self.ligada):
            self.canal -= 1
            if(self.canal < 1):
                self.canal = 30
        else:
            print("Televisão desligada")

if __name__ == '__main__':
    calculadora = Classe_Calculadora(890, 132)

    print(calculadora.soma(),
          calculadora.sub(), 
          calculadora.mult(), 
          calculadora.div(), 
          calculadora.resto())

    calculadora_2 = Classe_Calculadora_2()

    print(calculadora_2.soma(987, 321),
          calculadora_2.sub(963, 852), 
          calculadora_2.mult(753, 951), 
          calculadora_2.div(369, 123), 
          calculadora_2.resto(487, 263))

    televisao = Televisao()
    print("Televisão está ligada: {}".format(televisao.ligada))
    televisao.power()
    print("Televisão está ligada: {}".format(televisao.ligada))
    televisao.power()
    print("Televisão está ligada: {}".format(televisao.ligada))
    televisao.power()
    print("Televisão está ligada: {}".format(televisao.ligada))

    print("Televisão está em qual canal: {}".format(televisao.canal))
    televisao.trocar_canal()
    televisao.trocar_canal()
    televisao.trocar_canal()
    print("Televisão está em qual canal: {}".format(televisao.canal))
    televisao.voltar_canal()
    televisao.voltar_canal()
    televisao.voltar_canal()
    televisao.voltar_canal()
    televisao.voltar_canal()
    print("Televisão está em qual canal: {}".format(televisao.canal))