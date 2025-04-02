class Mentor:
    def __init__(self, name: str, last_name: str):
        self.name = name
        self.last_name = last_name

    def info(self):
        return f'Hi my name is {self.name}\nMy last name {self.last_name}'


class Bak(Mentor):
    def __init__(self):
        super().__init__('Baktybai', 'Sulaimanov')

mentor = Mentor('Askat', 'Kulmanov')
bak = Bak()

print(bak.info())


