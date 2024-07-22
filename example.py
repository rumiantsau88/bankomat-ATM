# my_dict = {'my_key': "afsdfsd",
#            'your_key': 'jhskfssd',
#            'their_key': 'Khsdyu67u26&'
#            }
# print(my_dict['my_key'])
#
# my_list = [['first', 1], ['second', 2], ['third', 3]]
# my_second_dict = dict(my_list)
# print(my_second_dict)
class Car:
    __object_color = ''
    __object_count_of_wheels = 4
    __object_vendor = ''
    __object_model = ''

    def __init__(self, count_wheels=4, color='none', vendor='noname', model='noname'):
        self.__object_model = model
        self.__object_color = color
        self.__object_vendor = vendor
        self.__object_count_of_wheels = count_wheels

    def print_properties(self):
        print(f'Производитель машины:\t{self.__object_vendor}')
        print(f'Цвет машины:\t\t\t{self.__object_color}')
        print(f'Модель машины:\t\t\t{self.__object_model}')
        print(f'Количество колес:\t\t{self.__object_count_of_wheels}')


new = Car(6, 'white', 'Mercedes', 's-600')

new.print_properties()



