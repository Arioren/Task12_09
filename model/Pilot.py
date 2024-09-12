class Pilot:
    def __init__(self, name, skill):
        self.name = name
        self.skill = skill

    def __repr__(self):
        return f"name: {self.name}, skill: {self.skill}"