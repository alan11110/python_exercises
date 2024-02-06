from datetime import datetime


date = '05 February 2022'

string_to_date = datetime.strptime(date,'%d %B %Y') #transforma a string em formato data

data_formatada = string_to_date.strftime('%y-%m-%d')#formatar a string recem transfomada em data da maneira desejada
print(data_formatada)