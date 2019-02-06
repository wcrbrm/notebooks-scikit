import unittest
import re

def cabin_letter(x):
    return str(x)[:1]
def cabin_num(x):
    list = re.sub('[^0-9\\s]', '', str(x)[1:]).split()
    sum = 0
    for number in list:
        sum += int(number)
    return int(sum / len(list))


class CabinExtractionTest(unittest.TestCase):
    def testLetter(self):
        self.assertEqual(cabin_letter("C23 C25 C27"), "C")

    def testnum1(self):
        self.assertEqual(cabin_num("B77"), 77)
    def testnum2(self):
        self.assertEqual(cabin_num("B96 B98"), 97)
    def testnum3(self):
        self.assertEqual(cabin_num("C23 C25 C27"), 25)
    def testnum4(self):
        avg = int((57 + 59 + 63 + 66) / 4.0)
        self.assertEqual(cabin_num("B57 B59 B63 B66"), avg)
