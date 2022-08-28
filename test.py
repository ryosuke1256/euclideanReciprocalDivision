import unittest 
import euclideanReciprocalDivision

class TestEuclideanReciprocalDivision(unittest.TestCase):
    def test_euclidean_reciprocal_division(self):
        self.assertTrue(euclideanReciprocalDivision.euclideanReciprocalDivision(51,21) == 3)
        self.assertTrue(euclideanReciprocalDivision.euclideanReciprocalDivision(49,21) == 7)
        self.assertTrue(euclideanReciprocalDivision.euclideanReciprocalDivision(21,49) == 7)
        self.assertTrue(euclideanReciprocalDivision.euclideanReciprocalDivision(300,630) == 30)

if __name__ == '__main__':
    unittest.main()
