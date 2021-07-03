a = 'Conditional statements'
print(a)
b = 1
c = 2
print('b = 1')
print('c = 2')
if c > b:
    print('c больше, чем b')
if b < c:
    print('b меньше, чем c')
print('вне блока if')
d = 3
e = 5
print('d = 3')
print('e = 5')
if d < e:
    print('d меньше, чем e')
else:
    print('либо d > e')
    print('либо d = e')
f = 20
g = 8
if f < g:
    print("f меньше, чем g")
elif f == g:
    print("f равняется g")
elif f > g + 10:
    print('разница между f и g больше 10')
else:
    print("f больше g")
e = 10
h = 10
if e < h:
    print('e меньше, чем h')
else:
    if e == h:
        print('e равняется h')
    else:
        print('e больше, чем h')
name = 'Tom'
height = 1.92
weight = 104
bmi = weight / (height ** 2)
print('индекс массы тела:' + str(bmi))
if bmi < 25:
    print('У ' + name + ' нет лишнего веса')
else:
    print('У ' + name + ' есть лишний вес')
my_bool = 10 < 15
print(my_bool)




