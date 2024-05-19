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


    def __repr__(self):
        return f"Item('{self.name}', {self.price}, {self.quantity})"
        

item1 = Item('phone', 100, 5)
item2 = Item('laptop', 1000, 3)
item3 = Item('cable', 18, 5)
item4 = Item('mouse', 58, 5)
item5 = Item('keyboard', 75, 5)

#for instance in Item.all:
#    print(instance.name, ':', instance.price)

print(Item.all)
