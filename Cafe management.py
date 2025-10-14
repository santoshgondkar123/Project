#  define the menu of resturant

menu = {
    "pizza" :40,
    "pasta" :50 ,
    "burger" : 60,
    "salad" : 70 ,
    "coffee" :80 ,
}
print(menu)

# greet
print("welcome to python resturant")
print("pizza: Rs40\npasta: Rs50\nburger: Rs60\nsalad: Rs70\ncoffee: Rs80")

order_total =0

item_1 = input("enter the name of items you want to order = ")
if item_1 in menu:
    order_total += menu[item_1]
    print(f"your item {item_1} has been added to your order")
else:
    print(f"ordered item {item_1} is not available yet")
    
another_order =input("Do you want to add another item? (Yes/NO)")
if another_order == "Yes" :
    item_2 = input("enter the name of second items =")
    if item_2 in menu:
        order_total += menu[item_2]
        print(f"Item {item_2} has been added to order")
    else:
        print(f"ordered item {item_2} is not avaialable")
print(f"the total amount of items to pay {order_total}")