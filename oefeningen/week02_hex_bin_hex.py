import unittest


# Zet de gegeven getallen om naar het gevraagde formaat
# Vervang telkens de ... in de tweede parameter door het gevraagde (zie functienaam)
# De prefix 0b duidt een binair getal aan, 0x een hexadecimaal.
# Voor de leesbaarheid kan je binaire getallen groeperen met een _
# De derde parameter dient enkel om je fouten makkelijker te vinden en kan je dus best laten staan

class Bin2Hex(unittest.TestCase):
    def test_example(self):
        self.assertEquals(0b11111111, 0xff)

    def test_oef1(self):
        self.assertEquals(0b00110110, ...)

    def test_oef2(self):
        self.assertEquals(0b11110101, ...)

    def test_oef3(self):
        self.assertEquals(0b00000011, ...)

    def test_oef4(self):
        self.assertEquals(0b01000110, ...)

    def test_oef5(self):
        self.assertEquals(0b01011100, ...)

    def test_oef6(self):
        self.assertEquals(0b11010010, ...)

    def test_oef7(self):
        self.assertEquals(0b00101001, ...)

    def test_oef8(self):
        self.assertEquals(0b11010101, ...)

    def test_oef9(self):
        self.assertEquals(0b00010011, ...)

    def test_oef10(self):
        self.assertEquals(0b00010010, ...)


class Hex2Bin(unittest.TestCase):
    def test_example(self):
        self.assertEquals(0xff, 0b11111111)

    def test_oef1(self):
        self.assertEquals(0x04, ...)

    def test_oef2(self):
        self.assertEquals(0x67, ...)

    def test_oef3(self):
        self.assertEquals(0xb1, ...)

    def test_oef4(self):
        self.assertEquals(0x9f, ...)

    def test_oef5(self):
        self.assertEquals(0xf0, ...)

    def test_oef6(self):
        self.assertEquals(0x7c, ...)

    def test_oef7(self):
        self.assertEquals(0x0b, ...)

    def test_oef8(self):
        self.assertEquals(0xe8, ...)

    def test_oef9(self):
        self.assertEquals(0x75, ...)

    def test_oef10(self):
        self.assertEquals(0xce, ...)


if __name__ == "__main__":
    unittest.main()
