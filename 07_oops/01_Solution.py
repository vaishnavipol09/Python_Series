#Solution_1

#class Car:
#    def __init__(self, brand, model):
 #       self.brand = brand
  #      self.model = model
#my_car = Car("Creta" , "BMW")
#print (my_car.brand)
#print(my_car.model)

#my_new_car = Car("Swift" , "Ertica")

#print(my_new_car.brand)



#Solution_2

#class Car:
    #def __init__(self, brand, model):
     #   self.brand = brand
      #  self.model = model

       # def full_name(self):
        #    return f"{self.brand} {self.model}"
        
        
#my_car = Car("Creta" , "BMW")
#print (my_car.brand)
#print(my_car.model)
#print(my_car.full_name())

#my_new_car = Car("Swift" , "Ertica")

#print(my_new_car.brand)



#Solution_3

#class Car:
 #   def __init__(self, brand, model):
  #      self.brand = brand
   #     self.model = model

        #def full_name(self):
         #   return f"{self.brand} {self.model}"
        
#class ElctricCar(Car):
 #   def __init__(self, brand, model, battery_capacity):  
  #      super().__init__(brand, model)  # Call the parent class constructor
   #     self.battery_capacity = battery_capacity  


#my_tesla = ElctricCar("tesla" , "Model S" , "85kWH")

#print(my_tesla.brand)
        
        
#my_car = Car("Creta" , "BMW")
#print (my_car.brand)
#print(my_car.model)
#print(my_car.full_name())

#my_new_car = Car("Swift" , "Ertica")

#print(my_new_car.brand)



#Solution_4

#class Car:
 #   def __init__(self, brand, model):
  #      self.brand = brand
   #     self.model = model

    #def get_brand(self):
     #   return self.brand + " !"   

        #def full_name(self):
           # return f"{self.brand} {self.model}"
        
#class ElctricCar(Car):
 #   def __init__(self, brand, model, battery_capacity):  
  #      super().__init__(brand, model)  # Call the parent class constructor
   #     self.battery_capacity = battery_capacity  


#my_tesla = ElctricCar("tesla" , "Model S" , "85kWH")

#print(my_tesla.brand)
#print(my_tesla.get_brand())
        
        
#my_car = Car("Creta" , "BMW")
#print (my_car.brand)
#print(my_car.model)
#print(my_car.full_name())

#my_new_car = Car("Swift" , "Ertica")

#print(my_new_car.brand)




#Solution_5

class Car:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model

    def get_brand(self):
        return self.brand + " !"   

        #def full_name(self):
         #   return f"{self.brand} {self.model}"

    def fuel_type(self):
        return "Petrol or Disel"     
        
class ElctricCar(Car):
    def __init__(self, brand, model, battery_capacity):  
        super().__init__(brand, model)  # Call the parent class constructor
        self.battery_capacity = battery_capacity  

    def fuel_type(self):
        return "Elctric charge"

my_tesla = ElctricCar("tesla" , "Model S" , "85kWH")

#print(my_tesla.brand)
#print(my_tesla.get_brand())
print(my_tesla.fuel_type())

Hydai = Car("Creta" , "Hydai")

print(Hydai.fuel_type())
        
        
#my_car = Car("Creta" , "BMW")
#print (my_car.brand)
#print(my_car.model)
#print(my_car.full_name())

#my_new_car = Car("Swift" , "Ertica")

#print(my_new_car.brand)



