code = 25
print(code > 10 and code < 30)
print(code > 30)
print(not code > 25)

code = 10
if code > 10:
    print('it greater than 10')

elif code == 10:
    print('it is 10')

else:
    print('it less than 10')

weight = float(input())
unit = input('Is it in (K)g or (L)bs').upper()

if unit == 'K':
    weight = weight/.45
    print(str(weight) + 'bs')

else:
    weight = weight * .45
    print(str(weight) + 'kg')

