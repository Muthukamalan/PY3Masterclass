class Animal:
    def speak(self) -> None:
        print("Animal makes a sound")


class Dog(Animal):
    def speak(self) -> None:
        print("Dog woofs!")


class Cat(Animal):
    def speak(self) -> None:
        print("Cat meows!")