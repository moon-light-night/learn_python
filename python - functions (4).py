#блок кода
#блок инструкций
def function():
    print('Hello1')
    print('Hello2')
function()
function()
def function2(x):
    return 2 * x
a = function2(5)
print(a)
print(function2(10))
function2(3)
def sum_of_two_numbers(x,y):
    return x + y
a = sum_of_two_numbers(10,5)
print(a)
def function3(x):
    print(x)
    print('skyrim')
    return 3 * x
a = function3(10)
print(a)

name1 = 'Tom'
height1 = 1.8
weight1 = 90

name2 = 'Katy'
height2 = 1.7
weight2 = 60

name3 = 'Bob'
height3 = 2
weight3 = 130

def bmi_calculator(name, height, weight):
    bmi = weight / height **2
    print('Индекс массы тела:' + str(bmi))
    if bmi < 25:
        return name + ' не имеет лишнего веса'
    else:
        return name + ' имеет лишний вес'
bmi1 = bmi_calculator(name1, height1, weight1)
bmi2 = bmi_calculator(name2, height2, weight2)
bmi3 = bmi_calculator(name3, height3, weight3)
print(bmi1)
print(bmi2)
print(bmi3)
    
