import os


# pin = ""
# myfile = open("pass.txt", "r")
# for i in myfile:
#     pin = str(i)
# myfile.close()
# print(f"Your pin code {pin}")
def show_main_screen():
    print("ВЫБЕРИТЕ ДЕЙСТВИЕ,НАЖАВ СООТВЕТСТВУЮЩУЮ ЦИФРУ:")
    print("=" * 30)
    print("1.СНЯТЬ НАЛИЧНЫЕ")
    print("2.ПРОСМОТРЕТЬ БАЛАНС")
    print("3.ВЕРНУТЬ КАРТУ")
    print("=" * 30)
    user_select = input("ВАШ ВЫБОР:>")
    clear_screen()
    return user_select


def show_get_cashe_screen():
    print("ВЫБЕРИТЕ ДЕЙСТВИЕ,НАЖАВ СООТВЕТСТВУЮЩУЮ ЦИФРУ:")
    print("=" * 30)
    print("1.СНЯТЬ 10 РУБЛЕЙ ")
    print("2.СНЯТЬ 20 РУБЛЕЙ")
    print("3.СНЯТЬ 50 РУБЛЕЙ")
    print("4.СНЯТЬ 100 РУБЛЕЙ")
    print("5.СНЯТЬ 200 РУБЛЕЙ")
    print("6.ДРУГАЯ СУММА")
    print("7.ВЫЙТИ В ГЛАВНОЕ МЕНЮ")
    print("=" * 30)
    user_select = input("ВАШ ВЫБОР:>")
    clear_screen()
    return user_select


def show_user_authorization_screen():
    user_pin = input("ВВЕДИТЕ ВАШ PIN-КОД:>")
    myfile = open("pass.txt", "r")
    for i in myfile:
        pin = str(i)
    myfile.close()
    if pin == user_pin:
        return True
    else:
        return False

def user_authoriation():
    if show_user_authorization_screen():
        print("TRUE")
    else:
        print("FALSE")

def show_check_balance_screen():
    pass


def show_exit_screen():
    print("ЗАБЕРИТЕ ВАШУ КАРТУ")
    input()
    clear_screen()

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')


# ================================================================================
show_main_screen()
show_get_cashe_screen()
show_exit_screen()

