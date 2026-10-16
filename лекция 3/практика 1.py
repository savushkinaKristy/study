class Employee:
    def __init__(self, id, name, base_money):
        self.id = id
        self.name = name
        self.base_money = base_money

    def calculate_salaries(self):
        return self.base_money

class Manage(Employee):
    def __init__(self, id, name, base_money, bonus):
        super().__init__(id, name, base_money)
        self.bonus = bonus

    def calculate_salaries(self):
        return self().base_money + self.bonus


class Developer(Employee):
    def __init__(self, id, name, base_money, project_sum):
        super().__init__(id, name, base_money)
        self.project_sum = project_sum

    def calculate_salaries(self):
        return self.base_money + (self.project_sum * 0.3) # 30% от суммы проекта