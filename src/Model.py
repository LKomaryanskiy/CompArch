""" Implementation of Model class """

from src.Event import Event


class Model:
    """ Class Model controls all operations on events.

    Attributes:
        __events_list(list): List of events.
    """

    def __init__(self):
        """ Initialize Model class

        Args:
            filename(str): Set name of the file which is used to upload
                information about schedule.
        """

        self.__events_list = []

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

