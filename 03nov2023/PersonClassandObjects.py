# Create a Class Person , Two Objects by taking (name, age, address) Input from users and print details in the end.

class Person:
    name=None
    age=None
    address=None

    def person_details(self):
        print (f"My name is {self.name} \n My age is {self.age} \n My address is {self.address}")


obj1_person=Person()
obj1_person.name =input("enter the name of first person\n")
obj1_person.age = input("enter the age of first person\n")
obj1_person.address = input("enter the address of first person \n")

obj2_person=Person()
obj2_person.name =input("enter the name of second person\n")
obj2_person.age= input("enter the age of second person\n")
obj2_person.address = input("enter the address of second person \n")

obj1_person.person_details()
obj2_person.person_details()