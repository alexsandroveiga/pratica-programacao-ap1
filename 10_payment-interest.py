from locale import setlocale, currency, LC_MONETARY

setlocale(LC_MONETARY, 'pt_BR.UTF-8')

interestPerDay = 0.1
mulct = 3
installmentQuantityReport = []
installmentValueToPayReport = []

def valorPagamento(value: float, delayedDays: int):
  mulctValue = (value * mulct) / 100
  interestValue = 0
  for x in range(0, delayedDays):
    interestValue += (value * interestPerDay) / 100
  total = value + mulctValue + interestValue
  installmentValueToPayReport.append(total)
  installmentQuantityReport.append(delayedDays)
  return currency(total)

while True:
  try:
    installmentValue = input('Digite o valor da prestação: ')
    installmentValue = float(installmentValue.replace(',', '.'))
    delayedDays = int(input('Digite a quantidade de dias em atraso: '))
    if delayedDays <= 0:
      break
    print(F'Valor do pagamento: {valorPagamento(installmentValue, delayedDays)}')
  except ValueError:
    print('Digite o valor correto, use vírgula ou ponto somente para centavos...')
    continue

print(F'''
Relatório do dia
Quantidade de parcelas pagas: {sum(installmentQuantityReport)}
Valor total de prestações pagas: {currency(sum(installmentValueToPayReport))}''')