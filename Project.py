
# List to store all the items

inventory = []

def add_item():
    print("\n--- Add New Item ---")
    name = input("Enter item name: ")
    price = float(input("Enter item price: "))
    quantity = int(input("Enter item quantity: "))
    category = input("Enter item category: ")

    item = {
        "name": name,
        "price": price,
        "quantity": quantity,
        "category": category
    }

    inventory.append(item)
    print(f"Item '{name}' added successfully!\n")

# If you need to update an item

def update_item():
    print("\n--- Update Item ---")
    name = input("Enter the item name to update: ")

    for item in inventory:
        if item["name"].lower() == name.lower():
            print("Item found. Enter new details:")

            item["price"] = float(input("New price: "))
            item["quantity"] = int(input("New quantity: "))
            item["category"] = input("New category: ")

            print(f"Item '{name}' updated successfully!\n")
            return
    print("Item not found.\n")

def view_inventory():
    print("\n--- Inventory List ---")
    if not inventory:
        print("Inventory is empty.\n")
        return

    for item in inventory:
        print(f"Name: {item['name']} | Price: {item['price']} | "
              f"Quantity: {item['quantity']} | Category: {item['category']}")
    print()

# If you need to remove an item

def remove_item():
    print("\n--- Remove Item ---")
    name = input("Enter the name of the item to remove: ")

    for item in inventory:
        if item["name"].lower() == name.lower():
            inventory.remove(item)
            print(f"Item '{name}' removed successfully!\n")
            return
    print("Item not found.\n")

# If you need to search by category

def search_by_category():
    print("\n--- Search by Category ---")
    category = input("Enter category: ").lower()

    found_items = [item for item in inventory if item["category"].lower() == category]

    if found_items:
        print(f"\nItems in category '{category}':")
        for item in found_items:
            print(f"Name: {item['name']} | Price: {item['price']} | "
                  f"Quantity: {item['quantity']}")
    else:
        print("No items found in this category.")
    print()

def main():
    while True:
        print("=== Inventory Management System ===")
        print("1. Add Item")
        print("2. Update Item")
        print("3. View Inventory")
        print("4. Remove Item")
        print("5. Search by Category")
        print("6. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            add_item()
        elif choice == "2":
            update_item()
        elif choice == "3":
            view_inventory()
        elif choice == "4":
            remove_item()
        elif choice == "5":
            search_by_category()
        elif choice == "6":
            print("Exiting program. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.\n")


# Run the program
main()