# Assignment 3: INVENTORY
# Create an inventory tracking system that has all of the following features:
# - Each item will have a name, quantity, and description as a dictionary.
# - All dictionaries will be saved in a master inventory list.
# - A function that ADDS something to that list (creates the dictionary and adds to the list).
# - A function that DISPLAYS the inventory in a readable format (i.e. do not just print out the list or dictionary, separate them out).
# - A function that will CHANGE THE QUANTITY of an item (this is difficult to do and many ways to do it).
# - A function that REMOVES an item from the list. Research required :)
# Questions for this assignment:
# - What was the most challenging part about this.

master_inventory = [
    {'name': 'ONE', 'qty': 1, 'desc': 'first item'},
    {'name': 'TWO', 'qty': 2, 'desc': 'second item'},
    {'name': 'THREE', 'qty': 3, 'desc': 'third one'},
]


def add_item():
    print('---\nAdd items...')
    name = input('Item name >> ')
    qty = input('Quantity >> ')
    desc = input('Description >> ')
    try:
        new_item = {
            'name': name,
            'qty': qty,
            'desc': desc
        }

        master_inventory.append(new_item)
        print(f"{name} added.")
    except:
        print("Something went wrong")


def del_item():
    print("---\nRemove item...")
    remove_item = int(input("Index of the item to remove >> "))
    # if remove_item != "":
    try:
        master_inventory.pop(remove_item)
        print(f"{remove_item} removed.")
    except:
        print("Something went wrong")


def change_qty():
    print("---\nChange quantity...")
    this_item = int(input("Index of item >> "))
    new_qty = int(input("New quantity >> "))
    try:
        master_inventory[this_item]['qty'] = int(new_qty)
        print(
            f"Upated quantity to {new_qty} for {master_inventory[this_item]['name']}")
    except:
        print("Something went wrong")


def print_items():
    print("---\nItems in list")
    for inv_item in master_inventory:
        print(
            f"{master_inventory.index(inv_item)} > Name: {inv_item['name']} | Quantity: {inv_item['qty']} | Description: {inv_item['desc']}")


choice = "p"

while choice != "q":
    match choice:
        case "a":
            add_new = ""
            while add_new != "n":
                add_item()
                add_new = str(input("Add another item? Y/n >> "))
        case "r":
            del_item()
        case "p":
            print_items()
        case "c":
            change_qty()
        case _:
            choice = input(
                "\nChoose: (a)dd, (c)hange quantity, (r)emove, (p)rint, (q)uit >> ")

    choice = input(
        "\nChoose: (a)dd, (c)hange quantity, (r)emove, (p)rint, (q)uit >> ")

print("DONE")
