from locale import setlocale, currency, LC_MONETARY

setlocale(LC_MONETARY, 'pt_BR.UTF-8')

while True:
  try:
    hourValue = input('Quanto você ganha por hora: ')
    hourValue = float(hourValue.replace(',', '.'))
    quantityHourPerMonth = int(input('Quantas horas você trabalha por mês: '))
    break
  except ValueError:
    print('''Por favor, digite os valores corretos...
Use somente um ponto pra centavo no valor da hora''')   
    continue

total = hourValue * quantityHourPerMonth
incomeTax = (total * 11) / 100
inss = (total * 8) / 100
syndicate = (total * 5) / 100
discounts = incomeTax + inss + syndicate

print(F'''
Salário Bruto           : {currency(total)}
IR (11%)                : {currency(incomeTax)}
INSS (8%)               : {currency(inss)}
Sindicato (5%)          : {currency(syndicate)}
Salário Líquido         : {currency(total - discounts)}''')