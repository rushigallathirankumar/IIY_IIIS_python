def add():
    x = int(input())
    y = int(input())
    return x+y
def sub():
    x = int(input())
    y = int(input())
    return x-y
def mul():
    x = int(input())
    y = int(input())
    return x*y
def div():
    x = int(input())
    y = int(input())
    if y==0:
       return "error"
    return x/y

print(add())
print(sub())
print(mul())
print(div())



