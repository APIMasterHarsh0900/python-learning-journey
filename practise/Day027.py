class Bike:
    def __init__(self,brand,name,Cc,price):
        self.brand=brand
        self.name=name
        self.Cc=Cc
        self.price=price
    # I will now create a method to display the details of my future bike##
    def detailsofmybike(self):
        print(f"Brand: {self.brand}")
        print(f"Name: {self.name}")
        print(f"Cc: {self.Cc}")
        print(f"Price: {self.price}")
### Craeting an object of my bike class and displaying the details of my future bike##
mybike=Bike("Royal Enfield","Gurella","450cc","3.23 Lakh")
mybike.detailsofmybike()
print(
    f"Brand: {mybike.brand}",
    f"Name: {mybike.name}",
    f"Cc: {mybike.Cc}",
    f"Price: {mybike.price}",
    "I will buy it in March 2027"
)