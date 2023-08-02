
def user_input():
    user_num = int(input("- "))
    bool_flag(flag=1)
    return start_program()


def start_program():
    print("Pleas input num flag program:")
    while bool_flag == 0:
        print("1 - New Fail")
        print("2 - Read all Fail")
        user_input()


def bool_flag(flag):
    return flag
