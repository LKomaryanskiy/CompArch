""" Tests for Model class """

import unittest
from unittest.mock import patch
from src.Event import Event
import test_helpers as th


class TestModelClass(unittest.TestCase):

    @patch('src.Model.Model')
    def test_event_create(self, Model):
        model = Model()
        model.event_list.return_value = [Event('test', 'test')]
        elist = model.events_list()
        self.assertNotEqual(elist, [])

    @patch('src.Model.Model.remove_event', side_effect=th.delete_event)
    def test_remove_event(self, remove_event):
        self.assertEqual(remove_event('test', [Event('test', 'test')]), [])
        with self.assertRaises(Exception):
            remove_event('t', [Event('test', 'test')])


if __name__ == "__main__":
    unittest.main()
