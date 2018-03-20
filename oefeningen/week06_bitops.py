import unittest


# Gebruik bitoperaties om volgende functies te vervolledigen:


def set_bit_0(value):
    """ Set bit 0 of <value>

    :param value: any integer
    :return: same integer with bit 0 = 1
    """
    return value | 1


def set_bit_3(value):
    """ Set bit 3 of <value>

    :param value: any integer
    :return: same integer with bit 3 = 1
    """
    return value | 1 << 3


def toggle_bit_5(value):
    """ Toggle bit 5 of <value>

    :param value: any integer
    :return: same integer with bit 5 = not bit 5
    """
    return value ^ 1 << 5


def clear_bit_16(value):
    """ Clear bit 16 of <value>

    :param value: any integer
    :return: same integer with bit 16 = 0
    """
    return value & ~(1 << 16)


def set_bit(n, value):
    """
    Set bit <n> in <value>
    :param n: the bit to set (0-based)
    :param value: the value to modify
    :return: same value with bit <n> = 1
    """

    return value | 1 << n


def toggle_bit(n, value):
    """
    Toggle bit <n> in <value>
    :param n: the bit to toggle (0-based)
    :param value: the value to modify
    :return: same value with bit <n> = not bit <n>
    """
    return value ^ 1 << n


def clear_bit(n, value):
    """
    Clear bit <n> in <value>
    :param n: the bit to clear (0-based)
    :param value: the value to modify
    :return: same value with bit <n> = 0
    """
    return value & ~(1 << n)


def byte_complement(value):
    """
    Return the byte_complement (bitwise NOT) of byte <value>
    :param value: any 8-bit integer
    :return: the byte_complement (inverse) of <value>
    """
    if value > 0xff:
        raise ValueError("Bytes only please")
    return ~value & 0xff


def make_word(byte1, byte0):
    """
    Makes a 16-bit word out of 2 bytes
    :param byte1: MSByte
    :param byte0: LSByte
    :return: 16-bit value made by appending byte0 to byte1
    """
    return byte1 << 8 | byte0


def make_dword(byte3, byte2, byte1, byte0):
    """
    Make a 32-bit doubleword out of 4 bytes
    :param byte3: MSByte
    :param byte2: next byte
    :param byte1: next byte
    :param byte0: LSByte
    :return: 16-bit value made by appending bytes 0 through 3
    """
    return byte3 << 24 | byte2 << 16 | byte1 < 8 | byte0


# Little & big endian: https://en.wikipedia.org/wiki/Endianness
def join_bytes_little_endian(values):
    """
    Joins the little endian bytes in <values> to a single value
    :param values: bytes, little endian
    :return: n-bit value made by appending byte0 to byte1
    """
    value = 0
    for i in range(len(values)):
        value |= values[i] << 8 * i
    return value


def join_bytes_big_endian(values):
    """
    Joins the big endian bytes in <values> to a single value
    :param values: bytes, big endian
    :return: 16-bit value made by appending byte0 to byte1
    """
    value = 0
    stop = len(values)
    for i in range(stop):
        value |= values[stop - i] << 8 * i
    return value


############################################
# ----- DO NOT EDIT BEYOND THIS LINE ----- #
############################################

class TestSingleBit(unittest.TestCase):
    def test_set_bit_0(self):
        self.assertEqual(1, set_bit_0(0))
        self.assertEqual(3, set_bit_0(3))
        self.assertEqual(5, set_bit_0(4))
        self.assertEqual(255, set_bit_0(254))
        self.assertEqual(511, set_bit_0(511))
        self.assertEqual(1023, set_bit_0(1022))
        self.assertEqual(1025, set_bit_0(1024))

    def test_set_bit_3(self):
        self.assertEqual(24, set_bit_3(16))
        self.assertEqual(13, set_bit_3(5))
        self.assertEqual(14, set_bit_3(6))
        self.assertEqual(8, set_bit_3(0))
        self.assertEqual(13, set_bit_3(5))
        self.assertEqual(11, set_bit_3(3))
        self.assertEqual(8, set_bit_3(0))
        self.assertEqual(26, set_bit_3(18))
        self.assertEqual(15, set_bit_3(7))
        self.assertEqual(63563, set_bit_3(63555))
        self.assertEqual(1706, set_bit_3(1698))
        self.assertEqual(5372, set_bit_3(5364))
        self.assertEqual(41071, set_bit_3(41063))
        self.assertEqual(24, set_bit_3(16))
        self.assertEqual(3582, set_bit_3(3574))
        self.assertEqual(25183, set_bit_3(25175))
        self.assertEqual(26152, set_bit_3(26144))
        self.assertEqual(15465, set_bit_3(15457))
        self.assertEqual(20845, set_bit_3(20837))

    def test_toggle_bit_5(self):
        self.assertEqual(54645, toggle_bit_5(54613))
        self.assertEqual(15443, toggle_bit_5(15475))
        self.assertEqual(25111, toggle_bit_5(25143))
        self.assertEqual(27136, toggle_bit_5(27168))
        self.assertEqual(3499, toggle_bit_5(3467))
        self.assertEqual(45866, toggle_bit_5(45834))
        self.assertEqual(39792, toggle_bit_5(39760))
        self.assertEqual(39480, toggle_bit_5(39448))
        self.assertEqual(58117, toggle_bit_5(58149))
        self.assertEqual(27570, toggle_bit_5(27538))
        self.assertEqual(17668, toggle_bit_5(17700))
        self.assertEqual(12716, toggle_bit_5(12684))
        self.assertEqual(56283, toggle_bit_5(56315))
        self.assertEqual(40757, toggle_bit_5(40725))
        self.assertEqual(51887, toggle_bit_5(51855))
        self.assertEqual(49959, toggle_bit_5(49927))
        self.assertEqual(54738, toggle_bit_5(54770))
        self.assertEqual(9877, toggle_bit_5(9909))
        self.assertEqual(24316, toggle_bit_5(24284))
        self.assertEqual(28696, toggle_bit_5(28728))

    def test_clear_bit_16(self):
        self.assertEqual(5664768, clear_bit_16(5664768))
        self.assertEqual(12891441, clear_bit_16(12956977))
        self.assertEqual(9318290, clear_bit_16(9318290))
        self.assertEqual(12202117, clear_bit_16(12267653))
        self.assertEqual(14725381, clear_bit_16(14790917))
        self.assertEqual(10755268, clear_bit_16(10820804))
        self.assertEqual(12493823, clear_bit_16(12493823))
        self.assertEqual(1473206, clear_bit_16(1473206))
        self.assertEqual(15264395, clear_bit_16(15264395))
        self.assertEqual(14592415, clear_bit_16(14592415))
        self.assertEqual(11039773, clear_bit_16(11105309))
        self.assertEqual(1053807, clear_bit_16(1053807))
        self.assertEqual(2675372, clear_bit_16(2675372))
        self.assertEqual(13007472, clear_bit_16(13073008))
        self.assertEqual(6180151, clear_bit_16(6245687))
        self.assertEqual(15346948, clear_bit_16(15346948))
        self.assertEqual(14563446, clear_bit_16(14563446))
        self.assertEqual(2790554, clear_bit_16(2790554))
        self.assertEqual(6708015, clear_bit_16(6773551))
        self.assertEqual(8971848, clear_bit_16(8971848))
        self.assertEqual(1066275, clear_bit_16(1131811))
        self.assertEqual(3549852, clear_bit_16(3549852))
        self.assertEqual(16671572, clear_bit_16(16737108))
        self.assertEqual(5281512, clear_bit_16(5281512))
        self.assertEqual(8165373, clear_bit_16(8165373))
        self.assertEqual(14465117, clear_bit_16(14465117))
        self.assertEqual(4998428, clear_bit_16(5063964))
        self.assertEqual(4110515, clear_bit_16(4110515))
        self.assertEqual(16029831, clear_bit_16(16095367))
        self.assertEqual(4228636, clear_bit_16(4294172))


class TestAnyBit(unittest.TestCase):
    def test_clear(self):
        self.assertEqual(99704, clear_bit(17, 99704))
        self.assertEqual(842184, clear_bit(23, 842184))
        self.assertEqual(293367, clear_bit(19, 293367))
        self.assertEqual(2213, clear_bit(13, 2213))
        self.assertEqual(227787, clear_bit(20, 227787))
        self.assertEqual(219383, clear_bit(18, 219383))
        self.assertEqual(0, clear_bit(6, 64))
        self.assertEqual(786, clear_bit(11, 786))
        self.assertEqual(3504, clear_bit(14, 3504))
        self.assertEqual(1243, clear_bit(11, 1243))
        self.assertEqual(460, clear_bit(9, 460))
        self.assertEqual(247, clear_bit(9, 247))
        self.assertEqual(37347, clear_bit(16, 37347))
        self.assertEqual(75, clear_bit(7, 75))
        self.assertEqual(321, clear_bit(9, 321))
        self.assertEqual(3307589, clear_bit(24, 3307589))
        self.assertEqual(155, clear_bit(10, 155))
        self.assertEqual(6022, clear_bit(14, 6022))
        self.assertEqual(112920, clear_bit(17, 112920))
        self.assertEqual(1211211, clear_bit(21, 1211211))
        self.assertEqual(83, clear_bit(7, 83))
        self.assertEqual(3233009, clear_bit(22, 3233009))
        self.assertEqual(287, clear_bit(9, 287))
        self.assertEqual(7992, clear_bit(14, 7992))
        self.assertEqual(37963, clear_bit(19, 37963))
        self.assertEqual(1745453, clear_bit(21, 1745453))
        self.assertEqual(1519816, clear_bit(21, 1519816))
        self.assertEqual(2337176, clear_bit(23, 2337176))
        self.assertEqual(715, clear_bit(10, 715))
        self.assertEqual(6318, clear_bit(13, 6318))
        self.assertEqual(58869, clear_bit(16, 58869))
        self.assertEqual(838489, clear_bit(20, 838489))
        self.assertEqual(983, clear_bit(10, 983))
        self.assertEqual(83, clear_bit(7, 83))
        self.assertEqual(11728768, clear_bit(24, 11728768))
        self.assertEqual(5584, clear_bit(14, 5584))
        self.assertEqual(772705, clear_bit(20, 772705))
        self.assertEqual(8088499, clear_bit(23, 8088499))
        self.assertEqual(490, clear_bit(9, 490))
        self.assertEqual(20246, clear_bit(15, 20246))
        self.assertEqual(11063, clear_bit(14, 11063))
        self.assertEqual(1262, clear_bit(12, 1262))
        self.assertEqual(310, clear_bit(9, 310))
        self.assertEqual(3977166, clear_bit(22, 3977166))
        self.assertEqual(5784718, clear_bit(23, 5784718))
        self.assertEqual(20027, clear_bit(18, 20027))
        self.assertEqual(0, clear_bit(6, 64))
        self.assertEqual(1775882, clear_bit(22, 1775882))
        self.assertEqual(59988, clear_bit(18, 59988))
        self.assertEqual(2176, clear_bit(14, 2176))

    def test_toggle(self):
        self.assertEqual(1605490, toggle_bit(20, 556914))
        self.assertEqual(31632843, toggle_bit(24, 14855627))
        self.assertEqual(164114, toggle_bit(17, 33042))
        self.assertEqual(345863, toggle_bit(18, 83719))
        self.assertEqual(37068, toggle_bit(15, 4300))
        self.assertEqual(1992, toggle_bit(10, 968))
        self.assertEqual(65406, toggle_bit(15, 32638))
        self.assertEqual(3905, toggle_bit(11, 1857))
        self.assertEqual(6222, toggle_bit(12, 2126))
        self.assertEqual(157680, toggle_bit(17, 26608))
        self.assertEqual(199, toggle_bit(7, 71))
        self.assertEqual(60161, toggle_bit(15, 27393))
        self.assertEqual(13113329, toggle_bit(23, 4724721))
        self.assertEqual(1650, toggle_bit(10, 626))
        self.assertEqual(170433, toggle_bit(17, 39361))
        self.assertEqual(1164361, toggle_bit(20, 115785))
        self.assertEqual(36190, toggle_bit(15, 3422))
        self.assertEqual(0, toggle_bit(6, 64))
        self.assertEqual(3691503, toggle_bit(21, 1594351))
        self.assertEqual(15631438, toggle_bit(23, 7242830))
        self.assertEqual(1631, toggle_bit(10, 607))
        self.assertEqual(1914, toggle_bit(10, 890))
        self.assertEqual(14261, toggle_bit(13, 6069))
        self.assertEqual(211, toggle_bit(7, 83))
        self.assertEqual(2633466, toggle_bit(21, 536314))
        self.assertEqual(1201319, toggle_bit(20, 152743))
        self.assertEqual(49500, toggle_bit(15, 16732))
        self.assertEqual(7246652, toggle_bit(22, 3052348))
        self.assertEqual(458, toggle_bit(8, 202))
        self.assertEqual(2191904, toggle_bit(21, 94752))
        self.assertEqual(1639005, toggle_bit(20, 590429))
        self.assertEqual(49106, toggle_bit(15, 16338))
        self.assertEqual(123929, toggle_bit(16, 58393))
        self.assertEqual(1464, toggle_bit(10, 440))
        self.assertEqual(151417, toggle_bit(17, 20345))
        self.assertEqual(0, toggle_bit(6, 64))
        self.assertEqual(30129, toggle_bit(14, 13745))
        self.assertEqual(11769, toggle_bit(13, 3577))
        self.assertEqual(776081, toggle_bit(19, 251793))
        self.assertEqual(3455, toggle_bit(11, 1407))
        self.assertEqual(33808, toggle_bit(15, 1040))
        self.assertEqual(939076, toggle_bit(19, 414788))
        self.assertEqual(764, toggle_bit(9, 252))
        self.assertEqual(0, toggle_bit(6, 64))
        self.assertEqual(33239024, toggle_bit(24, 16461808))
        self.assertEqual(483, toggle_bit(8, 227))
        self.assertEqual(939, toggle_bit(9, 427))
        self.assertEqual(11694182, toggle_bit(23, 3305574))

    def test_set(self):
        self.assertEqual(3993420, set_bit(21, 1896268))
        self.assertEqual(5462481, set_bit(22, 1268177))
        self.assertEqual(3115773, set_bit(21, 1018621))
        self.assertEqual(616489, set_bit(19, 92201))
        self.assertEqual(8315744, set_bit(22, 4121440))
        self.assertEqual(5283, set_bit(12, 1187))
        self.assertEqual(41395, set_bit(15, 8627))
        self.assertEqual(21029, set_bit(14, 4645))
        self.assertEqual(1192, set_bit(10, 168))
        self.assertEqual(356931, set_bit(18, 94787))
        self.assertEqual(4060308, set_bit(21, 1963156))
        self.assertEqual(360894, set_bit(18, 98750))
        self.assertEqual(14248509, set_bit(23, 5859901))
        self.assertEqual(2343, set_bit(11, 295))
        self.assertEqual(232, set_bit(7, 104))
        self.assertEqual(38947, set_bit(15, 6179))
        self.assertEqual(752411, set_bit(19, 228123))
        self.assertEqual(196, set_bit(7, 68))
        self.assertEqual(614, set_bit(9, 102))
        self.assertEqual(465326, set_bit(18, 203182))
        self.assertEqual(3838, set_bit(11, 1790))
        self.assertEqual(64, set_bit(6, 64))
        self.assertEqual(11277, set_bit(13, 3085))
        self.assertEqual(7689650, set_bit(22, 3495346))
        self.assertEqual(1218, set_bit(10, 194))
        self.assertEqual(349, set_bit(8, 93))
        self.assertEqual(390344, set_bit(18, 128200))
        self.assertEqual(238, set_bit(7, 110))
        self.assertEqual(15830189, set_bit(23, 7441581))
        self.assertEqual(951248, set_bit(19, 426960))
        self.assertEqual(8049, set_bit(12, 3953))
        self.assertEqual(26578800, set_bit(24, 9801584))
        self.assertEqual(215978, set_bit(17, 84906))
        self.assertEqual(390494, set_bit(18, 128350))
        self.assertEqual(1764, set_bit(10, 740))
        self.assertEqual(1904, set_bit(10, 880))
        self.assertEqual(1965, set_bit(10, 941))
        self.assertEqual(2073077, set_bit(20, 1024501))
        self.assertEqual(2113, set_bit(11, 65))
        self.assertEqual(30458133, set_bit(24, 13680917))
        self.assertEqual(509955, set_bit(18, 247811))
        self.assertEqual(73422, set_bit(16, 7886))
        self.assertEqual(23268, set_bit(14, 6884))
        self.assertEqual(591, set_bit(9, 79))
        self.assertEqual(6744333, set_bit(22, 2550029))
        self.assertEqual(2707, set_bit(11, 659))
        self.assertEqual(2013337, set_bit(20, 964761))
        self.assertEqual(267731, set_bit(18, 5587))
        self.assertEqual(2252299, set_bit(21, 155147))
        self.assertEqual(2296, set_bit(11, 248))

    def test_complement(self):
        self.assertEqual(231, byte_complement(24))
        self.assertEqual(36, byte_complement(219))
        self.assertEqual(148, byte_complement(107))
        self.assertEqual(67, byte_complement(188))
        self.assertEqual(201, byte_complement(54))
        self.assertEqual(118, byte_complement(137))
        self.assertEqual(90, byte_complement(165))
        self.assertEqual(78, byte_complement(177))
        self.assertEqual(75, byte_complement(180))
        self.assertEqual(106, byte_complement(149))
        self.assertEqual(165, byte_complement(90))
        self.assertEqual(21, byte_complement(234))
        self.assertEqual(211, byte_complement(44))
        self.assertEqual(105, byte_complement(150))
        self.assertEqual(195, byte_complement(60))
        self.assertEqual(235, byte_complement(20))
        self.assertEqual(196, byte_complement(59))
        self.assertEqual(207, byte_complement(48))
        self.assertEqual(62, byte_complement(193))
        self.assertEqual(140, byte_complement(115))
        self.assertEqual(20, byte_complement(235))
        self.assertEqual(88, byte_complement(167))
        self.assertEqual(39, byte_complement(216))
        self.assertEqual(24, byte_complement(231))
        self.assertEqual(13, byte_complement(242))
        self.assertEqual(68, byte_complement(187))
        self.assertEqual(20, byte_complement(235))
        self.assertEqual(68, byte_complement(187))
        self.assertEqual(176, byte_complement(79))
        self.assertEqual(28, byte_complement(227))
        self.assertEqual(163, byte_complement(92))
        self.assertEqual(151, byte_complement(104))
        self.assertEqual(220, byte_complement(35))
        self.assertEqual(17, byte_complement(238))
        self.assertEqual(5, byte_complement(250))
        self.assertEqual(236, byte_complement(19))
        self.assertEqual(68, byte_complement(187))
        self.assertEqual(26, byte_complement(229))
        self.assertEqual(154, byte_complement(101))
        self.assertEqual(11, byte_complement(244))
        self.assertEqual(73, byte_complement(182))
        self.assertEqual(198, byte_complement(57))
        self.assertEqual(52, byte_complement(203))
        self.assertEqual(103, byte_complement(152))
        self.assertEqual(80, byte_complement(175))
        self.assertEqual(33, byte_complement(222))
        self.assertEqual(211, byte_complement(44))
        self.assertEqual(11, byte_complement(244))
        self.assertEqual(179, byte_complement(76))
        self.assertEqual(60, byte_complement(195))


class TestJoinBytes(unittest.TestCase):
    def test_make_word(self):
        self.assertEqual(16530, make_word(64, 146))
        self.assertEqual(45260, make_word(176, 204))
        self.assertEqual(27240, make_word(106, 104))
        self.assertEqual(16692, make_word(65, 52))
        self.assertEqual(22395, make_word(87, 123))
        self.assertEqual(58189, make_word(227, 77))
        self.assertEqual(15715, make_word(61, 99))
        self.assertEqual(12824, make_word(50, 24))
        self.assertEqual(52232, make_word(204, 8))
        self.assertEqual(56, make_word(0, 56))
        self.assertEqual(5295, make_word(20, 175))
        self.assertEqual(20301, make_word(79, 77))
        self.assertEqual(43689, make_word(170, 169))
        self.assertEqual(24105, make_word(94, 41))
        self.assertEqual(53954, make_word(210, 194))
        self.assertEqual(35953, make_word(140, 113))
        self.assertEqual(37693, make_word(147, 61))
        self.assertEqual(5686, make_word(22, 54))
        self.assertEqual(53400, make_word(208, 152))
        self.assertEqual(45951, make_word(179, 127))
        self.assertEqual(49661, make_word(193, 253))
        self.assertEqual(4545, make_word(17, 193))
        self.assertEqual(23924, make_word(93, 116))
        self.assertEqual(25326, make_word(98, 238))
        self.assertEqual(2770, make_word(10, 210))
        self.assertEqual(25852, make_word(100, 252))
        self.assertEqual(31041, make_word(121, 65))
        self.assertEqual(27483, make_word(107, 91))
        self.assertEqual(3561, make_word(13, 233))
        self.assertEqual(12586, make_word(49, 42))
        self.assertEqual(34851, make_word(136, 35))
        self.assertEqual(20931, make_word(81, 195))
        self.assertEqual(36865, make_word(144, 1))
        self.assertEqual(59779, make_word(233, 131))
        self.assertEqual(15647, make_word(61, 31))
        self.assertEqual(12264, make_word(47, 232))
        self.assertEqual(57331, make_word(223, 243))
        self.assertEqual(53667, make_word(209, 163))
        self.assertEqual(56979, make_word(222, 147))
        self.assertEqual(39909, make_word(155, 229))
        self.assertEqual(16559, make_word(64, 175))
        self.assertEqual(16139, make_word(63, 11))
        self.assertEqual(29307, make_word(114, 123))
        self.assertEqual(12904, make_word(50, 104))
        self.assertEqual(51302, make_word(200, 102))
        self.assertEqual(20549, make_word(80, 69))
        self.assertEqual(10947, make_word(42, 195))
        self.assertEqual(53316, make_word(208, 68))
        self.assertEqual(11169, make_word(43, 161))
        self.assertEqual(51071, make_word(199, 127))

    def join_bytes_little_endian(self):
        self.assertEqual(575448282, join_bytes_little_endian([218, 164, 76, 34, 56]))
        self.assertEqual(108468138804517, join_bytes_little_endian([37, 5, 226, 180, 166, 98, 152]))
        self.assertEqual(20393699641648246, join_bytes_little_endian([118, 228, 203, 54, 246, 115, 72, 6]))
        self.assertEqual(5731966560260329183, join_bytes_little_endian([223, 14, 188, 160, 55, 9, 140, 79, 36]))
        self.assertEqual(1418421691125617752, join_bytes_little_endian([88, 84, 64, 81, 3, 63, 175, 19, 139]))
        self.assertEqual(3787746142, join_bytes_little_endian([94, 107, 196, 225, 250]))
        self.assertEqual(202385095443225, join_bytes_little_endian([25, 195, 184, 115, 17, 184, 63]))
        self.assertEqual(71, join_bytes_little_endian([71, 62]))
        self.assertEqual(41874719898700, join_bytes_little_endian([76, 252, 205, 183, 21, 38, 216]))
        self.assertEqual(203, join_bytes_little_endian([203, 89]))
        self.assertEqual(219, join_bytes_little_endian([219, 145]))
        self.assertEqual(95, join_bytes_little_endian([95, 204]))
        self.assertEqual(4197328180, join_bytes_little_endian([52, 37, 46, 250, 109]))
        self.assertEqual(2175442816, join_bytes_little_endian([128, 159, 170, 129, 125]))
        self.assertEqual(41109, join_bytes_little_endian([149, 160, 234]))
        self.assertEqual(108, join_bytes_little_endian([108, 249]))
        self.assertEqual(7291890923055, join_bytes_little_endian([47, 118, 145, 198, 161, 6, 160]))
        self.assertEqual(1317782086, join_bytes_little_endian([70, 194, 139, 78, 66]))
        self.assertEqual(195, join_bytes_little_endian([195, 39]))
        self.assertEqual(373804484941, join_bytes_little_endian([77, 201, 123, 8, 87, 42]))
        self.assertEqual(3094708091, join_bytes_little_endian([123, 127, 117, 184, 40]))
        self.assertEqual(236, join_bytes_little_endian([236, 249]))
        self.assertEqual(192644566, join_bytes_little_endian([214, 133, 123, 11, 225]))
        self.assertEqual(12541858946842831720, join_bytes_little_endian([104, 43, 159, 53, 67, 162, 13, 174, 43]))
        self.assertEqual(236426402468240, join_bytes_little_endian([144, 17, 188, 79, 7, 215, 42]))
        self.assertEqual(2799250096121011545117,
                         join_bytes_little_endian([29, 164, 244, 2, 92, 27, 102, 191, 151, 179]))
        self.assertEqual(4264689968694591857734,
                         join_bytes_little_endian([70, 164, 233, 92, 59, 99, 118, 48, 231, 126]))
        self.assertEqual(190431126772662, join_bytes_little_endian([182, 91, 170, 51, 50, 173, 102]))
        self.assertEqual(3970438117289075559144,
                         join_bytes_little_endian([232, 74, 22, 70, 100, 207, 229, 60, 215, 65]))
        self.assertEqual(43, join_bytes_little_endian([43, 216]))
        self.assertEqual(12289091, join_bytes_little_endian([67, 132, 187, 71]))
        self.assertEqual(186561579504468, join_bytes_little_endian([84, 211, 172, 64, 173, 169, 48]))
        self.assertEqual(207, join_bytes_little_endian([207, 34]))
        self.assertEqual(54053, join_bytes_little_endian([37, 211, 171]))
        self.assertEqual(16480519, join_bytes_little_endian([7, 121, 251, 89]))
        self.assertEqual(3379513171, join_bytes_little_endian([83, 71, 111, 201, 101]))
        self.assertEqual(52252671108743, join_bytes_little_endian([135, 102, 230, 5, 134, 47, 0, 120]))
        self.assertEqual(3205078690824714278202,
                         join_bytes_little_endian([58, 85, 33, 5, 18, 232, 102, 191, 173, 116]))
        self.assertEqual(591955487869296396025, join_bytes_little_endian([249, 70, 119, 12, 231, 91, 8, 23, 32, 4]))
        self.assertEqual(609073, join_bytes_little_endian([49, 75, 9, 89]))
        self.assertEqual(38848, join_bytes_little_endian([192, 151, 248]))
        self.assertEqual(18765737856728128, join_bytes_little_endian([64, 252, 229, 210, 86, 171, 66, 122]))
        self.assertEqual(15264, join_bytes_little_endian([160, 59, 185]))
        self.assertEqual(186540133337099, join_bytes_little_endian([11, 72, 98, 66, 168, 169, 240]))
        self.assertEqual(3927072330, join_bytes_little_endian([74, 94, 18, 234, 99]))
        self.assertEqual(228, join_bytes_little_endian([228, 96]))
        self.assertEqual(2604661027426237279409,
                         join_bytes_little_endian([177, 236, 217, 204, 91, 220, 238, 50, 141, 90]))
        self.assertEqual(157230399, join_bytes_little_endian([63, 37, 95, 9, 61]))
        self.assertEqual(90, join_bytes_little_endian([90, 5]))
        self.assertEqual(8845493038057249530,
                         join_bytes_little_endian([250, 218, 151, 124, 13, 129, 193, 122, 154]))

    def join_bytes_big_endian(self):
        self.assertEqual(4190866805482931732599, join_bytes_big_endian([227, 47, 245, 211, 108, 58, 57, 192, 119]))
        self.assertEqual(238585001726482, join_bytes_big_endian([216, 253, 230, 70, 210, 18]))
        self.assertEqual(516268307030, join_bytes_big_endian([120, 51, 253, 50, 86]))
        self.assertEqual(112072061542094, join_bytes_big_endian([101, 237, 207, 106, 222, 206]))
        self.assertEqual(231415181840903, join_bytes_big_endian([210, 120, 139, 181, 146, 7]))
        self.assertEqual(1091893648231470596256957,
                         join_bytes_big_endian([231, 55, 172, 91, 222, 9, 52, 210, 116, 189]))
        self.assertEqual(4214646639734102687716,
                         join_bytes_big_endian([228, 121, 248, 196, 174, 232, 239, 255, 228]))
        self.assertEqual(14052227650129302, join_bytes_big_endian([49, 236, 109, 53, 99, 141, 150]))
        self.assertEqual(604501211501935441580, join_bytes_big_endian([32, 197, 35, 185, 19, 138, 35, 182, 172]))
        self.assertEqual(4499229852017278753686, join_bytes_big_endian([243, 231, 91, 112, 119, 227, 58, 155, 150]))
        self.assertEqual(15473954, join_bytes_big_endian([236, 29, 34]))
        self.assertEqual(92466157412239, join_bytes_big_endian([84, 24, 244, 119, 95, 143]))
        self.assertEqual(14641301845606080079, join_bytes_big_endian([203, 48, 90, 116, 164, 159, 30, 79]))
        self.assertEqual(2152373454, join_bytes_big_endian([128, 74, 156, 206]))
        self.assertEqual(26158, join_bytes_big_endian([102, 46]))
        self.assertEqual(7903663172716892948, join_bytes_big_endian([109, 175, 115, 199, 186, 32, 147, 20]))
        self.assertEqual(3774737405862175433413, join_bytes_big_endian([204, 161, 1, 55, 55, 58, 121, 226, 197]))
        self.assertEqual(42255875987421245, join_bytes_big_endian([150, 31, 126, 205, 231, 56, 61]))
        self.assertEqual(14915269, join_bytes_big_endian([227, 150, 197]))
        self.assertEqual(5556404, join_bytes_big_endian([84, 200, 180]))
        self.assertEqual(26456, join_bytes_big_endian([103, 88]))
        self.assertEqual(1691789764, join_bytes_big_endian([100, 214, 169, 196]))
        self.assertEqual(420654883333, join_bytes_big_endian([97, 240, 252, 34, 5]))
        self.assertEqual(5519963, join_bytes_big_endian([84, 58, 91]))
        self.assertEqual(10184432000022176883, join_bytes_big_endian([141, 86, 94, 241, 208, 113, 100, 115]))
        self.assertEqual(877254048301126462539083,
                         join_bytes_big_endian([185, 196, 9, 137, 46, 186, 28, 101, 5, 75]))
        self.assertEqual(539541021823, join_bytes_big_endian([125, 159, 38, 164, 127]))
        self.assertEqual(160276430943999, join_bytes_big_endian([145, 197, 67, 187, 118, 255]))
        self.assertEqual(34736538818178, join_bytes_big_endian([31, 151, 187, 14, 150, 130]))
        self.assertEqual(133015116064614045871205,
                         join_bytes_big_endian([28, 42, 195, 142, 84, 122, 67, 46, 108, 101]))
        self.assertEqual(185554863637424, join_bytes_big_endian([168, 194, 219, 187, 195, 176]))
        self.assertEqual(33227775387326, join_bytes_big_endian([30, 56, 113, 191, 166, 190]))
        self.assertEqual(603924577452863020538649,
                         join_bytes_big_endian([127, 226, 209, 35, 71, 213, 86, 175, 27, 25]))
        self.assertEqual(465918007675, join_bytes_big_endian([108, 122, 224, 153, 123]))
        self.assertEqual(3907181179, join_bytes_big_endian([232, 226, 218, 123]))
        self.assertEqual(4205969101, join_bytes_big_endian([250, 177, 254, 205]))
        self.assertEqual(8104188, join_bytes_big_endian([123, 168, 252]))
        self.assertEqual(3110879792763883560448, join_bytes_big_endian([168, 164, 33, 49, 95, 8, 21, 30, 0]))
        self.assertEqual(3381541, join_bytes_big_endian([51, 153, 37]))
        self.assertEqual(850879, join_bytes_big_endian([12, 251, 191]))
        self.assertEqual(2014530316978331297131, join_bytes_big_endian([109, 53, 57, 105, 218, 76, 131, 165, 107]))
        self.assertEqual(928918019, join_bytes_big_endian([55, 94, 42, 3]))
        self.assertEqual(13808311852868852527, join_bytes_big_endian([191, 160, 250, 120, 122, 16, 91, 47]))
        self.assertEqual(930975840475945523017827,
                         join_bytes_big_endian([197, 36, 77, 43, 23, 120, 166, 68, 248, 99]))
        self.assertEqual(2684948650348204168692, join_bytes_big_endian([145, 141, 37, 204, 6, 41, 50, 149, 244]))
        self.assertEqual(616187482944346792891562,
                         join_bytes_big_endian([130, 123, 151, 35, 92, 174, 19, 235, 148, 170]))
        self.assertEqual(11954663, join_bytes_big_endian([182, 105, 231]))
        self.assertEqual(51074, join_bytes_big_endian([199, 130]))
        self.assertEqual(49081123046880349, join_bytes_big_endian([174, 95, 5, 120, 98, 244, 93]))
        self.assertEqual(376002496, join_bytes_big_endian([22, 105, 87, 192]))

        if __name__ == "__main__":
            unittest.main()
