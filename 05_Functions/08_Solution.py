def print_kwargs(**kwargs):
    for key, value in kwargs.items():
        print(f"{key}: {value}")
print_kwargs(name = "Vaishnavi")        
print_kwargs(name = "Vaishnavi" , age = 25)        
print_kwargs(name = "Vaishnavi" , age = 25 , role = "Sofware Engineer")        