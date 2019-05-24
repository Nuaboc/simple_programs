# chapter 4 Comma code

abc = ['a', 'b', 'c', 'd', 'e']

lulu = ['w']

pepe = ['grillo', 'loco']

sate = ['luna', 'sol', 'estrella']

comma = ', '

y = ', and '


def join(lst):
    if len(lst) >= 2:
        out = comma.join(lst[:-1])
        out += y + lst[-1]
        print(out)
    else:
        print(lst[0])


join(abc)

join(lulu)

join(pepe)

join(sate)

print('....................................................')

# Solution 2


def add(string):
    return string


def code(lst):
    if len(lst) >= 2:
        out = ' '
        for i in lst[:-1]:
            out += i + ', '
        out += add('and ') + lst[-1]
        print(out)
    else:
        print(lst)


code(abc)

code(lulu)

code(pepe)

code(sate)
