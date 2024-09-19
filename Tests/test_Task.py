import unittest

from Task import Task
from Status import Status


class TestStatus(unittest.TestCase):

    def test_create_task(self):
        # Create Task without with default status
        task = Task("Do Something")
        self.assertEqual(task.description, "Do Something")
        self.assertEqual(task.status, Status.NOT_COMPLETED)

        # Create Task with Status enum
        task = Task("Do Something Else", Status.COMPLETED)
        self.assertEqual(task.description, "Do Something Else")
        self.assertEqual(task.status, Status.COMPLETED)

        # Create Task with status string
        task = Task("Do Something Else", "Complete")
        self.assertEqual(task.description, "Do Something Else")
        self.assertEqual(task.status, Status.COMPLETED)

    def test_cannot_create_task_with_bad_status(self):
        with self.assertRaises(ValueError):
            Task.from_string("Invalid Task", "bad status")


if __name__ == '__main__':
    unittest.main()
