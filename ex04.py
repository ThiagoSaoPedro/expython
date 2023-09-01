n = input('Digite algo')

print(type(n))
print('string?', n.isalpha())
print('numero?', n.isnumeric())
print('alfanumérico?', n.isalnum())
print('maiusculo?', n.isupper())
print('minusculo?', n.islower())
print('capitalizada?', n.istitle())