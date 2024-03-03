class Fract:
    #инициализируем данные в классе дробей
    #используем магические методы питона
    def __init__(self, num, denom):
        self.__num = num
        self.__denom = denom

    def __str__(self): # вызываем принт, чтобы печатались данные, а не объекты
            return str(self.__num) + '/' + str(self.__denom)

    def decimal_fract(self): # перевод в десятичную дробь
            return round(self.__num / self.__denom, 6) #округление до 6 знаков после ,

    def __add__(self, other): #сложение
            new_num = self.__num * other.__denom + other.__num * self.__denom
            new_denom = self.__denom * other.__denom
            degree = reduction(new_num, new_denom)
            return Fract(new_num // degree, new_denom // degree) #degree - НОД

    def __sub__(self, other): #вычитание
            new_num = self.__num * other.__denom - other.__num * self.__denom
            new_denom = self.__denom * other.__denom
            degree = reduction(new_num, new_denom)
            return Fract(new_num // degree, new_denom // degree)

    def __mul__(self, other): #умножение
            new_num = self.__num * other.__num
            new_denom = self.__denom * other.__denom
            degree = reduction(new_num, new_denom)
            return Fract(new_num // degree, new_denom // degree)

    def __floordiv__ (self, other): #деление
            new_num = self.__num * other.__denom
            new_denom = self.__denom * other.__num
            degree = reduction(new_num, new_denom)
            return Fract(new_num // degree, new_denom // degree)

        # сравниваем дроби магическими методами
    def __ne__(self, other): #неравенсвтво
            return(self.__num * other.__denom) != (other.__num * self.__denom)

    def __eq__(self, other): #равенство
            return (self.__num * other.__denom) == (other.__num * self.__denom)

    def __gt__(self, other):  #проверка, больше ли первая
            return str(self.__num * other.__denom) > str(other.__num * self.__denom)

    def __lt__(self, other): #проверка, меньше ли первая
            return (self.__num * other.__denom) < (other.__num * self.__denom)

def reduction(m, n): #функция для сокращения дробей
    while m % n != 0:
        m, n = n, m % n
    return n

#функция проверки корректности, если числа не int то выдаст ошибку
def CorrectNumber():
    while True:
        try:
            num = int(input())
            return num
        except Exception:
            print("Неправильный ввод")

if __name__ == "__main__":
    print("Введите дробь двумя числами")
    f1 = Fract(CorrectNumber(), CorrectNumber())
    print("Введите дробь двумя числами")
    f2 = Fract(CorrectNumber(), CorrectNumber())
    print(f"f1={f1} f2={f2}")
    print(f" Сумма = {f1 + f2}")
    print(f"Десятичная дробь от суммы = {(f1 + f2).decimal_fract()}")
    print(f"Разность = {f1 - f2}")
    print(f"Произведение - {f1 * f2}")
    print(f"Деление = {f1 // f2}")
    print(f"функция f1 не равна f2 = {f1 != f2}")
    print(f"функция f1 равна f2 = {f1 == f2}")
    print(f"функция f1 больше f2 = {f1 > f2}")
    print(f"функция f1 меньше f2 = {f1 < f2}")