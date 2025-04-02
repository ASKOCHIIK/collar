class Mentor:
    def __init__(self, name: str, last_name: str):
        self.name = name
        self.last_name = last_name

    def info(self):
        return f'Hi my name is {self.name}\nMy last name {self.last_name}'

class Lecturer(Mentor):
    def __init__(self,  name: str, last_name: str):
        super().__init__(self, name, last_name)

Rachid = Lecturer("Rachid", "dfsk")
