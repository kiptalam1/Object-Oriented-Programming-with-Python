from item import Item

class Phone(Item):
   
    def __init__(self, name: str, price: float, quantity= 0, broken_phones= 0 ):
        # call super() function for access to all attributes / methods
        super().__init__(name, price, quantity)
        # Run validations to assigned arguments
        assert broken_phones >= 0, f"Broken Phones {broken_phones} is not greater than or equal to zero!"

        # assign object to self
        self.broken_phones = broken_phones
