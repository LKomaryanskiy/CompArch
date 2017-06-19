''' Constants for keys from parser dictionary result 
    Config handles save type for doctest.'''
import re
save_type_key = 'save_type'
last_save_type = 'last_save_type'

def config_parser_result():
    ''' If config is empty it full fills the result of parser with default values '''
    dictionary_result = {}
    try:
        dictionary_result = read_from_configs("savetype.cfg")
    except IOError:
        dictionary_result = {save_type_key: 'json'}

    if not dictionary_result:
        dictionary_result = {save_type_key: 'json'}

    return dictionary_result

def last_session_data_save(type_of_save):
    with open (".lastSessionData", "w") as fl:
        fl.write(last_save_type + "=" + type_of_save)

def last_session_save_type():
    dictionary_result = {}
    try:
        dictionary_result = read_from_configs(".lastSessionData")
    except IOError:
        last_session_data_save('json')

    if not dictionary_result:
        dictionary_result = {last_save_type: 'json'}

    return dictionary_result[last_save_type]

def read_from_configs(file_name):
    result = {}
    delimiter = "="
    comment_delimiter = "#"
    with open(file_name, "r") as fl:
        for line in fl:
            if (line[0] != comment_delimiter):
                separate_list = line.split(delimiter)
                #using replace to fix newline inclusion
                result[separate_list[0]] = separate_list[1].replace("\n","") 
                break

    return result
