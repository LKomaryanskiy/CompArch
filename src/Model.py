""" Implementation of Model class """

import src.serialize.Serialize as srz
from src.Event import Event


class Model:
    """ Class Model controls all operations on events.

    Attributes:
        __events_list(list): List of events.
    """

    def __init__(self, filename, serialization_type):
        """ Initialize Model class

        Args:
            filename(str): Set name of the file which is used to upload
                information about schedule.
        """

        self.__events_list = []
        self.filename = filename
        self.serialization_type = serialization_type
        self.load()

    @property
    def events_list(self):
        """ list: Contains the list of events. """
        return self.__events_list

    def create_event(self, title, description):
        """ Method create_event creates event and adds it to the list.

        Args:
            title(str): Title of event.
            description(str): Description of event.
        Raises:
            Exception: if event with given title already exist.

        Examples:
            >>> model.create_event("New event", "Do smth.")
            >>> model._show_list(model.event_list)
            [Title: 'New event', Description: 'Do smth.': ']
            >>> model.create_event("New event", "Do smth else.")
            Traceback (most recent call last):
            Exception: [ERROR]::The event already exists.
        """

        if self._is_title_exists(title):
            raise Exception("[ERROR]::The event already exists.")
        self.__events_list.append(Event(title, description))

    def remove_event(self, title):
        """ Removes an event from events list.

        Args:
            title(str): The title of the deleted event.
        Raises:
            Exception: if event with given title does not exist.

        Examples:
            >>> model.remove_event("Old event")
            Traceback (most recent call last):
            Exception: [ERROR]::There is no event with such title.
            >>> model.remove_event("New event")
            >>> model._show_list(model.events_list)
            []
        """
        if not self._is_title_exists(title):
            raise Exception("[ERROR]::There is no event with such title.")
        self.__events_list = [
            event for event in self.__events_list if event.title != title]

    def load(self):
        """ Load information about events

        Args:
            filename(str): Set name of the file which is used to upload
                information about events.
        """

        load_type = last_session_save_type()

        specifier = "rb" if load_type == srz.pickle_type else "r"
        try:
            with open(self.filename, specifier) as source:
                self.__events_list = srz.load(source, load_type)
                if not self.__events_list:
                    self.__events_list = []
        except OSError:
            self.__events_list = []

    def save(self):
        """ Save information about events in text file.

        Args:
            filename(str): Set name of the file which is used to upload
                information about events.
        """
        specifier = "wb" if self.serialization_type == srz.pickle_type else "w"
        with open(self.filename, specifier) as target_file:
            srz.save(self.__events_list, target_file, self.serialization_type)

        last_session_data_save(self.serialization_type)

    def _is_title_exists(self, title):
        if self.__events_list:
            event_title = [
                event for event in self.__events_list if event.title == title]
            return bool(event_title)
        else:
            return False

    # this method created for test
    def _show_list(self, lst):
        return [str(item) for item in lst]

