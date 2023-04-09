class Pet:
    def __init__(self, pet_type, pet_name):
        self.pet_type = pet_type
        self.pet_name = pet_name
        print(f'The {self.pet_type} name is {self.pet_name}')

pet_type = input('What pet do you have? ')
pet_name = input('Ok, and what is its name? ')
x = Pet(pet_type, pet_name)