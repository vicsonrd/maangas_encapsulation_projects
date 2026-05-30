class Pet:
    def __init__(self) -> None:
        self.__name: str = ""
        self.__animal_type: str = ""
        self.__age: int = 0

    def set_name(self, name: str) -> None:
        self.__name = name

    def set_animal_type(self, animal_type: str) -> None:
        self.__animal_type = animal_type

    def set_age(self, age: int) -> None:
        self.__age = age

    def get_name(self) -> str:
        return self.__name

    def get_animal_type(self) -> str:
        return self.__animal_type

    def get_age(self) -> int:
        return self.__age