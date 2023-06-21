altura = int(input('Qual é a altura da parede (em m)?'))
largura = int(input('Qual é a largura da parede (em m)?'))
area = altura*largura
tinta_area = area/2
print('A área a ser pintada é de {}m, e a quantidade de tinta que você vai precisar é de {}L'.format(area,tinta_area))