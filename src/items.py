class Item():
    def __init__(self, name, description, value):
        self.name = name
        self.description = description = description
        self.value = value

    def __str__(self):
        return f'{self.name}\n{self.description}\nValue: {self.value}'

# class Gold(Item):
#     def __init__(self, amt):
#         self.amt = amt
#         super().__init__(name="Gold", description=f"A small round gold coin valued at {self.amt}", value=self.amt)

# class Gem(Item):
#     def __init__(self, amt, color):
#         self.amt = amt
#         self.color = color
