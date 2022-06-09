class Stationery:
    def __init__(self, title):
        self.title = title

    def draw(self):
        print("Запуск отрисовки")


class Pen(Stationery):
    def draw(self):
        print(f"{self.title}: ", end="")
        super().draw()


class Pencil(Stationery):
    def draw(self):
        print(f"{self.title}: ", end="")
        super().draw()


class Handle(Stationery):
    def draw(self):
        print(f"{self.title}: ", end="")
        super().draw()


p1 = Pen("Ручка")
p1.draw()
p2 = Pencil("Карандаш")
p2.draw()
p3 = Handle("Маркер")
p3.draw()
