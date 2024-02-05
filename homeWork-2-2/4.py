def foo(name):
    list = []
    for character in name:
        list.append(character)
        
    return list

name = input("enter name:")
print(foo(name))
