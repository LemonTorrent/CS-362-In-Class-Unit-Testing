def add(a, b):
    print(a, "+", b, "=", a+b)
    return a + b

def sub(a, b):
    print(a, "-", b, "=", a-b)
    return a - b

def mul(a, b):
    print(a, "*", b, "=", a*b)
    return a * b

def div(a, b):
    print(a, "/", b, "=", a/b)
    return a / b

def errorHandle(a, b):
    print("a is int:", type(a)== int)
    print("b is int:", type(b)== int)
    return (type(a)== int and type(b)== int)
