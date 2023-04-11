class ITEM:
    def __init__(self, id, weight, value):
        self.id = int(id)
        self.weight = int(weight)
        self.value = int(value)

    def __str__(self):
        return f'weight: {self.weight}, value: {self.value}'