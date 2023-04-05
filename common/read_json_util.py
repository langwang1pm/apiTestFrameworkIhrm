import json


def ihrm_get_data(file):
    with open(file, "r", encoding="utf-8") as f:
        ihrm_login_data = json.load(f)

        ihrm_login_data_list = []

        for item in ihrm_login_data:
            temp = tuple(item.values())
            ihrm_login_data_list.append(temp)
    return ihrm_login_data_list


if __name__ == '__main__':
    file = "../data/ihrm_login_data.json"
    data = ihrm_get_data(file)
    print(data)
