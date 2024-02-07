import math
class GeometricFigure:
    def __init__(self, name: str, area: float):
        self.name = name
        self._area = area

    def __str__(self):
        return f"{self.name} with area {self._area}"

    def __repr__(self):
        return f"GeometricFigure({self.name}, {self._area})"

    def get_area(self) -> float:
        return self._area


class Circle(GeometricFigure):
    def __init__(self, radius: float):
        super().__init__("Circle", math.pi * radius ** 2)
        self._radius = radius

    def __str__(self):
        return f"Circle with radius {self._radius}"

    def __repr__(self):
        return f"Circle({self._radius})"

    def get_radius(self) -> float:
        return self._radius
class Vehicle:
    def __init__(self, name: str, speed: float):
        self.name = name
        self._speed = speed

    def __str__(self):
        return f"{self.name} with speed {self._speed}"

    def __repr__(self):
        return f"Vehicle({self.name}, {self._speed})"

    def get_speed(self) -> float:
        return self._speed
class Car(Vehicle):
    def __init__(self, brand: str, model: str, speed: float):
        super().__init__(f"Car {brand} {model}", speed)
        self._brand = brand
        self._model = model

    def __str__(self):
        return f"Car {self._brand} {self._model}"

    def __repr__(self):
        return f"Car({self._brand}, {self._model}, {self._speed})"

    def get_brand(self) -> str:
        return self._brand

    def get_model(self) -> str:
        return self._model

if __name__ == "__main__":
    # Создаем объекты класса Circle и Car
    circle = Circle(5)
    car = Car("Toyota", "Corolla", 120)

    # Выводим информацию о фигуре и транспорте
    print(circle)
    print(car)

    # Получаем площадь круга и скорость автомобиля
    print(f"Area of the circle: {circle.get_area()}")
    print(f"Speed of the car: {car.get_speed()}")

    # Получаем радиус круга и марку и модель автомобиля
    print(f"Radius of the circle: {circle.get_radius()}")
    print(f"Brand of the car: {car.get_brand()}")
    print(f"Model of the car: {car.get_model()}")
    pass