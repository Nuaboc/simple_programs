# chapter 4 Comma code trying solution 2

abc = ['a', 'b', 'c', 'd']

comma = ', '

y = ' and '


def add(string):
    return string


def code(lst):
    if len(lst) >= 2:
        out = ' '
        for i in lst[:-1]:
            out += i + ', '
        out += add(' and ') + lst[-1]
        print(out)
    else:
        print(lst)


code(abc)
