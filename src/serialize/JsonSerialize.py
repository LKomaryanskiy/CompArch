""" Module for serialization using JSON format """

import json
from src.Event import Event


def js_default(obj):
    """ serialize method for Event class"""
    return {'event_title': obj.title, 'description': obj.description}


def decode(lst):
    """ Decode serialized data """
    event_list = lst
    events = list()
    events = [Event(event['event_title'], event['description']) for event in event_list]
    return events


def jload(file_obj):
    """ Load model from a file """
    data = json.load(file_obj)
    event_list = decode(data)
    return event_list


def jdump(data, file_obj):
    """ Dump model to a file """
    json.dump(data, file_obj, default=js_default)
