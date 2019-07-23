class Dog:
    def __init__(self,name,age):
        self.name = name
        self.age = age

    def bark(self):
        print(self.name + " can bark.")

dog = Dog('ZHA',12)
# dog.bark()
def info(self):
    print(self.name,self.age)

dog.inf = info
dog.inf(dog)
dog.inf()