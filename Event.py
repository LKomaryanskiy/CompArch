class Event:
    def __init__(self, title, description):
        self.title = title
        self.description = description

    @property
    def title(self):
        return self.__title

    @property
    def description(self):
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

