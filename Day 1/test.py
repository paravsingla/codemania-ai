# initialize an empty list

l = []

# add elements to list

l.append(1)

# initialize a dictionary

d = {}

# add elements to dictionary

d['a'] = 1


# create a class


class Person:

    def __init__(self, name):
        self.name = name

    def say_hello(self):
        print("Hello", self.name)


# instantiate the class
ob = Person("Parav")

# call a method of an object
ob.say_hello()
