class SpaceShip:
    def __init__(self):
        self.fuel = 150 # топливо
        self.hull = 90 # корпус
        self.speed = 0 # скорость

    def refuel(self, sum): # пополняем топливо
        self.fuel += sum

    def damage(self, sum): # при повреждении уменьшаем прочность корпуса
        self.hull -= sum


class CrewMember:
    def __init__(self, name, role):
        self.name = name # имя члена экипажа
        self.role = role # его роль
        self.health = 100 # уровень здоровья

    def heal(self, sum): # восстановление здоровья
        self.health += sum


class Mission:
    def __init__(self, goal):
        self.goal = goal # цель миссии
        self.events = [] # события

    def add_event(self, text): # добавляем события
        self.events.append(text)

    def status(self, ship, comand):
        return f"Цель: {self.goal}, топливо: {ship.fuel}, экипаж: {len(comand)} чел."
