import json

# load_inventory function that reads json file
def load_inventory(file_path):
    with open(file_path, 'r') as file:
        inventory = json.load(file)  # Parshing in JSON format
    return inventory


# bot_clerk function
def bot_clerk(item_list):
    cart_list = []
    thread_lock = []

    # Reading and storing the inventory
    file_path = 'inventory.dat'
    inventory_data = load_inventory(file_path)

    # If the item list is empty 
    if item_list == []:
        return []

    # Separate the items that have been passed to the clerk into 3 robot fetcher lists
    else:
        for item in item_list:
            if item in inventory_data:
                cart_list.append([item, inventory_data[item][0]])

        return cart_list


# bot_fetcher function
def bot_fetcher(item_list, cart_list):
    return 0



my_item_list = input("Please enter item list: ")
bot_clerk(my_item_list)