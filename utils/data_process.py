import json
import jsonlines
import pickle

def read_jsonl(file_path):
    data_list = []
    with open(file_path, "r",encoding='utf-8') as file:
        for line in file:
            json_data = json.loads(line)
            data_list.append(json_data)
    return data_list

def write_jsonl(file_path, data_list):
    with jsonlines.open(file_path, 'w') as jsonl_file:
        for data in data_list:
            jsonl_file.write(data)
            
def read_json(file_path):
    with open(file_path, 'r') as json_file:
        data_list = json.load(json_file)
    return data_list
            
def write_json(file_path, data_list):
    with open(file_path, 'w', encoding='utf-8') as file:
        json.dump(data_list, file,ensure_ascii=False, indent=4)  

def read_pk(file_path):
    data_list = []
    with open(file_path, 'rb') as f:
        data_list = pickle.load(f)
    return data_list