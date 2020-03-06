class Animal:

    def __init__(self):
        pass

    def make_a_sound(self, species):
        if species == "cat":
            print("meow")
        elif species == "dog":
            print("woof, woof")
        elif species == "fox":
            print("timtirimtim")
        else:
            print("Don't know that animal")


my_animal = Animal()
my_animal.make_a_sound("cat")
