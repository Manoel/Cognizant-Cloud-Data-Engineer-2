# Data e Hora
# date traz a data atual
# strftime('%d/%m/%Y') traz a data formatada em dia mes ano
# datetime traz a data e hora atual
# timedelta traz a diferença entre duas datas

from datetime import date, time, datetime, timedelta

def trabalhando_com_datetime():
    data_atual = datetime.now()
    print(data_atual)
    print(type(data_atual))
    data_atual_str = data_atual.strftime('%d/%m/%y')
    data_atual_str = data_atual.strftime('%H:%M:%S')
    data_atual_str = data_atual.strftime('%d/%m/%y %H: %M: %S')
    data_atual_str = data_atual.strftime('%c')
    print(data_atual_str)
    print(type(data_atual_str))
    print(data_atual.day)
    print(data_atual.month)
    print(data_atual.year)
    print(data_atual.weekday())
    tupla = ('Segunda', 'Terça', 'Quarta', 'Quinta', 'Sexta', 'Sabado', 'Domingo')
    print(tupla[data_atual.weekday()])
    data_criada = datetime(2018, 6, 20, 15, 30, 20) # data crida com os parametros ano, mes, dia, hora, minuto, segundo
    print(data_criada)
    print(data_criada.strftime('%c'))
    data_string = '01/01/2019 12:20:22'
    data_convertida = datetime.strptime(data_string, '%d/%m/%Y %H:%M:%S')
    print(data_convertida)
    nova_data = data_convertida - timedelta(days=365, hours=2, minutes=15)

def trabalhando_com_date():

    data_atual = date.today()
    #print(data_atual.strftime('%d/%m/%Y'))
    #print(data_atual.strftime('%A %B %Y'))
    data_atual_str = data_atual.strftime('%A %B %Y')
    print(type(data_atual)) # <class 'datetime.date'> desta forma é possível acessar os metodos da função date
    print(data_atual_str)
    print(type(data_atual_str)) # <class 'str'> desta forma não é possível acessar os metodos da função str

def trabalhando_com_time():
    horario = time(hour=15, minute=18, second=30)
    print(horario)
    print(type(horario))
    horario_str = horario.strftime('%H:%M:%S')
    print(horario_str)
    print(type(horario_str))

if __name__ == '__main__':
    #trabalhando_com_date()
    #trabalhando_com_time()
    trabalhando_com_datetime()

