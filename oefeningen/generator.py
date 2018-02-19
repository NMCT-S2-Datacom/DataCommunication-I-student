from itertools import permutations
from random import randint

d = ('Decimaal', 'd')
h = ('Hexadecimaal', '#04x')
b = ('Binair', '#010b')

header = """import unittest

# Zet de gegeven getallen om naar het gevraagde formaat
# Vervang telkens de ... in de tweede parameter door het gevraagde (zie functienaam)
# De prefix 0b duidt een binair getal aan, 0x een hexadecimaal.
# Voor de leesbaarheid kan je binaire getallen groeperen met een _
# De derde parameter dient enkel om je fouten makkelijker te vinden en kan je dus best laten staan


"""

footer = """
if __name__ == "__main__":
    unittest.main()
"""


def mesh(n):
    oef = ''
    for (x, y) in permutations((d, h, b), 2):
        oef += duo(x, y, n)
    return oef


def duo(x, y, n):
    oef = 'class {a}2{b}(unittest.TestCase):\n'.format(a=x[0][:3], b=y[0][:3])
    vb = 255
    oef += '\tdef test_example(self):\n' \
           '\t\tself.assertEquals({:{a[1]}}, {:{b[1]}})\n\n'.format(vb, vb, a=x, b=y)
    for i in range(n):
        k = randint(2, 254)
        oef += '\tdef test_oef{i}(self):\n\t\tself.assertEquals({k:{a[1]}}, ...)\n\n'.format(k=k, i=i + 1, a=x, b=y)
    oef += '\n'
    return oef.replace('\t', ' '*4)


if __name__ == '__main__':
    # print(header + mesh(3) + footer)  # week 1
    print(header + duo(b, h, 10) + duo(h, b, 10) + footer)  # week 2
