from src.Controller import Controller
from src.Model import Model

if __name__ == "__main__":
    model = Model()
    controller = Controller(model)
    controller.start()
