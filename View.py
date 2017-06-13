class View:

    def main_menu():
        print("~~ Menu ~~")
        print("1: Add event")
        print("2: Remove event")
        print("3: List of events")
        print("4: Exit\n")

    def event_create():
        print("Enter the information about the event below\n.")

    def print_events(events_list):
        if not events_list:
            print('You have no events!')
        else:
            print('Your events:\n')
            for i in range(len(events_list)):
                event = events_list[i]
                print("{}. {}".format(i + 1, event))
        print('\n')

    def success_event_create_message():
        print("\nEvent set!\n")

    def wrong_input():
        print("Invalid input!\n")

    def wrong_option():
        print("No current option!\n")

    def exit_message():
        print("We saved your data. Be organized!\n")
