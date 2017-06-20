from src.Controller import Controller
from src.Model import Model
from src.configuration.configParser import config_parser_result, save_type_key

if __name__ == "__main__":
    result_dict = config_parser_result()
    model = Model('savedata', result_dict[save_type_key])
    controller = Controller(model)
    controller.start()
