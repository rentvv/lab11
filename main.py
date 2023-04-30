def z1():
    class restaurant:
        def __init__(self, name, type):
            self.name = name
            self.type = type
        def restoran(self):
            print(f"название ресторана: {self.name}")
            print(f"тип кухни: {self.type}")
        def open_restoran(self):
            print("ресторан открыт!")

    newrest = restaurant("RestoClub", "европейская")
    print(newrest.name)
    print(newrest.type)
    print()
    newrest.restoran()
    newrest.open_restoran()

#z1()


def z2():
    class restaurant:
        def __init__(self, name, type):
            self.name = name
            self.type = type

        def restoran(self):
            print(f"название ресторана: {self.name}")
            print(f"тип кухни: {self.type}")


    res_1 = restaurant("Чечил", "грузинская")
    res_2 = restaurant("KFC", "фаст фуд")
    res_3 = restaurant("BenBar", "тайская")

    res_1.restoran()
    print()
    res_2.restoran()
    print()
    res_3.restoran()

#z2()

def z3():
    class restaurant:
        def __init__(self, name, type, rating=0):
            self.name = name
            self.type = type
            self.rating = rating

        def restoran(self):
            print(f"название ресторана: {self.name}")
            print(f"тип кухни: {self.type}")

        def openrest(self):
            print(f"ресторан открыт!")

        def oldrating(self, rating):
            self.rating = rating
            print(f"рейтинг: {self.rating}")

        def newrat(newrat):
            newrat.rating = float(input('введите новое значение рейтинга: '))
            print()
            newrest = restaurant("RestoClub", "европейская")
            newrest.restoran()
            newrest.openrest()
            print(f"рейтинг обновлен: {newrat.rating}")

    newrest = restaurant("RestoClub", "европейская")
    newrest.restoran()
    newrest.openrest()
    newrest.oldrating(3.5)
    print()
    newrest.newrat()

z3()
