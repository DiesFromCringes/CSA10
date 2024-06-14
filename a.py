class Animal:
    age = 0.5
    def __init__(self, name):
        self.name = name

        def talk():
            print('talk')
cuu = Animal(name='xyz')
print(cuu.name)
cuu.talk()