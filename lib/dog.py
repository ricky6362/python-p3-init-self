#!/usr/bin/env python3

class Dog:
    def __init__(self, name, breed = 'Mutt'):
        self.name = name
        self.breed = breed
        print(f"{self.name} is born!")

    def showing_self(self):
        return self
    
    def test_saves_self_breed(self):
        pass
        

    
fido = Dog('Fido')