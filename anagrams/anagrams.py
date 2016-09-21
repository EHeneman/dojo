"""
https://github.com/thoughtworks-academy/dojo/blob/master/anagrams/en.md

Write a program to generate all potential anagrams of an input string.

For example, the potential anagrams of "biro" are

biro bior brio broi boir bori
ibro ibor irbo irob iobr iorb
rbio rboi ribo riob roib robi
obir obri oibr oirb orbi orib


"""

import itertools

def anagrams(word):
    return ["".join(perm) for perm in itertools.permutations(word)]

if __name__ == '__main__':

    assert len(anagrams('biro')) == 24
    assert len(anagrams('tdd')) == 6
    assert len(anagrams('python')) == 720

    assert 'biro' in anagrams('biro')
    assert 'test' in anagrams('test')
    assert 'tdd' in anagrams('tdd')

    assert 'orib' in anagrams('biro')
    assert 'tset' in anagrams('test')
    assert 'tdd' in anagrams('ddt')
