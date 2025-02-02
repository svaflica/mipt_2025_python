from .modules.get import get_dict


def get_data():
    return get_dict()


# Не работает
# __init__ не может иметь точки входа
#
# if __name__ == '__main__':
#     get_data()