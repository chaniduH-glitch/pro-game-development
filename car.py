class Car():
    
    brand = "tesla"
    speed = 35

    

    def __init__(self):
        print("making a new object")
    def accelerate(self):
            
        self.speed +=10 
        print(self.speed)
object1 = Car()
object2 = Car()

object1.accelerate()
object1.accelerate()
object2.accelerate()








  
