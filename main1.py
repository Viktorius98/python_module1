per_cent = {'ТКБ': 5.6, 'СКБ': 5.9, 'ВТБ': 4.28, 'СБЕР': 4.0}
money = int(input("Введите сумму:"))
TKB = money * (per_cent.get('ТКБ')/100)
SKB = money * (per_cent.get('СКБ')/100)
VTB = money * (per_cent.get('ВТБ')/100)
SBER = money * (per_cent.get('СБЕР')/100)
deposit = ([round(TKB), round(SKB), round(VTB), round(SBER)])

str1 = "deposit ="
print(str1, ', '.join(map(str, [deposit])))

str2 = "Максимальная сумма, которую вы можете заработать -"
print(str2, max(deposit))