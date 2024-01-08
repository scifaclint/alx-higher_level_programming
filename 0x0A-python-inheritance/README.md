# python inheritance

// https://docs.python.org/3/tutorial/classes.html#inheritance
class Animal:
def **init**(self, name):
self.name = name
def speak(self):
print("I don't know what I say.")
class Dog(Animal): # Dogs inherit from Animals
