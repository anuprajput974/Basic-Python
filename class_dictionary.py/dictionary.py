shopping_cart = [] 

def add_item():
    item_name = input("Enter the item name: ") 
    item_price = float(input("Enter the item price: "))
    shopping_cart.append((item_name, item_price))

def remove_item():
    item_to_remove = input("Enter the item name to remove: ")f
    shopping_cart.remove((item_to_remove))

def calculate_total_cost():
    total_cost = 0 
    for item_name, item_price in shopping_cart:
        total_cost += item_price
        print("Total cost:", total_cost)

def display_items():
    for item_name, item_price in shopping_cart:
       print(item_name,item_price); 

choice = input("Enter your choice: ")

if choice == "1":
      add_item()
elif choice == "2":
    remove_item()
elif choice == "3":
    calculate_total_cost()
elif choice == "4":
    display_items()

else:
    print("Invalid choice. Please try again.")