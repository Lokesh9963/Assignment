'***************Classes and Objects **************'



#Define a Class in Python
'For example, let’s say you want to track employees in an organization.'
'You need to store some basic information about each employee such as their name, age, position, and year they started working.'

kirk = ["James Kirk", 34, "Captain", 2265]
spock = ["Spock", 35, "Science Officer", 2254]
mccoy = ["Leonard McCoy", "Chief Medical Officer", 2266]


#How to Define a Class
'All class definitions start with the class keyword, which is followed by the name of the class and a colon.'
'Any code that is indented below the class definition is considered part of the class’s body.'
'Python class names are written in CapitalizedWords notation by convention.'

class Dog:
    pass


#Instance Attributes

class Dog:
    def __init__(self, name, age):   #__init__() sets the initial state of the object by assigning  values of object’s properties
        self.name = name  #self.name = name creates an attribute called name and assigns it to value of the name parameter.
        self.age = age    #self.age = age creates an attribute called age and assigns it to value of the age parameter.


#Class Attributes

class Dog:
    species = "Canis familiaris"   #class attributes are attributes that have the same value for all class instances
    buddy = Dog("Buddy", 9)
    miles = Dog("Miles", 4)

    def __init__(self, name, age):
        self.name = name
        self.age = age
    print(buddy.age)        #accessing their instance attributes using dot notation
    buddy.age=10            #changing the value of attribute dynamically
    print(buddy.age)




#Instance Methods

class Dog:
    miles = Dog("Miles", 4)
    species = "Canis familiaris"

    def __init__(self, name, age):
        self.name = name
        self.age = age

    # Instance method
    def description(self):
        return f"{self.name} is {self.age} years old"

    # Another instance method
    def speak(self, sound):
        return f"{self.name} says {sound}"


#Special Instance Methods
class Dog:
    miles = Dog("Miles", 4)
    species = "Canis familiaris"

    def __init__(self, name, age):
        self.name = name
        self.age = age
    # Replace .description() with __str__()
    def __str__(self):
         return f"{self.name} is {self.age} years old"



#Examples
class Car:
    def __init__(self, color, mileage):
        self.color = color
        self.mileage = mileage

car1 = Car (color="blue", mileage=20_000)
car2 = Car (color="red", mileage=30_000)
for car in (car2, car2):
    print(f"The {car.color} car has {car.mileage:,} miles")


#Inheritance in Classes
'Inheritance is the process by which one class takes on the attributes and methods of another.'
'Newly formed classes are called child classes, and classes that child classes are derived from are called parent classes.'


class Dog:
    species = "Canis familiaris"

    def __init__(self, name, age, breed):
        self.name = name
        self.age = age
        self.breed = breed
    def speak(self, sound):
        return f"{self.name} says {sound}"
miles = Dog("Miles", 4, "Jack Russell Terrier")
buddy = Dog("Buddy", 9, "Dachshund")
jack = Dog("Jack", 3, "Bulldog")
jim = Dog("Jim", 5, "Bulldog")
print(buddy.speak("Yap"))
print(jim.speak("Woof"))
print(jack.speak("Woof"))


#Parent Class VS Child Class

class Dog:
    species = "Canis familiaris"

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __str__(self):
        return f"{self.name} is {self.age} years old"

    def speak(self, sound):
        return f"{self.name} says {sound}"

#Creating Child classes of Parent Dog Class

class JackRussellTerrier(Dog):
    pass

class Dachshund(Dog):
    pass

class Bulldog(Dog):
    pass

#Instances of Child Classes

miles = JackRussellTerrier("Miles", 4)
buddy = Dachshund("Buddy", 9)
jack = Bulldog("Jack", 3)
jim = Bulldog("Jim", 5)

#Inheritance
print(miles.species)
print(buddy.name)
print(jack)
print(jim.speak("Woof"))

#To determine which class a given object belongs to, you can use the built-in type():
print(type(miles))

#to determine if miles is also an instance of the Dog class? You can do this with the built-in isinstance():
print(isinstance(miles, Dog))
print(isinstance(miles, Bulldog))


#Extend the Functionality of a Parent Class

class Dog:
    species = "Canis familiaris"

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __str__(self):
        return f"{self.name} is {self.age} years old"

    def speak(self, sound):
        return f"{self.name} says {sound}"
class JackRussellTerrier(Dog):
    def speak(self, sound="Arf"):
        return f"{self.name} says {sound}"
miles = JackRussellTerrier("Miles", 4)
print(miles.speak())
print(miles.speak("Grrr"))


#Changing the string returned by .speak
class Dog:
    species = "Canis familiaris"

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __str__(self):
        return f"{self.name} is {self.age} years old"

    def speak(self, sound):
        return f"{self.name} barks: {sound}"
class JackRussellTerrier(Dog):
    pass

class Dachshund(Dog):
    pass

class Bulldog(Dog):
    pass

jim = Bulldog("Jim", 5)
print(jim.speak("Woof"))


#You can access the parent class from inside a method of a child class by using super():
class Dog:
    species = "Canis familiaris"

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __str__(self):
        return f"{self.name} is {self.age} years old"

    def speak(self, sound):
        return f"{self.name} barks: {sound}"
class JackRussellTerrier(Dog):
    def speak(self, sound="Arf"):
        return super().speak(sound)
#When you call super().speak(sound) inside JackRussellTerrier,
#Python searches the parent class, Dog, for a .speak() method and calls it with the variable sound.

miles = JackRussellTerrier("Miles", 4)
print(miles.speak())



#Class Inheritance Exercise
class Dog:
    species = "Canis familiaris"

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __str__(self):
        return f"{self.name} is {self.age} years old"

    def speak(self, sound):
        return f"{self.name} says {sound}"
class GoldenRetriever(Dog):
    def speak(self, sound="Bark"):
        return super().speak(sound)

miles = JackRussellTerrier("Miles", 4)
print(miles.speak("gr"))
