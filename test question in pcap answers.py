def foo(x,y,z):
    return x(y) – x(z)

print (foo(lambda x: x % 2, 2, 1) )
