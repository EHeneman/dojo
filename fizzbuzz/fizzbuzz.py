"""
Regras do Fizzbuzz (WTTD)

1. Se a posição for múltiplo de 3: fizz
2. Se a posição for múltiplo de 5: buzz
3. Se a posição for múltiplo de 3 e 5: fizzbuzz
4. Para qualquer outra posição fale o próprio nº.

"""
from functools import partial

multiple_of = lambda base, num: num % base == 0
multiple_of_3 = partial(multiple_of, 3)
multiple_of_5 = partial(multiple_of, 5)


def robot(pos):
    say = str(pos)
    if multiple_of_3(pos) and multiple_of_5(pos):
#    if pos % 3 == 0 and pos % 5 == 0:
        say = 'fizzbuzz'
    elif multiple_of_5(pos):
        say = 'buzz'
    elif multiple_of_3(pos):
        say = 'fizz'

    return say

if __name__ == '__main__':
    assert robot(1) == '1'
    assert robot(2) == '2'
    assert robot(4) == '4'

    assert robot(3) == 'fizz'
    assert robot(6) == 'fizz'
    assert robot(9) == 'fizz'

    assert robot(5) == 'buzz'
    assert robot(10) == 'buzz'
    assert robot(20) == 'buzz'

    assert robot(15) == 'fizzbuzz'
    assert robot(30) == 'fizzbuzz'
    assert robot(45) == 'fizzbuzz'