class Database:
    def __init__(self):
        self.data = {}
    def add_user(self, username, password):
        self.data[username] = password


class User:
    """
    Описание класса User
    """
    def __init__(self, username, password, password_confirm):
        self.username = username
        if password == password_confirm:
            self.password = password


if __name__ == '__main__':
    import re
    special_chars = re.compile('[@_!#$%^&*()<>?/\|}{~:]')
    database = Database()
    while True:
        choice = input("Приветствую! Выберите действие: \n1 - Вход\n2 - Регистрация\n")
        user = User(input("Введите логин: "), password := input("Введите пароль: "), password2 := input("Подтвердите пароль: "))
        if password != password2:
            print("Пароль не равен подтверждению пароля")
            exit()
        elif len(password) < 8:
            print("Длина пароля менее 8 символов")
            exit()
        elif not any(char.isdigit() for char in password):
            print("Пароль не содержит цифры")
            exit()
        elif not any(char.islower() for char in password):
            print("Пароль не содержит символы в нижнем регистре")
            exit()
        elif not any(char.isupper() for char in password):
            print("Пароль не содержит символы в верхнем регистре")
            exit()
        elif not special_chars.search(password):
            print("Пароль не содержит специальных символов")
            exit()

        database.add_user(user.username, user.password)
        print(database.data)

