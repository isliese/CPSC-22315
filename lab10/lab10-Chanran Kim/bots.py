import json
import threading
import time
import ast  # 추가: 안전한 문자열 변환을 위해 사용

# Load inventory from the file
def load_inventory(file_path):
    with open(file_path, 'r') as file:
        inventory = json.load(file)  # Parsing in JSON format
    return inventory


# Bot fetcher function
def bot_fetcher(item_list, cart_list, thread_lock, inventory_data):
    for item in item_list:
        if item in inventory_data:
            time.sleep(inventory_data[item][1])  # Simulate fetching time
            with thread_lock:  # Ensure only one thread accesses the cart at a time
                cart_list.append([item, inventory_data[item][0]])
                print(f"Robot fetched: {item} - {inventory_data[item][0]}")


# Bot clerk function
def bot_clerk(item_list):
    # Load inventory data
    file_path = './inventory.dat'
    inventory_data = load_inventory(file_path)

    # Initialize shared cart and thread lock
    cart_list = []
    thread_lock = threading.Lock()

    # Split items into 3 separate fetcher lists for robots
    robot_fetcher_lists = [[], [], []]
    for idx, item in enumerate(item_list):
        robot_fetcher_lists[idx % 3].append(item)

    # Launch threads for each robot
    threads = []
    for robot_list in robot_fetcher_lists:
        if robot_list:  # Only create a thread if there are items for the robot
            t = threading.Thread(target=bot_fetcher, args=(robot_list, cart_list, thread_lock, inventory_data))
            threads.append(t)
            t.start()

    # Wait for all threads to finish
    for t in threads:
        t.join()

    return cart_list


# Main function to test the bots
if __name__ == "__main__":
    user_input = input("Please enter item list (e.g., ['101', '102', '103']): ")
    try:
        # Safely convert the input string to a Python list
        my_item_list = ast.literal_eval(user_input)  
        if not isinstance(my_item_list, list):
            raise ValueError("Input is not a valid list!")

        # Process the items through bot_clerk
        result = bot_clerk(my_item_list)
        print("Final Cart List:", result)
    except FileNotFoundError as e:
        print(e)
    except (SyntaxError, ValueError):
        print("Invalid input! Please enter a valid list of item numbers.")
