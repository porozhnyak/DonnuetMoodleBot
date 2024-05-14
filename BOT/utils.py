import json
import os

def save_to_json(filename, data):
    if os.path.exists(filename):
        current_data = load_from_json(filename)
        current_data.update(data)
        data = current_data
    
    with open(filename, 'w', encoding='utf-8') as file:
        json.dump(data, file, ensure_ascii=False, indent=4)

def load_from_json(filename):
    if not os.path.exists(filename):
        return {}
    
    with open(filename, 'r', encoding='utf-8') as file:
        data = json.load(file)
    return data

