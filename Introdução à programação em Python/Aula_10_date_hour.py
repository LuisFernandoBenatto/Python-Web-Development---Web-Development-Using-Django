from datetime import date, datetime, time, timedelta

class Calcular_execucao:
    def __init__(self):
        pass
    def calculo_execucao(self):
        inicio = datetime.now()
        inicio_minute = inicio.minute
        inicio_second= inicio.second
        inicio_microsecond = inicio.microsecond
        return inicio_minute, inicio_second, inicio_microsecond

class Date_:
    def __init__(self):
        pass
    def data_atual(self):
        dataAtual = date.today()
        return dataAtual
        # return dataAtual.strftime("%d/%m/%Y")
    def data_atual_str(self):
        dataAtualStr = date.today()
        return dataAtualStr.strftime("%A %B %Y")

class Date_Time_:
    def __init__(self):
        pass
    def data_hora_atual(self):
        dataHoraAtual = datetime.today()
        return dataHoraAtual
    def data_hora_atual_str(self):
        dataHoraAtualStr = datetime.today()
        return dataHoraAtualStr.strftime("%d/%m/%Y %H:%M:%S")
    def data_hora_atual_(self):
        dataHoraAtual = datetime.today()
        return dataHoraAtual.strftime("%c")
    def test_date_time(self):
        data_atual = datetime.now()
        print(data_atual.date())
        print(data_atual.hour)
        print(data_atual.minute)
        print(data_atual.second)
        print(data_atual.microsecond)
        print(data_atual.day)
        print(data_atual.month)
        print(data_atual.year)
        print(data_atual.weekday())
        tupla = ("Segunda", "Terça", "Quarta", "Quinta", "Sexta", "Sabado", "Domingo")
        print(tupla[data_atual.weekday()])
        print(data_atual.isoweekday())
        tupla_2 = ("Domingo", "Segunda", "Terça", "Quarta", "Quinta", "Sexta", "Sabado")
        print(tupla_2[data_atual.isoweekday()])
    def criar_data(self, ano, mes, dia, horas, minutos, segundos):
        data_criada = datetime(ano, mes, dia, horas, minutos, segundos)
        print(data_criada)
        print(data_criada.strftime("%c"))
    def converter_data(self, data_string = "01/01/2022 10:10:22"):
        data_convertida = datetime.strptime(data_string, "%d/%m/%Y %H:%M:%S")
        print(type(data_convertida))
        return data_convertida

class Time_:
    def __init__(self):
        pass
    def hora_atual(self):
        criandoHorario = time(hour=15, minute=10, second=30)
        return criandoHorario
    def hora_atual_str(self):
        criandoHorarioStr = time(hour=15, minute=10, second=30)
        return criandoHorarioStr.strftime('%H : %M : %S')

class Time_Delta:
    def __init__(self):
        pass
    def time_delta(self, quant_dias, quant_horas, quant_minutos, quant_segundos, quant_milessegundos):
        data_atual = datetime.now()
        nova_data = data_atual - timedelta(days = quant_dias, hours = quant_horas, minutes = quant_minutos)
        nova_data_2 = data_atual + timedelta(hours = quant_horas, minutes = quant_minutos, seconds = quant_segundos, microseconds = quant_milessegundos)
        return nova_data, nova_data_2

if __name__ == "__main__":
    calculo_execucao_ = Calcular_execucao()
    print(calculo_execucao_.calculo_execucao())
    tupla_1 = calculo_execucao_.calculo_execucao()

    print("\n")
    date_ = Date_()
    print(date_.data_atual())
    print(date_.data_atual_str())

    print("\n")
    date_time_ = Date_Time_()    
    print(date_time_.data_hora_atual())
    print(date_time_.data_hora_atual_str())
    print(date_time_.data_hora_atual_())
    date_time_.test_date_time()
    date_time_.criar_data(2030, 3, 13, 1, 56, 37)
    print(date_time_.converter_data("20/01/2022 12:20:22"))

    print("\n")
    time_ = Time_()
    print(time_ .hora_atual())
    print(time_ .hora_atual_str())

    print("\n")
    time_delta_ = Time_Delta()
    print(time_delta_.time_delta(365, 2, 40, 35, 1000))

    print("\n")
    calculo_execucao_2 = Calcular_execucao()
    print(calculo_execucao_2.calculo_execucao())
    tupla_2 = calculo_execucao_2.calculo_execucao()

    list_1 = list(tupla_1)
    list_2 = list(tupla_2)
    print("Diferença dos Segundos: {}".format(list_2[1] - list_1[1]))
    print("Diferença dos Milessegundos: {}".format(list_2[2] - list_1[2]))