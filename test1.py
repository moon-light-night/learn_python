
l = [1,2,3,4,'skyrim']
c = 'skyrim is the most popular game in the world'

for element in l:
    print(element)
    print(l,c)
    if isinstance(element,str):
        for char in element:
            print(char)
            print(element)
            print(l,c)

print(element,char)
            





