import unittest
from src.Event import Event


class TestEventClass(unittest.TestCase):

    def setUp(self):
        self.event = Event('test', 'test')

    def test_getters(self):
        self.assertIsNotNone(self.event.title)
        self.assertIsNotNone(self.event.description)

    def test_setter(self):
        new_title = 'test1'
        new_description = 'test1'
        self.event.title = new_title
        self.event.description = new_description
        self.assertEqual(self.event.title, new_title)
        self.assertEqual(self.event.description, new_description)

    def test_eq(self):
        clone = Event(self.event.title, self.event.description)
        self.assertEqual(self.event, clone)
        clone.title = 'reverse'
        self.assertNotEqual(self.event, clone)


if __name__ == "__main__":
    unittest.main()
