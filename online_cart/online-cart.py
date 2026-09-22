cart = ["bread", "biscuits", "butter", "candies", "tissues"]

print("\n===== AMAZON CART =====")
print("1. Add Item")
print("2. Remove Item")
print("3. Search Item")
print("4. View Cart")

choice = input("Enter your choice: ")

if choice == "1":
    item = input("Enter item to add: ")
    cart.append(item)
    print("Item added successfully!")
    print("Updated Cart:", cart)

elif choice == "2":
    item = input("Enter item to remove: ")

    if item in cart:
        cart.remove(item)
        print("Item removed successfully!")
        print("Updated Cart:", cart)
    else:
        print("Item not found in cart.")

elif choice == "3":
    item = input("Enter item to search: ")

    if item in cart:
        print("Item found in cart.")
    else:
        print("Item not found in cart.")

elif choice == "4":
    print("\nYour Cart:")
    
    for item in cart:
        print("-", item)

else:
    print("Invalid choice.")
