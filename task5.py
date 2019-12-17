import os

database = []


class Employee:
    def __init__(self, employee_id=0, city='', first_name='', second_name='', age=0, gender=''):
        self.employee_id = employee_id
        self.first_name = first_name
        self.second_name = second_name
        self.city = city
        self.age = age
        self.gender = gender

    @staticmethod
    def check_str(name):
        return name != ''

    @staticmethod
    def check_age(age):
        return 10 < age < 120

    @staticmethod
    def check_gender(gender):
        return gender == 'm' or gender == 'f' or gender == 'o'

    def create(self):
        while not self.check_str(self.first_name):
            self.first_name = input('Input first name: ')
            if not self.check_str(self.first_name):
                print("invalid name")

        while not self.check_str(self.first_name):
            self.first_name = input('Input first name: ')
            if not self.check_str(self.first_name):
                print("invalid name")

        while not self.check_str(self.second_name):
            self.second_name = input('Input second name: ')
            if not self.check_str(self.second_name):
                print("invalid name")

        while not self.check_gender(self.gender):
            self.gender = input('Input gender: ')
            if not self.check_gender(self.gender):
                print("invalid gender")

        while not self.check_age(self.age):
            self.age = int(input('Input age: '))
            if not self.check_age(self.age):
                print("invalid age")

        while not self.check_str(self.city):
            self.city = input('Input city: ')
            if not self.check_str(self.city):
                print("invalid name")

        return self


class Student(Employee):
    def __init__(self, employee_id: int):
        self.type = 'student'
        super().__init__(employee_id)


class Tutor(Employee):
    def __init__(self, employee_id: int):
        self.type = 'tutor'
        super().__init__(employee_id)


def make_menu(menu_items):
    os.system('clear')

    for item in menu_items:
        print("[" + str(menu_items.index(item)) + "] " + item["title"])
    choice = input(">> ")
    try:
        if int(choice) < 0: raise ValueError
        menu_items[int(choice)]["fn"]()
    except (ValueError, IndexError):
        pass


def new_employee():
    make_menu(choose_type_items)


def add_tutor():
    os.system('clear')
    employee_id = 0
    while not check_uniq(employee_id):
        employee_id = input('Input employee id: ')
        if not check_uniq(employee_id):
            print("invalid id")
    database.append(Tutor(employee_id).create())
    save()
    success()


def add_student():
    os.system('clear')
    employee_id = 0
    while not check_uniq(employee_id):
        employee_id = input('Input employee id: ')
        if not check_uniq(employee_id):
            print("invalid id")
    database.append(Student(employee_id).create())
    save()
    success()


def success():
    print("Employee saved successfully")
    input("Press [Enter] for return to main menu")


def make_header():
    return f"""
ID    | Type    |  Name      | Surname    | Gender | Age  | City   |
--------------------------------------------------------------------
"""


def make_row(item):
    return f"{str(item.employee_id):5} | {item.type:7} | {item.first_name:10} | {item.second_name:10} | {item.gender:6} | {str(item.age):>3}  | {item.city:10} |\n"


def check_uniq(employee_id):
    if employee_id == 0:
        return False

    flag = True

    for item in database:
        if item.employee_id == employee_id:
            flag = False

    return flag


def main():
    while True:
        make_menu(main_menu_items)


def show(employee_id=0, employee_type='all'):
    os.system('clear')
    flag = False
    data = make_header()
    for item in database:
        if (employee_id == 0 and employee_type == 'all') or (employee_id != 0 and item.employee_id == employee_id) or (
                employee_type != 'all' and item.type == employee_type):
            data += make_row(item)
            flag = True

    if not flag:
        data += 'No records \n'

    print(data)
    input("Press [Enter] for return to main menu")


def show_all():
    show()


def show_tutors():
    show(0, 'tutor')


def show_students():
    show(0, 'student')


def show_moscow():
    os.system('clear')
    count = 0
    for item in database:
        if item.city == 'Moscow' or item.city == 'moscow':
            count += 1
            flag = True

    if count == 0:
        data = 'No records \n'
    else:
        data = 'Employee in Moscow: ' + str(count) + '\n'

    print(data)
    input("Press [Enter] for return to main menu")


def show_one():
    employee_id = -1
    while check_uniq(employee_id):
        employee_id = input('Input employee id: ')
        if check_uniq(employee_id):
            print("invalid id")
    show(employee_id, 'all')


def save():
    data = make_header()
    f = open('db.txt', 'w')
    for item in database:
        data += make_row(item)
    f.write(data)
    f.close()


def edit():
    employee_id = -1
    index = -1
    while check_uniq(employee_id):
        employee_id = input('Input employee id: ')
        if check_uniq(employee_id):
            print("invalid id")

    for idx, item in enumerate(database):
        if item.employee_id == employee_id:
            index = idx

    if database[index].type == 'tutor':
        database[index] = Tutor(employee_id).create()
        save()
        success()
    elif database[index].type == 'student':
        database[index] = Student(employee_id).create()
        save()
        success()


main_menu_items = [
    {"title": "Add Item", "fn": new_employee},
    {"title": "Show All", "fn": show_all},
    {"title": "Show Only Tutors", "fn": show_tutors},
    {"title": "Show Only Students", "fn": show_students},
    {"title": "Show Item by ID", "fn": show_one},
    {"title": "Show How many in Moscow", "fn": show_moscow},
    {"title": "Edit Item by ID", "fn": edit},
    {"title": "Exit", "fn": exit},
]

choose_type_items = [
    {"title": "Add Tutor", "fn": add_tutor},
    {"title": "Add Student", "fn": add_student},
    {"title": "Back to main menu", "fn": lambda *a, **k: None},
]

if __name__ == "__main__":
    main()
