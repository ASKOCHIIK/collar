class Mentor:
    def __init__(self, name: str, last_name: str):
        self.name = name
        self.last_name = last_name

    def info(self):
        return f'Hi my name is {self.name}\nMy last name {self.last_name}'
class Malika(Mentor):
    def __init__(self, name: str, last_name: str, age: int):
        super().__init__(name, last_name)
        self.age = age
malika= Malika("Malika", "raimbekova", 14)

