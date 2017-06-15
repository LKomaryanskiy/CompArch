import pickle
import yaml

pickle_type = "pickle"
yaml_type = "yaml"


def load(file_obj, serialize_method):
    """ deserialize data """
    if serialize_method == pickle_type:
        return pickle.load(file_obj)
    elif serialize_method == yaml_type:
        return yaml.load(file_obj)
    elif serialize_method == json_type:
        return jsn.jload(file_obj)


def save(data, file_obj, serialize_method):
    """ serialize data """
    try:
        if serialize_method == pickle_type:
            pickle.dump(data, file_obj)
        elif serialize_method == yaml_type:
            yaml.dump(data, file_obj, default_flow_style=False)
        elif serialize_method == json_type:
            jsn.jdump(data, file_obj)
    except ValueError:
        raise Exception("[ERROR]::Serialization failed")
