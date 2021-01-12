"""
A code that develop the Fibonacci sequence.

Each number in the sequence is the sum of the two numbers that precede it.
"""
print('type a number:')
num = int(input())


def fibonacci(n):
    """
    Each number in the sequence is the sum of the two numbers that precede it.

    Example: For 10 numbers, starting from 0;
            returns 0, 1, 2, 5, 8, 13, 21, 34

    :param n: is an input from the user, it should be a number
    :return: a sequence based in the Fibonacci sequence.
    """
    if n <= 1:
        return list(range(2))
    else:
        for i in range(n):
            list(i)


fibonacci(num)
