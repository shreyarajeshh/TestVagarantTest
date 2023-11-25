class Product:
    def __init__(self, name, ind_price, gst, quantity):
        self.name = name
        self.ind_price = ind_price
        self.gst = gst
        self.quantity = quantity

    def total_price(self):
        return (self.ind_price + (self.ind_price * self.gst / 100)) * self.quantity
    #5% discount on leatherwallet and umbrella only
    


leatherwallet = Product("Leather Wallet", 1100, 18, 1)
umbrella = Product("Umbrella", 900, 12, 4)
cigarette = Product("Cigarette", 200, 28, 3)
honey = Product("Honey", 100, 0, 2)

purchase = [leatherwallet, umbrella, cigarette, honey]
max_gst = max(purchase, key=lambda x: (x.ind_price * x.gst / 100) * x.quantity)
print(f"Item with maximum GST amount is: {max_gst.name}")
total_bill_amount = sum(product.total_price() for product in purchase)
print(f"Total bill amount to be paid is: Rs. {total_bill_amount}")




            