""" Implementation of Event class """


class Event:
    """ Describes all properties of events schedule.

    Attributes:
        title: Contains events title.
        description: Contains event description.
    """

    def __init__(self, title, description):
        """ Initialize Event class.

        Args:
            title(str): The title of event;
            Can be an arbitrary sequence of characters.
            description(str): Description of event.

        Examples:
            >>> new_event = Event('New event', 'Drink b33r with ur buddys')
            >>> new_event  #doctest: +ELLIPSIS
            <__main__.Event object at 0x...>
            >>> print(new_event)
            Title: New event; Description: Drink b33r with ur buddys
        """
        self.title = title
        self.description = description

    @property
    def title(self):
        """ str: Contains a title of a particular event
        Examples:
            >>> event.title
            'Main event'
            >>> important_event.title = "Important event"
            >>> important_event.title
            'Important event'
        """
        return self.__title

    @property
    def description(self):
        """ str: Contains description of a particular event
        Examples:
            >>> event.description
            'Drink b33r with ur buddys'
            >>> great_event.description = "Drink b33r with ur grandma"
            >>> great_event.description
            'Drink b33r with ur grandma'
        """
        return self.__description

    @description.setter
    def description(self, description):
        self.__description = description

    @title.setter
    def title(self, title):
        self.__title = title

    def __str__(self):
        return "Title: {}; Description: {}".format(
            self.title, self.description)

    def __eq__(self, event):
        if self.__title == event.title\
                and self.__description == event.description:
            return True
        return False


if __name__ == "__main__":
    import doctest
    doctest.testmod(extraglobs={"b33r": Event("Title", "Description")})

