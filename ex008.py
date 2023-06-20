#Desenvolva um programa que leia uma distância em metros e mostre os valores relativos em outras medidas.
#20/06/2023
#HALLAN VICTOR PEREIRA DE ALMEIDA
valor_num = float(input('Digite uma distância (em m):'))
km = valor_num/1000
hm = valor_num/100
dam = valor_num/10
dm = valor_num*10
cm = valor_num*100
mm = valor_num*100
print('A distância de', str(valor_num) + 'm corresponde a:')
print(str(km) + 'km')
print(str(hm) + 'hm')
print(str(dam) + 'dam')
print(str(dm) + 'dm')
print(str(cm) + 'cm')
print(str(mm) + 'mm')

