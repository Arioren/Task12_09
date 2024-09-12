class Aircraft:
    def __init__(self, type, speed, fule_capacity):
        self.type = type
        self.speed = speed
        self.fule_capacity = fule_capacity

    def __repr__(self):
        return f"type: {self.type}, speed: {self.speed}, fule_capacity: {self.fule_capacity}"