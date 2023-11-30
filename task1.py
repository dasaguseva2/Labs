# TODO Написать 3 класса с документацией и аннотацией типов
import doctest


class Animal:
    def __init__(self, name: str, age: int):
        """
                Создание и подготовка к работе объекта "Животное"

                :param name: Имя животного
                :param age: Возраст животного

                Примеры:
                >>> animal = Animal("Шарик", 5)  # инициализация экземпляра класса
                """
        if not isinstance(name, str):
            raise TypeError("Имя животного должно быть типа str")
        self.name = name

        if not isinstance(age, int):
            raise TypeError("Возраст животного должен быть типа int")
        if age < 0:
            raise ValueError("Возраст животного должен быть положительным числом")
        self.age = age

    def is_adult(self) -> bool:
        """
        Функция, определяющая, является ли животное взрослым (старше 18 лет).

        :return: Является ли животное взрослым
        Примеры:
        >>> animal = Animal("Шарик", 50)
        >>> animal.is_adult()
        True
        """
        return self.age >= 18

    def change_name(self, new_name: str) -> None:
        """
        Изменение имени животного.

        :param new_name: Новое имя животного
        :raise TypeError: Если новое имя не является строкой
        """
        if not isinstance(new_name, str):
            raise TypeError("Новое имя животного должно быть типа str")
        self.name = new_name

    def increase_age(self, years: int) -> None:
        """
        Увеличение возраста животного на определенное количество лет.

        :param years: Количество лет, на которое нужно увеличить возраст животного
        :raise TypeError: Если количество лет не является целым числом
        :raise ValueError: Если количество лет отрицательно
        """
        if not isinstance(years, int):
            raise TypeError("Количество лет должно быть типа int")
        if years < 0:
            raise ValueError("Количество лет должно быть неотрицательным числом")
        self.age += years

    def __str__(self) -> str:
        """
        Строковое представление объекта Animal.

        :return: Строковое представление объекта Animal
        """
        return f"Animal(name={self.name}, age={self.age})"

    def __repr__(self) -> str:
        """
        Представление объекта Animal в виде строки, которая может быть использована для создания нового объекта.

        :return: Представление объекта Animal в виде строки
        """
        return f"Animal(name='{self.name}', age={self.age})"


class Book:
    def __init__(self, title: str, author: str, year: int):
        """
                        Создание и подготовка к работе объекта "Животное"

                        :param title (str): название книги
                        :param author (str): автор книги
                        :param year (int): год издания

                        Примеры:
                        >>> book = Book("Misery", "Stephen King", 1987)  # инициализация экземпляра класса
                        """

        if not isinstance(title, str):
            raise TypeError("Название книги должно быть типа str")
        self.title = title

        if not isinstance(author, str):
            raise TypeError("Автор книги должен быть типа str")
        self.author = author

        if not isinstance(year, int):
            raise TypeError("Год издания должен быть типа int")
        if year <= 0:
            raise ValueError("Год издания должен быть положительным числом")
        self.year = year

    def get_title(self) -> str:
        """
        Получение названия книги
        :return: Название книги

        Примеры:
        >>> book = Book("Misery", "Stephen King", 1987)
        >>> book.get_title()
        'Misery'
        """
        return self.title

    def get_author(self) -> str:
        """
        Получение автора книги
        :return: Автор книги

        Примеры:
        >>> book = Book("Misery", "Stephen King", 1987)
        >>> book.get_author()
        'Stephen King'
        """
        return self.author

    def get_year(self) -> int:
        """
        Получение года издания книги
        :return: Год издания
        Примеры:
        >>> book = Book("Misery", "Stephen King", 1987)
        >>> book.get_year()
        1987
        """
        return self.year

    def set_title(self, title: str) -> None:
        """
        Изменить заголовок книги

        :param title: Новый заголовок
        """
        if not isinstance(title, str):
            raise TypeError("Заголовок книги должен быть типа str")
        self.title = title

    def set_author(self, author: str) -> None:
        """
        Изменить автора книги

        :param author: Новый автор
        """
        if not isinstance(author, str):
            raise TypeError("Автор книги должен быть типа str")
        self.author = author

    def set_year(self, year: int) -> None:
        """
        Изменить год издания книги

        :param year: Новый год издания
        """
        if not isinstance(year, int):
            raise TypeError("Год издания книги должен быть типа int")
        self.year = year
class Vehicle:
    def __init__(self, brand: str, color: str, fuel: str):
        """
        param: brand (str): марка транспортного средства
        param: color (str): цвет транспортного средства
        param: fuel (str): тип топлива
        Примеры:
        >>> vehicle = Vehicle("BMW", "Blue", "Diesel")  # инициализация экземпляра класса
        """
        if not isinstance(brand, str):
            raise TypeError("Марка транспортного средства должна быть типа str")
        if not isinstance(color, str):
            raise TypeError("Цвет транспортного средства должен быть типа str")
        if not isinstance(fuel, str):
            raise TypeError("Тип топлива должен быть типа str")
        self.brand = brand
        self.color = color
        self.fuel = fuel

    def is_brand_vehicle(self) -> bool:
        """
        Функция которая проверяет является ли марка транспортного средства BMW
        :return: Является ли марка транспортного средства BMW

        Примеры:
        >>> vehicle = Vehicle("BMW", "Blue", "Diesel")
        >>> vehicle.is_brand_vehicle()
        True
        """

        return self.brand == "BMW"

    def change_color(self, new_color: str) -> None:
        """
        Изменение цвета транспортного средства.
        :param new_color: Новый цвет транспортного средства

        :raise TypeError: Если новый цвет не является строкой

        Примеры:
        >>> vehicle = Vehicle("BMW", "Blue", "Diesel")
        >>> vehicle.change_color("Red")
        """
        if not isinstance(new_color, str):
            raise TypeError("Новый цвет транспортного средства должен быть типа str")
        self.color = new_color

    def refuel(self, fuel_amount: float) -> None:
        """
        Пополнение топлива в транспортном средстве.
        :param fuel_amount: Количество добавляемого топлива

        :raise ValueError: Если количество добавляемого топлива отрицательное

        Примеры:
        >>> vehicle = Vehicle("BMW", "Blue", "Diesel")
        >>> vehicle.refuel(50)
        """
        if not isinstance(fuel_amount, (int, float)):
            raise TypeError("Количество добавляемого топлива должно быть типа int или float")
        if fuel_amount < 0:
            raise ValueError("Количество добавляемого топлива должно быть положительным числом")
        ...

    def calculate_brand_color(self) -> str:
        """
        Функция, которая возвращает строку с информацией о марке и цвете транспортного средства.

        :return: Информация о марке и цвете транспортного средства

        Примеры:
        >>> vehicle = Vehicle("BMW", "Blue", "Diesel")
        >>> vehicle.calculate_brand_color()
        'Марка транспортного средства: BMW, Цвет транспортного средства: Blue'
        """
        return f"Марка транспортного средства: {self.brand}, Цвет транспортного средства: {self.color}"


if __name__ == "__main__":
    doctest.testmod()  # тестирование примеров, которые находятся в документации
