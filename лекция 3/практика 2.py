class Transport:
    def describe(self):
        return "Это любое траспортное средство"


class Car(Transport):
    def describe(self):
        return "Это машина, в которой комфортнее всего ездить"


class Bus(Transport):
    def describe(self):
        return "Это автобус, который не так комфортен, как машина, но тоже норм"


class Train(Transport):
    def describe(self):
        return "Это поезд, самый атмосферный вид траспорта"


all_together = [Car(), Bus(), Train()]
for together in all_together:
    print(together.describe())