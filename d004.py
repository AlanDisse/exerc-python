teclado = input('Vamos identificar todas informações sobre o número que você mandou')
print(type(teclado))
print('É alfabético?', teclado.isalpha())
print('É Numérico?', teclado.isnumeric())
print('É alfanumérico?', teclado.isalnum())
print('Está tudo escrito em minúsculo?', teclado.isupper())
print('Está tudo escrito em minúsculo?', teclado.islower())
print('É um número decimal?', teclado.isdecimal())
print('É um identificador?', teclado.isidentifier())
print('Pode ser impresso?', teclado.isprintable())
print('Começa com letras maiúsculas e termina com minúsculas?', teclado.istitle())
print('É um dígito?', teclado.isdigit())
print('Contém apenas espaços?', teclado.isspace())