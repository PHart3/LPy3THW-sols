class Person(object):
    def __init__(self, name):
        self.name = name
        self.pet = None
    def function(self):
        self.new =  self.name.join(("Perry ", " James ", " Linda "))
        print(self.new)

class Employee(Person):
    def __init__(self, name, salary):
        super(Employee, self).__init__(name)
        self.salary = salary
        
    def coolfunction(self):
        self.new =  self.name.join(("Perry ", " James ", " Linda "))
        print(self.new)
    def new_funct(self, dict):
        print(self.salary * 3)
        self.list = dict
        self.list1 =  list(self.list.keys())
        self.list2 =  list(self.list.items())
        for each in self.list1:
            print(each)
        for each in self.list2:
            print(each)


dic = {1: "One", 2: "Two", 3: "Three"}
first = Person("Hart")
second = Employee("Hart", 90)

first.function()
second.coolfunction()
second.new_funct(dic)

satan = first.pet
print(second.list)
