from Character import Character


class Elf(Character):
    def __init__(self, name, age, intelligence):
        super().__init__(name, age)
        self.intelligence = intelligence

    def move(self):
        super(Elf, self).move()