class Car:
    def __init__(self, year_model: str, make: str) -> None:
        self.__year_model: str = year_model
        self.__make: str = make
        self.__speed: int = 0

    def accelerate(self) -> None:
        self.__speed += 5

    def brake(self) -> None:
        self.__speed -= 5
        if self.__speed < 0:
            self.__speed = 0

    def get_speed(self) -> int:
        return self.__speed