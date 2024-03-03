class Array3d:
    def __init__(self, width, height, depth, values):
        self.__width = width  # ширина
        self.__height = height  # высота
        self.__depth = depth  # глубина
        self.__values = values
        self.__length = width * height * depth  # общая длина нашего одномерного массива хранящегося внутри класса
        self.__data = [values] * self.__length  # заполняем наш массив значениями int

    def __transform_index(self, x, y, z):  # преобразование трехмерного индекса в одномерный индекс
        return x + self.__width * (y + self.__height * z)

    def __str__(self):  # Переопределяем написание массива
        result = ""
        for z in range(self.__depth):
            result += f"Глубина: {z}\n"
            for y in range(self.__height):
                for x in range(self.__width):
                    result += f"{self.data[self.__transform_index(x, y, z)]} "
                result += "\n"
            result += "\n"
        return result

    ################ Get
    def GetValues_Once(self, z):  # Получаем значение по 1 приближению (двумерный массив)
        result = ""
        for y in range(self.__height):
            result += "\n"
            for x in range(self.__width):
                result += f"{self.data[self.__transform_index(x, y, z)]}"
        return result

    def GetValues_Twice(self, z, y):  # Получаем значение по 2 приближению (одномерный массив)
        result = ""
        for x in range(self.__width):
            result += f"{self.data[self.__transform_index(x, y, z)]} "
        return result

    def GetValues_Thrice(self, z, y, x):  # Получаем значение по 3 приближению (Значение)
        result = f"{self.data[self.__transform_index(x, y, z)]} "
        return result

    ################### Set

    def SetValues_Once(self, z, array):  # В 1 приближении на 0 элемент ставим двумерный массив [[3,3,3],[3,3,3],[3,3,3]]
        for y in range(self.__height):
            for x in range(self.__width):
                 self.data[self.__transform_index(x, y, z)] = array[y][x]

    def SetValues_Twice(self, z, y, array):  # В 2 приближении на элемент [0][0] ставим одномерный массив [3,3,3]
        for x in range(self.__width):
            self.data[self.__transform_index(x, y, z)] = array[x]

    def SetValues_Thrice(self, z, y, x, value):  # В 3 приближение на элемент [0][0][0] ставим значение 1
        self.data[self.__transform_index(x, y, z)] = value

    def npfill(self, values):  # заполнение массива одинаковыми элементами values
        self.data = [values] * self.__length

###################

if __name__ == '__main__':
    array = Array3d(3, 3, 3, 10)
    array.npfill(0)   # заполнение массива одинаковыми элементами values
    # array[0, 0, 0] = 1
    # array[1, 1, 1] = 8
    # array.SetValues_Once(0, [[3, 3, 3],
    #                          [3, 3, 3],    # В 1 приближении на 0 элемент ставим двумерный массив [[3,3,3],[3,3,3],[3,3,3]]
    #                          [3, 3, 3]])
    # array.SetValues_Twice(0, 0, [3, 3, 3])  # В 2 приближении на элемент [0][0] ставим одномерный массив [3,3,3]
    array.SetValues_Thrice(0, 0, 0, 1)  # В 3 приближение на элемент [0][0][0] ставим значение 1
    array.SetValues_Thrice(1, 1, 1, 8)
    print(array.GetValues_Once(0))  # Получаем значение по 1 приближению (двумерный массив)
    print('/////////////////')
    print(array.GetValues_Twice(0, 0))  # Получаем значение по 2 приближению (одномерный массив)
    print('/////////////////')
    print(array.GetValues_Thrice(0, 0, 0))  # Получаем значение по 3 приближению (Значение)
    print('/////////////////')
    print('?????????????????')

    print(array.GetValues_Once(0))

    # print(array.SetValues_Once(0, [[3, 3, 3],
    #                                [3, 3, 3],
    #                                [3, 3, 3]]))
    # print(array.SetValues_Twice(0, 2, [3, 3, 3]))
    print(array.GetValues_Once(0))

    print(array)  # Печатаем весь массив магическим методом __str__