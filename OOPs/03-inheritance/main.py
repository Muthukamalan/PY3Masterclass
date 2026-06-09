class Animal:
    def __init__(self, name="Animal"):
        self.name = name
        print(f"Animal.__init__({name})")
        super().__init__()  # crucial for diamond pattern

    def speak(self):
        print(f"{self.name}: generic animal sound")


# ┌────────────────────────────────────────────────────┐
# │ 1) Single inheritance branches (two parents)       │
# └────────────────────────────────────────────────────┘
class Dog(Animal):
    def __init__(self, name="Dog"):
        # parent class calls first
        super().__init__(name)
        print(f"Dog.__init__({name})")

    def speak(self):
        print(f"{self.name}: woof!")


class Pet(Animal):
    def __init__(self, name="Pet"):
        # parent class calls first
        super().__init__(name)
        print(f"Pet.__init__({name})")

    def care(self):
        print(f"{self.name} is being cared for.")


# ┌────────────────────────────────────────────────────┐
# │ 2) Diamond class: inherits from both Dog and Pet   │
# │     → this is the diamond problem scenario         │
# └────────────────────────────────────────────────────┘
class DogPet(Dog, Pet):
    def __init__(self, name="DogPet"):
        # parent class calls first
        super().__init__(name)   # ← walks the MRO once, not twice
        print(f"DogPet.__init__({name})")

    def status(self):
        print(f"{self.name} is both a dog and a pet.")


if __name__ == "__main__":


    # ┌────────────────────────────────────────────────────┐
    # │ 3) Show MRO and run the diamond                    │
    # └────────────────────────────────────────────────────┘
    print("MRO for DogPet:")
    for cls in DogPet.__mro__:
        print("    ", cls.__name__)

    print("\nCreating DogPet instance:")
    dogpet = DogPet("Fido")

    print("\nMethod calls:")
    dogpet.speak()   # comes from Dog, because Dog comes first in (Dog, Pet)
    dogpet.care()    # from Pet
    dogpet.status()  # own method
