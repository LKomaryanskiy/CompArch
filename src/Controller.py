from View import View


class Controller:
    

    def __init__(self, main_model):
        self.model = main_model

    def start(self):
        mode = 0
        View.main_menu()

        while mode != 4:
            try:
                mode = int(input("Choose option: "))
            except ValueError:
                View.wrong_option()
                mode = 0

            if mode == 1:
                self.create_event_manager()
                View.main_menu()
            elif mode == 2:
                self.delete_event_manager()
                View.main_menu()
            elif mode == 3:
                View.print_events(self.model.events_list)
                View.main_menu()
            elif mode == 4:
                self.model.save()
                View.exit_message()
            elif mode not in range(1, 4):
                View.main_menu()

    def create_event_manager(self):
        title = None
        description = None
        try:
            title = str(input("Enter event title: "))
            description = str(input("Enter event description: "))
        except ValueError:
            View.wrong_input()
            return

        try:
            self.model.create_event(title, description)
        except Exception as e:
            print(e)
            return

        View.success_event_create_message()
        return

    def delete_event_manager(self):
        event_number = 0
        try:
            event_number = int(input("Enter event number: "))
        except ValueError:
            View.wrong_input()
            return
        if not self.model.events_list or (
            event_number not in range(
                1, len(
                self.model.events_list) + 1)):
            View.wrong_input()
            return
        event = self.model.events_list[event_number - 1]
        self.model.remove_event(event.title)
