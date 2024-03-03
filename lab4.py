import time
from abc import ABC, abstractmethod
import sys
class Command(ABC):

    @abstractmethod
    def execute(self):
        pass

    @abstractmethod
    def undo(self):
        pass


class Action1(Command):
    def execute(self):
        print("Выполнено действие 1", end="")

    def undo(self):
        sys.stdout.write('\r')
        sys.stdout.write('\r')


class Action2(Command):
    def execute(self):
        print("Выполнено действие 2", end="")

    def undo(self):
       sys.stdout.write('\r')
       sys.stdout.write('\r')


class Action3(Command):
    def execute(self):
        print("Выполнено действие 3", end="")

    def undo(self):
        sys.stdout.write('\r')
        sys.stdout.write('\r')


class Actions:
    def __init__(self):
        self.actions = {}  # Словарь для хранения назначенных действий
        self.history = []  # Список для отслеживания последних выполненных действий

    def assign_action(self, key, action):#
        """Назначает действия на определенную клавишу"""
        self.actions[key] = action
        print(f"\nКлавиша {key} назначена на действие {action.__class__.__name__}")

    def press_key(self, key):
        """Вызовает действия по нажатию клавишы"""
        if key in self.actions:
            action = self.actions[key]  # Получаем соответствующее действие
            print(f"\nНажата клавиша {key}")
            action.execute()
            self.history.append(action)  # Добавляем действие в историю
        else:
            print(f"\nНа клавишу {key} не назначено действия")


    def undo_last_action(self):
        """Отменяет последнее действие"""
        if self.history:
            action = self.history.pop()
            action.undo()
            print(f"\nОтменено действие {action.__class__.__name__}")
        else:
            print(f"\nИстория пуста")

    def break_connection(self, key):
        """Разрывает связь клавишы и действия"""
        if key in self.actions:
            del self.actions[key]
            print(f"\nНа клавишу {key} больше ничего не назначено")
        else:
            print(f"\nНа клавишу {key} не назначено действия")


# Пример использования
if __name__ == '__main__':
    actions = Actions()

    actions.assign_action("F1", Action1())
    actions.press_key("F1")  # Выполнено действие 1
    time.sleep(3)
    actions.undo_last_action()

    time.sleep(3)
    actions.assign_action("Ctrl+Alt+X", Action2())
    actions.assign_action("Shift+Z", Action3())
    actions.press_key("F1")  # Выполнено действие 1
    time.sleep(3)

    actions.press_key("Ctrl+Alt+X")  # Выполнено действие 2
    time.sleep(3)

    actions.press_key("Shift+Z")  # Выполнено действие 3
    time.sleep(3)

    actions.undo_last_action()  # Отменено действие 3
    time.sleep(3)

    actions.assign_action("F1", Action3())
    actions.assign_action("Ctrl+Alt+X", Action1())

    actions.undo_last_action()
    actions.press_key("F1")  # Выполнено действие 3
    time.sleep(3)
    actions.break_connection("F1")
    time.sleep(3)
    actions.press_key("F1")
    time.sleep(3)

    actions.press_key("Ctrl+Alt+X")  # Выполнено действие 1
    time.sleep(3)