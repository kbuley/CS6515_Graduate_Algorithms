import unittest

from fast_integer_multiplication import fast_integer_multiplication
from fast_fourier_transform import Polynomial

class TestDP(unittest.TestCase):

    def test_fast_integer_mult(self):
        self.assertTrue(fast_integer_multiplication(1234,56678) == 1234*56678)

    def test_fft(self):
        poly = Polynomial([1,3,5,5,6,3])
        fft = poly.fft()
        expected = poly.eval_test()

        ok = True
        for i in range(len(fft)):
            if abs(fft[i].real-expected[i].real) > 1e-2 or \
               abs(fft[i].imag-expected[i].imag) > 1e-2:
               ok = False
               break

        self.assertTrue(ok)

if __name__ == '__main__':
    unittest.main()
