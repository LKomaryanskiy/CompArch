from Event import Event


class Model:

    def __init__(self):
        self.__events_list = []

    @property
    def events_list(self):
        return self.__events_list

    def create_event(self, title, description):
        if self._is_title_exists(title):
            raise Exception("[ERROR]::The event already exists.")
        self.__events_list.append(Event(title, description))

    def remove_event(self, title):
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

