import unittest

# Voer de volgende logische bewerkingen uit, vervang telkens de ... in de tweede parameter door de oplossing
# Zet het resultaat in hetzelfde formaat (bin/hex) als de opgave
# De prefix 0b duidt een binair getal aan, 0x een hexadecimaal.
# Een '|' is een bitwise OR: een bit in het resultaat is 1 als de overeenkomstige bits in één van de beide operanden
#  (of allebei) ook 1 zijn.
# Een '&' is een bitwise AND: elke bit in het resultaat is ENKEL 1 als de overeenkomstige bits BEIDE operanden
#  ook 1 zijn.
# Een '^' is een bitwise XOR: elke bit in het resultaat is de eXclusive OR (XOR) van de overeenkomstige bits in de
# operanden: allebei gelijk (1 of 0) --> resultaat = 0, beide verschillend (de ene 1, de andere 0) --> resultaat = 1


class TestAndBin(unittest.TestCase):
    def test_example(self):
        self.assertEqual(0b11001010 & 0b01100011, 0b01000010)

    def test_oef1(self):
        self.assertEqual(0b10011111 & 0b11001111, ...)

    def test_oef2(self):
        self.assertEqual(0b00100011 & 0b01000111, ...)

    def test_oef3(self):
        self.assertEqual(0b01110100 & 0b10010100, ...)

    def test_oef4(self):
        self.assertEqual(0b10011001 & 0b01001000, ...)


class TestAndHex(unittest.TestCase):
    def test_example(self):
        self.assertEqual(0xca & 0x63, 0x42)

    def test_oef1(self):
        self.assertEqual(0x99 & 0xb0, ...)

    def test_oef2(self):
        self.assertEqual(0xe1 & 0xc2, ...)

    def test_oef3(self):
        self.assertEqual(0x21 & 0x51, ...)

    def test_oef4(self):
        self.assertEqual(0x55 & 0x76, ...)


class TestOrBin(unittest.TestCase):
    def test_example(self):
        self.assertEqual(0b11001010 | 0b01100011, 0b11101011)

    def test_oef1(self):
        self.assertEqual(0b01010001 | 0b00100101, ...)

    def test_oef2(self):
        self.assertEqual(0b00011001 | 0b01010110, ...)

    def test_oef3(self):
        self.assertEqual(0b10110000 | 0b00001100, ...)

    def test_oef4(self):
        self.assertEqual(0b10000010 | 0b01010011, ...)


class TestOrHex(unittest.TestCase):
    def test_example(self):
        self.assertEqual(0xca | 0x63, 0xeb)

    def test_oef1(self):
        self.assertEqual(0x4f | 0xba, ...)

    def test_oef2(self):
        self.assertEqual(0x07 | 0xc0, ...)

    def test_oef3(self):
        self.assertEqual(0x80 | 0x84, ...)

    def test_oef4(self):
        self.assertEqual(0xce | 0xbd, ...)


class TestXorBin(unittest.TestCase):
    def test_example(self):
        self.assertEqual(0b11001010 ^ 0b01100011, 0b10101001)

    def test_oef1(self):
        self.assertEqual(0b11101010 ^ 0b10010110, ...)

    def test_oef2(self):
        self.assertEqual(0b00011011 ^ 0b00011000, ...)

    def test_oef3(self):
        self.assertEqual(0b00110000 ^ 0b11000010, ...)

    def test_oef4(self):
        self.assertEqual(0b10010011 ^ 0b10101100, ...)


class TestXorHex(unittest.TestCase):
    def test_example(self):
        self.assertEqual(0xca ^ 0x63, 0xa9)

    def test_oef1(self):
        self.assertEqual(0x59 ^ 0x47, ...)

    def test_oef2(self):
        self.assertEqual(0xf9 ^ 0xb9, ...)

    def test_oef3(self):
        self.assertEqual(0xa1 ^ 0xe5, ...)

    def test_oef4(self):
        self.assertEqual(0x4f ^ 0x22, ...)




if __name__ == "__main__":
    unittest.main()
