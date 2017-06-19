""" Unit test for Serialize module """

from io import StringIO, BytesIO
import unittest
import pickle
import json
import yaml
from src.Event import Event
import src.serialize.JsonSerialize as jns
import src.serialize.Serialize as srz


class TestSerializeMethods(unittest.TestCase):
    """ test for Serialize module """

    def setUp(self):
        event = Event('Very important meeting', 'Meeting at 3:00 UTC')
        self.data = [event]
        self.output = None

    def test_pickle(self):
        """ test for serialization with pickle """
        output = pickle.dumps(self.data)
        self.output = BytesIO(output)
        extr_data = srz.load(self.output, 'pickle')
        self.assertEqual(self.data, extr_data)

    def test_yaml(self):
        """ test for serialization with yaml """
        output = yaml.dump(self.data)
        self.output = StringIO(output)
        extr_data = srz.load(self.output, 'yaml')
        self.assertEqual(self.data, extr_data)

    def test_json(self):
        """ test for serialization with json """
        output = json.dumps(self.data, default=jns.js_default)
        self.output = StringIO(output)
        events = srz.load(self.output, 'json')
        self.assertEqual(self.data, events)


if __name__ == "__main__":
    unittest.main()
