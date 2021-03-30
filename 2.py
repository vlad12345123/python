class Worker:
    '''doc class Worker'''
    count = 0

    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        Worker.count += 1

    def display(self):
        print("Worker:")
        print("{} {}".format(self.name, self.surname))


class Animal:
    count = 0

    def __init__(self, name, age):
        self.id = Animal.count
        self.name = name
        self.age = age
        Animal.count += 1

    def display(self):
        print("Animal {}\n Name:{}\n Age:{}".format(self.id, self.name, self.age))


w1 = Worker("Ivan", "Ivanov")
print("w1.count: ", w1.count)
w2 = Worker("Alexei", "Petrov")
print("w2.count: ", w2.count)
print("w1.count: ", w1.count)
print("Worker.count: {0} \n".format(Worker.count))
print("Worker.__name__: ", Worker.__name__)
print("Worker.__dict__: ", Worker.__dict__)
print("Worker.__doc__: ", Worker.__doc__)
print("Worker.__bases__: ", Worker.__bases__)

cat = Animal("Cat", 3)
dog = Animal("Dog", 5)
cow = Animal("Cow", 8)

cat.display()
dog.display()
cow.display()
cat.display()
