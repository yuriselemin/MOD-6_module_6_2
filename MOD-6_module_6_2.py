
class Vehicle:
    _COLOR_VARIANTS = ['blue', 'red', 'green', 'black', 'white']

    def __init__(self,owner, model, color, engine_power):
        self.__model = model
        self.__engine_power = engine_power
        self.__color = color
        self.owner = owner

    def get_model(self):
        return self.__model

    def get_horsepower(self):
        return self.__engine_power

    def get_color(self):
        return self.__color

    def print_info(self):
        print(f"Модель: {self.get_model()}")
        print(f"Мощность двигателя: {self.get_horsepower()}")
        print(f"Цвет: {self.get_color()}")
        print(f"Владелец: {self.owner}")

    def set_color(self, new_color):
        if new_color.lower() in self._COLOR_VARIANTS:
            self.__color = new_color
        else:
            print("Нельзя сменить цвет на", new_color)




class Sedan(Vehicle):
    PASSENGERS_LIMIT = 5

    def __init__(self,owner, model, color, engine_power):
        super().__init__(owner, model, color, engine_power)

    def print_info(self):
        print(f"Тип: Седан | Пассажировместимость: {self.PASSENGERS_LIMIT}")
        super().print_info()


if __name__ == "__main__":
    vehicle1 = Sedan('Fedos', 'Toyota Mark II', 'blue', 500)
    vehicle1.print_info()

    # Меняем свойства
    vehicle1.set_color('Pink')
    vehicle1.set_color('BLACK')
    vehicle1.owner = 'Vasyok'

    # Проверяем что поменялось
    vehicle1.print_info()