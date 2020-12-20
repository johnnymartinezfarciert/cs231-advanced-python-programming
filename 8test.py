import unittest
# Classes and methods to demonstrate unittest
class exponents():
    def square(x):
        return x**2

class test_exponents(unittest.TestCase):
    def test_square(self):
        self.assertEqual(exponents.square(-6),36)
        self.assertAlmostEqual(exponents.square(0),0.001,places=2)
        with self.assertRaises(TypeError):
            exponents.square('j')

    unittest.main(verbosity=2)
