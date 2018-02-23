import unittest

# Zet de gegeven getallen om naar het gevraagde formaat
# Vervang telkens de ... in de tweede parameter door het gevraagde (zie naam klasse)
# De prefix 0b duidt een binair getal aan, 0x een hexadecimaal.
# Voor de leesbaarheid kan je binaire getallen groeperen met een _
# De derde parameter dient enkel om je fouten makkelijker te vinden en kan je dus best laten staan


class Dec2Hex(unittest.TestCase):
    def test_example(self):
        self.assertEquals(255, 0xff)

    def test_oef1(self):
        self.assertEquals(220, 0xdc)

    def test_oef2(self):
        self.assertEquals(64, ...)

    def test_oef3(self):
        self.assertEquals(18, ...)


class Dec2Bin(unittest.TestCase):
    def test_example(self):
        self.assertEquals(255, 0b11111111)

    def test_oef1(self):
        self.assertEquals(55, ...)

    def test_oef2(self):
        self.assertEquals(151, ...)

    def test_oef3(self):
        self.assertEquals(103, ...)


class Hex2Dec(unittest.TestCase):
    def test_example(self):
        self.assertEquals(0xff, 255)

    def test_oef1(self):
        self.assertEquals(0x4b, ...)

    def test_oef2(self):
        self.assertEquals(0x9a, ...)

    def test_oef3(self):
        self.assertEquals(0x7c, ...)


class Hex2Bin(unittest.TestCase):
    def test_example(self):
        self.assertEquals(0xff, 0b11111111)

    def test_oef1(self):
        self.assertEquals(0x80, ...)

    def test_oef2(self):
        self.assertEquals(0x38, ...)

    def test_oef3(self):
        self.assertEquals(0x74, ...)


class Bin2Dec(unittest.TestCase):
    def test_example(self):
        self.assertEquals(0b11111111, 255)

    def test_oef1(self):
        self.assertEquals(0b10010011, ...)

    def test_oef2(self):
        self.assertEquals(0b10111001, ...)

    def test_oef3(self):
        self.assertEquals(0b00001011, ...)


class Bin2Hex(unittest.TestCase):
    def test_example(self):
        self.assertEquals(0b11111111, 0xff)

    def test_oef1(self):
        self.assertEquals(0b01110101, ...)

    def test_oef2(self):
        self.assertEquals(0b10010010, ...)

    def test_oef3(self):
        self.assertEquals(0b01011100, ...)


if __name__ == "__main__":
    unittest.main()

