import unittest
from testovoe import get_score, INITIAL_STAMP

STAMP = [
    {
    "offset": 0,
    "score": {
        "home": 0,
        "away": 0
             }
    },
    {
    "offset": 3,
    "score": {
        "home": 4,
        "away": 4
             }
    },
    {
    "offset": 5,
    "score": {
        "home": 4,
        "away": 4
             }
    },
    ]

class Test_get_score(unittest.TestCase):

    def test_initial_stamp_0_offset(self):
        self.assertEqual(get_score([INITIAL_STAMP], 0), (0, 0))

    def test_initial_stamp_10_offset(self):
        self.assertEqual(get_score([INITIAL_STAMP], 10), (None, None))

    def test_3_stamps_5_offset(self):
        self.assertEqual(get_score(STAMP, 5), (4, 4))

    def test_empty_stamps_empty_offset(self):
        self.assertEqual(get_score(None, None), (None, None))


if __name__ == "__main__":
    unittest.main()

