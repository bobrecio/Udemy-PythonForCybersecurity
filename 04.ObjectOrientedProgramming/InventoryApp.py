# Take the inventory assignment and redo it as an object oriented programming project.
# Use a class for each inventory item and place those into a list.
# Import that into another python file and make sure your program functions the same
# as your previous assignment or better.
from item import Item

inventory_list = []
inventory_list.append(Item('ONE', 1, 'first item'))
inventory_list.append(Item('TWO', 2, 'second item'))
inventory_list.append(Item('THREE', 3, 'third one'))


def create_item():
    print('---\nAdd items...')
    try:
        name = input('Item name >> ')
        qty = int(input('Quantity >> '))
        desc = input('Description >> ')

        item = Item(name, qty, desc)
        inventory_list.append(item)
        print(f"Created - {name}")
    except:
        print("Something went wrong")


def remove_item():
    print("---\nRemove item...")
    try:
        item_index = int(input("Index of the item to remove >> "))
        item_obj = inventory_list[item_index]
        inventory_list.pop(item_index)
        print(f"{item_obj.name} - removed.")
    except:
        print("Something went wrong")


def update_qty():
    print("---\nChange quantity...")
    try:
        index = int(input("Index of item >> "))
        new_qty = int(input("New quantity >> "))

        item = inventory_list[index]
        item.qty = int(new_qty)
        print(
            f"Upated quantity to {item.qty} for {item.name}")
    except:
        print("Something went wrong")


def display_items():
    # print(inventory_list)
    print("---\nItems in list")
    for item in inventory_list:
        name = item.name
        qty = item.qty
        desc = item.desc
        index = inventory_list.index(item)
        print(
            f"{index} > Name: {name} | Quantity: {qty} | Description: {desc}")


choice = ""

while choice != "q":
    match choice:
        case "c":
            add_new = ""
            while add_new != "n":
                create_item()
                add_new = str(input("Add another item? Y/n >> "))
        case "r":
            remove_item()
        case "u":
            update_qty()
        case "d":
            display_items()

    choice = input(
        "\nChoose: (c)reate, (r)emove, (u)pdate, (d)isplay, (q)uit >> ")

print("DONE")
