import unittest

from Status import Status


class TestStatus(unittest.TestCase):

    def test_from_string_returns_correct_status(self):
        self.assertEqual(Status.from_string("Complete"), Status.COMPLETED)
        self.assertEqual(Status.from_string("Not Complete"), Status.NOT_COMPLETED)
        self.assertEqual(Status.from_string("In Progress"), Status.IN_PROGRESS)

    def test_from_string_raises_value_error_for_invalid_status(self):
        with self.assertRaises(ValueError):
            Status.from_string("Invalid Status")

    def test_status_map_is_correct(self):
        self.assertEqual(Status.STATUS_MAP, {"Complete": Status.COMPLETED,
                                             "Not Complete": Status.NOT_COMPLETED,
                                             "In Progress": Status.IN_PROGRESS})


if __name__ == '__main__':
    unittest.main()
