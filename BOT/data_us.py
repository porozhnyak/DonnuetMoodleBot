import re
from BOT.utils import save_to_json, load_from_json

# username = "Дмитрий СРВ-21-А_Роговой"
# login = "ШОШОШ43О"
# password = "Stud_2023"

def extract_code(username):# Выводит группу учащегося
    pattern = r'\b([А-ЯA-Z]+\-\d+\-\w+)(?:\_)?\b'
    match = re.search(pattern, username)
    
    if match:
        code_with_possible_underscore = match.group(1)
        return code_with_possible_underscore.split('_')[0]
    else:
        return None

# group = extract_code(username)

# print(extract_code(username))

def save_data(group, login, password):

    # group = extract_code(username)
    # Сохранение данных в JSON файл
    new_data = {
        group: {
            login : password,
        }
    }
    save_to_json('data_users/data.json', new_data)
    print("Данные добавлены в data.json")

    # Загрузка данных из JSON файла
    loaded_data = load_from_json('data_users/data.json')
    print("Загруженные данные:", loaded_data)

# if __name__ == "__main__":
#     save_data()

def add_credentials(group, login, password):
    # Загрузка текущих данных из файла
    current_data = load_from_json('data_users/data.json')
    
    if group not in current_data:
        current_data[group] = {}

    # Проверка наличия группы в данных
    if group in current_data:
        # Проверка наличия логина в группе
        if login not in current_data[group]:
            current_data[group][login] = password
            save_to_json('data_users/data.json', current_data)
            return f"Добавлены новые учетные данные для {login} в группе {group}."
        else:
            return f"Логин {login} уже существует в группе {group}."


    



def add_data(group, login, password):

    if add_credentials(group, login, password):
        return "Данные были обновлены"
    elif save_data(group, login, password):
        return "Данные были сохранены в новом файле"
    else:
        return "Не удалось сохранить данные"
    

# if __name__ == "__main__":
#     add_data(group, login, password)