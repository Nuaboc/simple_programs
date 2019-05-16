# chapter 4 Comma code

abc = ['a', 'b', 'c', 'd', 'e']

lulu = ['w']

pepe = ['grillo', 'loco']

sate = ['luna', 'sol', 'estrella']

comma = ', '

y = ', and '


def code(lst):
    if len(lst) >= 2:
        out = comma.join(lst[:-1])
        out += y + lst[-1]
        print(out)
    else:
        print(lst[0])


code(abc)

code(lulu)

code(pepe)

code(sate)
