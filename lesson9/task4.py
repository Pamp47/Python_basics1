class Car:
    def __init__(self, name, color, is_police, speed):
        self.name = name
        self.color = color
        self.speed = speed
        self.is_police = is_police

    def go(self):
        print("Поехали")

    def stop(self):
        print("Тормозим")

    def turn(self, direction):
        print(f"Поворачиваем {direction}")

    def show_speed(self):
        print(f"Скорость: {self.speed}")


class TownCar(Car):
    speed_limit = 60

    def __init__(self, name, color, speed):
        super().__init__(name, color, False, speed)

    def show_speed(self):
        print(f"Скорость: {self.speed}")
        if self.speed >= self.speed_limit:
            print("Превышение скорости")


class WorkCar(Car):
    speed_limit = 40

    def __init__(self, name, color, speed):
        super().__init__(name, color, False, speed)

    def show_speed(self):
        print(f"Скорость: {self.speed}")
        if self.speed >= self.speed_limit:
            print("Превышение скорости")


class SportCar(Car):
    def __init__(self, name, color, speed):
        super().__init__(name, color, False, speed)


class PoliceCar(Car):
    def __init__(self, name, color, speed):
        super().__init__(name, color, True, speed)


tc = TownCar("Mercedes", "black", 150)
wc = TownCar("Газель", "orange", 80)
pc = PoliceCar("Лада", "white", 100)

tc.show_speed()
wc.show_speed()
pc.show_speed()

tc.go()
tc.stop()
tc.turn("Направо")
tc.turn("Налево")

print(pc.is_police)
