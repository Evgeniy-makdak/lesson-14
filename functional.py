with open('apache_logs.txt', 'r', encoding='utf-8') as file:
    apache_logs = [_.strip() for _ in file]


def filter_1(user_str: str, list_1: list) -> list:
    return list(filter(lambda x: user_str in x, list_1))


def map_1(number: str, list_1: list) -> list:
    ver = list(map(str.split, list_1))
    return [j[int(number)] for j in ver]


def unique_1(_, list_1: list) -> list:
    return list(set(list_1))


def sort_1(value: str, list_1) -> list:
    flag = False

    if value == 'desc':
        flag = True

    return sorted(list_1, reverse=flag)


def limit_1(number: str, list_1: list) -> list:
    return list_1[:int(number)]


def main(processing_list: list) -> None:
    try:
        for i in input().split('|'):
            user_command, value = i.split()
            if user_command in command_dict:
                processing_list = command_dict[user_command](value, processing_list)
            else:
                print('Неверный ввод данных')
                return
        print(*processing_list, sep='\n')
    except ValueError:
        print('Неверный ввод данных')


command_dict = {'filter': filter_1,
                'map': map_1,
                'unique': unique_1,
                'sort': sort_1,
                'limit': limit_1}

if __name__ == '__main__':
    main(apache_logs)
