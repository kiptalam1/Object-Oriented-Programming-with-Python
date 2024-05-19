import csv

class Item:
    pay_rate = 0.8 # pay rate after 20% discount
    all = []
    
    def __init__(self, name: str, price: float, quantity = 0):
        # Run validations to assigned arguments
        assert price >= 0, f"Price {price} is not greater than or equal to zero!"
        assert quantity >= 0, f"Quantity {quantity} is not greater than or equal to zero!"

        # assign object to self
        self.name = name
        self.price = price
        self.quantity = quantity
        
        # actions to execute
        Item.all.append(self)

    
    def calculate_total_price(self):
        return self.price * self.quantity
        

    def apply_discount(self):
        self.price = self.price * self.pay_rate

    
    @classmethod
    def instantiate_from_csv(cls):
        with open('Items.csv', 'r') as f:
            reader = csv.DictReader(f)
            items = list(reader)
            
        for item in items:
            Item(
                name= item.get('Name'), 
                price= float(item.get('Price')),
                quantity= float(item.get('Quantity'))
            )

    
    @staticmethod
    def is_integer(num):
        if isinstance(num, float):
            # count out the floats that are point zero
            return num.is_integer()
        elif isinstance(num, int):
            return True
        else:
            return False
        

        
    def __repr__(self):
        return f"{self.__class__.__name__}('{self.name}', {self.price}, {self.quantity})"


class Phone(Item):
   
    def __init__(self, name: str, price: float, quantity= 0, broken_phones= 0 ):
        # call super() function for access to all attributes / methods
        super().__init__(name, price, quantity)
        # Run validations to assigned arguments
        assert broken_phones >= 0, f"Broken Phones {broken_phones} is not greater than or equal to zero!"

        # assign object to self
        self.broken_phones = broken_phones
        
        

phone1 = Phone("jscPhonev10", 500, 5, 1)
print(Item.all)
