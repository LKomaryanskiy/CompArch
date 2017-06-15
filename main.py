from Controller import Controller
from Model import Model

if __name__ == "__main__":
    model = Model('savedata', result_dict[save_type_key])
    controller = Controller(model)
    controller.start()
    model.save()
