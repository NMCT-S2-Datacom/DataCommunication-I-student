from itertools import permutations, product
from random import randint

DEC = ('Decimaal', 'd')
HEX = ('Hexadecimaal', '#04x')
BIN = ('Binair', '#010b')

OR = ('Or', '|')
AND = ('And', '&')
NOT = ('Not', '~')
XOR = ('Xor', '^')

format_header = """import unittest

# Zet de gegeven getallen om naar het gevraagde formaat
# Vervang telkens de ... in de tweede parameter door het gevraagde (zie functienaam)
# De prefix 0b duidt een binair getal aan, 0x een hexadecimaal.
# Voor de leesbaarheid kan je binaire getallen groeperen met een _


"""

logical_ops_header = """import unittest

# Voer de volgende logische bewerkingen uit, vervang telkens de ... in de tweede parameter door de oplossing
# Zet het resultaat in hetzelfde formaat (bin/hex) als de opgave
# De prefix 0b duidt een binair getal aan, 0x een hexadecimaal.
# Een '|' is een bitwise OR: een bit in het resultaat is 1 als de overeenkomstige bits in één van de beide operanden 
#  (of allebei) ook 1 zijn.
# Een '&' is een bitwise AND: elke bit in het resultaat is ENKEL 1 als de overeenkomstige bits BEIDE operanden 
#  ook 1 zijn.
# Een '^' is een bitwise XOR: elke bit in het resultaat is de eXclusive OR (XOR) van de overeenkomstige bits in de 
# operanden: allebei gelijk (1 of 0) --> resultaat = 0, beide verschillend (de ene 1, de andere 0) --> resultaat = 1


"""
footer = """

if __name__ == "__main__":
    unittest.main()
"""


def format_mesh(n):
    oef = ''
    for (x, y) in permutations((DEC, HEX, BIN), 2):
        oef += format_conv(x, y, n)
    return oef


def format_conv(x, y, n):
    oef = 'class {a}2{b}(unittest.TestCase):\n'.format(a=x[0][:3], b=y[0][:3])
    vb = 255
    oef += '\tdef test_example(self):\n' \
           '\t\tself.assertEqual({:{a[1]}}, {:{b[1]}})\n\n'.format(vb, vb, a=x, b=y)
    for i in range(n):
        k = randint(2, 254)
        oef += '\tdef test_oef{i}(self):\n\t\tself.assertEqual({k:{a[1]}}, ...)\n\n'.format(k=k, i=i + 1, a=x, b=y)
    oef += '\n'
    return oef.replace('\t', ' ' * 4)


def logical_op(op, fmt, n):
    oef = 'class Test{a}{b}(unittest.TestCase):\n'.format(a=op[0], b=fmt[0][:3])
    vb = 0b11001010, 0b01100011
    oef += '\tdef test_example(self):\n' \
           '\t\tself.assertEqual({j:{fmt}} {op} {k:{fmt}}, {r:{fmt}})\n\n'.format(
        j=vb[0], k=vb[1], fmt=fmt[1], op=op[1], r=eval('{j:{fmt}} {op} {k:{fmt}}'.format(
            j=vb[0], k=vb[1], fmt=fmt[1], op=op[1])))
    for i in range(n):
        j = randint(2, 254)
        k = randint(2, 254)
        oef += '\tdef test_oef{i}(self):\n\t\tself.assertEqual({j:{fmt}} {op} {k:{fmt}}, ...)\n\n'.format(
            j=j, k=k, i=i + 1, fmt=fmt[1], op=op[1])
    oef += '\n'
    return oef.replace('\t', ' ' * 4)


def logical_mesh(n):
    oef = ''
    for (x, y) in product((AND, OR, XOR), (BIN, HEX)):
        oef += logical_op(x, y, n)
    return oef


if __name__ == '__main__':
    # print(header + format_mesh(3) + footer)  # week 1
    # print(header + format_conv(BIN, HEX, 10) + format_conv(HEX, BIN, 10) + footer)  # week 2
    print(logical_ops_header + logical_mesh(4) + footer)  # week 3
