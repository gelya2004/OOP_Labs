class User:
    def __init__(self, name, login, password, bd):
        self.__name = name
        self.__bd = bd # название базы данных в которой хранится пользователь
        self.__login = login
        self.__password = password
        self.__autorisatiion = False  # Состояние авторизованности сохранил ли пользователь куки для быстрого входа
        self.__state = False  # Состояние пользователя (True - зашел в кабинет, False - вышел)

    def getName(self):
        return self.__name

    def getLogin(self):
        return self.__login

    def getPassword(self):
        return self.__password

    def _getBd(self):
        return self.__bd

    def getAutorization(self):
        return self.__autorisatiion

    def getState(self):
        return self.__state

    def setState(self, state):
        self.__state = state
        if not state:
            print("Вы вышли из аккаунта!")
        else:
            print("Здравствуйте, " + self.__name)

    def setAutorization(self, state):
        self.__autorisatiion = state


class IUserManager(User):
    def LogIn(self):
        if self._getBd().SearchEqualsLogin(self.getLogin()):
            print("!!!Пользователь с таким логином уже существует!!!")
            return False
        else:
            self.Autorization()
            return True

    def SignIn(self):
        self.setState(True)

    def SignOut(self):
        self.setState(False)

    def Autorization(self):
        print("Запомнить меня? ('Да' или 'Нет')")
        if YesOrNO():
            self.setAutorization(True)


class IUserRepository():
    def __init__(self):
        self.__bdUsers = []

    def getBdUsers(self):
        return self.__bdUsers

    def addOnBd(self, user):
        self.__bdUsers.append(user)

    def SearchEqualsLogin(self, login):
        for user in self.__bdUsers:
            if user.getLogin() == login:
                return True
        return False

    def SearchUser(self, login, password):
        for user in self.__bdUsers:
            if user.getLogin() == login:
                if user.getPassword() == password:
                    if user.getAutorization():
                        user.setState(True)
                    else:
                        user.Autorization()
                        user.setState(True)
                    return user
        return None

    def GetByLogin(self, login):
        for user in self.__bdUsers:
            if user.getLogin() == login:
                return user


def YesOrNO():
    while True:
        answer = str(input())
        if answer == "Да":
            return True
        if answer == "Нет":
            return False


if __name__ == '__main__':
    bd = IUserRepository()
    testuser = IUserManager("TestName", "TestLogin", "Test", bd)
    testuser.setAutorization(True)
    bd.addOnBd(testuser)

    run = True
    AdminFlag = False
    UserFlag = False

    while run:
        print("Добро пожаловать!")
        print("1 - admin")
        print("2 - user")
        print("3 - Выйти")
        step = int(input())
        if step == 1:
            AdminFlag = True
        if step == 2:
            UserFlag = True
        if step == 3:
            run = False
        while AdminFlag:
            print("-----------ADMIN-----------")
            print("1 - Вывести всех пользователей")
            print("2 - Найти пользователя по логину")
            print("3 - Выйти")
            step = int(input())
            if step == 1:
                for i in range(len(bd.getBdUsers())):
                    print(f"-----------------{i+1}---------------------")
                    print(f" username - {bd.getBdUsers()[i].getName()}")
                    print(f" login - {bd.getBdUsers()[i].getLogin()}")
                    print(f" password - {bd.getBdUsers()[i].getPassword()}")
                    print(f" auth - {bd.getBdUsers()[i].getAutorization()}")
                    print(f" state - {bd.getBdUsers()[i].getState()}")
                    print("--------------------------------------")
            if step == 2:
                print("Введите логин!")
                login = str(input())
                user1 = bd.GetByLogin(login)
                if user1 is not None:
                    print(f" username - {user1.getName()}")
                    print(f" login - {user1.getLogin()}")
                    print(f" password - {user1.getPassword()}")
                    print(f" auth - {user1.getAutorization()}")
                    print(f" state - {user1.getState()}")
                else:
                    print("Такого пользователя не существует!")
        while UserFlag:
            print("Панель Пользователя")
            print("1 - Зарегистрироваться")
            print("2 - Войти")
            print("3 - Назад")
            step = int(input())
            if step == 1:
                print("Введите ваше Имя!")
                name = str(input())
                print("Введите логин!")
                login = str(input())
                print("Введите ваш пароль!")
                passord = str(input())
                user = IUserManager(name, login, passord, bd)
                state = user.LogIn()
                if state:
                    bd.addOnBd(user)
            if step == 2:
                print("Вы авторизованы? ('Да' или 'Нет')")
                if YesOrNO():
                    users = bd.getBdUsers()
                    mas_id = []
                    a = 0
                    for i in range(len(users)):
                        if users[i].getAutorization():
                            mas_id.append(i)
                            print((a + 1), " - ", users[i].getLogin())
                            a += 1
                    step2 = int(input())
                    step2 -= 1
                    users[mas_id[step2]].SignIn()
                    while True:
                        print("Других функций как выйти больше нет(")
                        print("1 - Выйти")
                        if int(input()) == 1:
                            users[mas_id[step2]].SignOut()
                            break
                else:
                    print("Введите логин!")
                    login = str(input())
                    print("Введите ваш пароль!")
                    passord = str(input())
                    tempUser = bd.SearchUser(login, passord)
                    if tempUser is not None:
                        tempUser.SignIn()
                        while True:
                            print("Других функций как выйти больше нет(")
                            print("1 - Выйти")
                            if int(input()) == 1:
                                tempUser.SignOut()
                                break
                    else:
                        print("Неправильно введенный логин или пароль!")
            if step == 3:
                UserFlag = False