""" Helpers for test Model class """


def _is_title_exists(title, elist):
    title = [event for event in elist if event.title == title]
    return True if title else False


def delete_event(title, lst):
    if not _is_title_exists(title, lst):
        raise Exception("[ERROR]::There is no event with such title.")
    return [event for event in lst if event.title != title]
