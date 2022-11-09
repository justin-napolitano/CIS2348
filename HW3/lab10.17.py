#Name: Becky Tseng
#StudentID: 2038591

class ItemToPurchase:
    def __init__(self,item_name="none",item_price=0,item_quantity=0):
        self.item_name=item_name
        self.item_price=item_price
        self.item_quantity=item_quantity
    def getTotalCost(self):
        return self.item_quantity*self.item_price
    def print_item_cost(self):
        print(f"{self.item_name} {self.item_quantity} @ ${self.item_price:g} = ${self.getTotalCost():G}")

if __name__ == "__main__":

    items=[]
    for i in range(1,3):
        print('Item',i)
        name=input('Enter the item name:\n')
        price=float(input('Enter the item price:\n'))
        quant=int(input('Enter the item quantity:\n'))
        item=ItemToPurchase(name,price,quant)
        items.append(item)
        print()
    print('TOTAL COST')
    total = 0
    for i in items:
        total += i.getTotalCost()
        i.print_item_cost()

    print(f"\nTotal: ${total:g}")
