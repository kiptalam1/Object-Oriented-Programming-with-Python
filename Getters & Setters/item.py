class Item:
    pay_rate = 0.8 # pay rate after 20% discount
    all = []
    
    def __init__(self, name: str, price: float, quantity = 0):
        # Run validations to assigned arguments
        assert price >= 0, f"Price {price} is not greater than or equal to zero!"
        assert quantity >= 0, f"Quantity {quantity} is not greater than or equal to zero!"

        # assign object to self
        self.__name = name
        self.price = price
        self.quantity = quantity
        
        # actions to execute
        Item.all.append(self)


    @property
    # Property Decorator = Read-Only Attribute
    def name(self):
        return self.__name

    @name.setter
    def name(self, value):
        if len(value) > 10:
            raise Exception("The name is too long!")
        else:
            self.__name = value
        

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


   
