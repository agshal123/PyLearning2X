#Create a Car class and Create 2 Objects of the class with attributes 5 and 5 methods

class Car:
    model =None
    color =None
    man_year=None
    Car_type=None
    fuel_type=None


    def Start(self,start_type):
        print(self.model + "\tis a\t" + start_type)

    def year_of_manufacturing(self):
        print(self.model +"\t has been manufactured in\t" + self.man_year)

obj1=Car()
obj1.model=input("Enter the 1st model of a car")
obj1.color=input("enter the color of the car")
obj1.man_year=input("enter the manufacturing year of the car")
obj1.Start("KeyStart")

obj2=Car()
obj2.model=input("Enter the 2nd model of a car")
obj2.color=input("enter the color of the car")
obj2.man_year=input("enter the manufacturing year of the car")
obj2.Start("KeyStart")
obj2.year_of_manufacturing()


