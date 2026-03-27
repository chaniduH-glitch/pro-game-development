#class is a blueprint

#object is instance of class
#creating a class

class Student():
    # properties/attributes of class
    name = ""
    age = 13
    studies = ""
    class_teacher = "john"
    #constructor - it gets called when an object is created 
    def __init__(self):
        print("making a new object")
    def change_details(self):
        self.age = int(input("what age do you want to put?"))
        self.name = input("what name do you want to put?") 
        self.studies = input("choose a study")
    def show_details(self):
        print(self.age)
        print(self.name)
        print(self.studies)
        print(self.class_teacher)

#creating an object of the class
object1 = Student()
object2 = Student()

object1.change_details()
object1.show_details()
object2.show_details()




        


