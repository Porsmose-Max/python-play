import os
os.system('clear')

class Dog:
	# A simple class representing a dog

	def __init__(self, name, age): # The __init__ method is the constructor for the class. It is called when an instance of the class is created.
		self.name = name  # Instance variable for the dog's name
		self.age = age    # Instance variable for the dog's age

	def bark(self):
		return "Woof!"

	def get_human_years(self):
		return self.age * 7

	def __str__(self):              # når du printer objektet
		return f"Hund: {self.name}"

	def __len__(self):              # når du kalder len() på objektet
		return len(self.name)

# Create an instance of the Dog class (instantiating the class)
my_dog = Dog("Fido", 3) 
# fido er en instans af Dog — og et objekt

# Access the dog's name and age
print("My dog's name is %s and it is %d years old." % (my_dog.name, my_dog.age))
# Make the dog bark
print(my_dog.bark())
# Get the dog's age in human years
print("My dog is %d years old in human years." % my_dog.get_human_years())

print(my_dog)        # → "Hund: Fido"  (bruger __str__)
print(len(my_dog))   # → 4             (længden af "Fido")

# define the Vehicle class
class Vehicle:
    name = ""
    kind = "car"
    color = ""
    value = 100.00
    def description(self):
        desc_str = "%s is a %s %s worth $%.2f." % (self.name, self.color, self.kind, self.value)
        return desc_str

car1 = Vehicle()
car2 = Vehicle()

car1.color = "Red"
car1.kind = "Convertible"
car1.value = 60.000
car1.name = "Fer"

car2.color = "Bed"
car2.kind = "Van"
car2.value = 10.000
car2.name = "Jump"

# test code
print(car1.description())
print(car2.description())
