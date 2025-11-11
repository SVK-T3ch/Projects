print('Welcome to the 2D Pattern Maker')
print('This program makes various 2D shapes and patterns like diamond,pyramid,etc')
q1 = input('Pick a pattern - \na)Diamond b)Rectangle c)Square d)Pyramid: ')
if q1 == 'c':
    print('The pattern of the shape you picked is the following - ')
    l = 10
    for i in range(l):
        print(' * ' * l)
elif q1 == 'b':
    print('The pattern of the shape you picked is the following - ')
    l = 15
    b = 8
    for i in range(b):
        print(' * ' * l)
elif q1 == 'd':
    print('The pattern of the shape you picked is the following - ')
    b = 20
    for i in range(b):
        print(' ' * (b-i) + '*' * (2*i-1))
elif q1 == 'a':
    print('The pattern of the shape you picked is the following - ')

    b = 12
    for i in range(b):
        print(' ' * (b-i) + '*' * (2*i-1))
    for i in range(b-1,0,-1):
        print(' ' * (b-i) + '*' * (2*i-1))

