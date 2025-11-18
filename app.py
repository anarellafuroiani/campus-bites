import heapq
from datetime import datetime, timedelta

# To test the algorithm, simulate saved data and avoid an empty algorithm:
def default_fridge():
    fridge={"eggs": [1, "2025-12-06", "Alejandro"], "pasta": [2, "2025-10-10", "Isabella"],"chocolate": [1, "2025-09-07", "Natalia"]} # hash table
    return fridge

# Display what's in the fridge:
def view_fridge(fridge):
    print("\nShared Fridge Items:")
    if not fridge:
        print("(The fridge is empty)")
        return
    for item, data in fridge.items():
        print(f"- {item.title()} (x{data[0]}) – expires {data[1]} – added by {data[2]}")


# Add a new item to the fridge:
def add_item(fridge):
    item = input("\nEnter item name: ").lower()
    qty = int(input("Enter quantity: "))
    exp = input("Enter expiration date (YEAR-MONTH-DAY): ")
    owner = input("Who is adding this? ")
    fridge[item] = [qty, exp, owner]
    print(f"{item.title()} added")

# Delwte an item if it was consumed:
def remove_item(fridge):
    item = input("\nEnter the item you want to remove: ").lower()
    if item in fridge:
        del fridge[item]
        print(f"{item.title()} removed")
    else:
        print("Food not found")

# Notify if item is expiring in less than 3 days
def expiring_items(fridge):
    heap = []
    today = datetime.today()
    for item, (qty, exp, owner) in fridge.items():
        days_left = (datetime.strptime(exp, "%Y-%m-%d") - today).days
        heapq.heappush(heap, (days_left, item))   # heap
    print("\nItems expiring soon:")
    while heap:
        days, item = heapq.heappop(heap)
        if days <= 3:
            print(f"- {item.title()} expires in {days} days")
    print()

# Store shared meals (meal name, info) (info=ingredients, available_until, owner)
def default_meals():
    return {
        "pasta bolognese": [
            ["pasta", "tomato sauce", "beef"],
            "2025-06-10",
            "Alejandro"
        ],
        "chicken salad": [
            ["chicken", "lettuce", "tomato"],
            "2025-06-08",
            "Isabella"
        ],
        "brownies": [
            ["chocolate", "flour", "butter"],
            "2025-06-07",
            "Natalia"
        ]
    }

# keeps track of ingredients requests (requested ingredient, pending/fulfilled)
def default_requests():
    return {
        "sugar": ["Anarella", "pending"],
        "rice": ["Valeria", "fulfilled"],
        "salt": ["Federico", "pending"]
    }

# Share leftovers:
def share_leftover(meals):
    print("\nShare a leftover meal")

    name = input("Meal name: ").lower()
    ingredients = input("Main ingredients (separated with comma please): ").lower()
    until = input("Available until (YYYY-MM-DD): ")
    owner = input("Who is sharing this? ")
    meals[name] = [ingredients.split(','), until, owner] # hash table

    print(f"{name.title()} shared successfully")
    print(f"Ingredients: {ingredients}")
    print(f"Available until {until}")

# View the "Meal's Feed":
def view_meals(meals):
    print("\nShared Meals:")
    if not meals:
        print("(No meals shared yet)")
        return
    for name, (ingredients, until, owner) in meals.items():
        print(f"- {name.title()} by {owner} : {', '.join(i.strip() for i in ingredients)} (until {until})")

# Request ingredients:
def request_ingredient(requests):
    print("\nRequest an ingredient")
    ingredient = input("Ingredient you need: ").lower()
    requester = input("Your name: ")
    requests[ingredient] = [requester, "pending"] # hash yable
    print(f"Request for {ingredient} sent by {requester}")

# View requests in feed
def view_requests(requests):
    print("\nCurrent Ingredient Requests:")
    if not requests:
        print("(No active requests)")
        return
    for ing, (req, status) in requests.items():
        print(f"- {ing.title()} requested by {req} → Status: {status}")

# Accepting requests
def fulfill_request(requests):
    ingredient = input("\nWhich ingredient are you accepting?").lower()
    if ingredient in requests:
        requests[ingredient][1] = "fulfilled"
        print(f"Request for {ingredient} marked as fulfilled!")
    else:
        print("Request not found.")

# Screen menu:
def welcome():
    print("\nWelcome to Campus Bites!")
    print("\nChoose an option:")
    print("1. View your fridge items")
    print("2. Add a new item to your fridge")
    print("3. Remove an item from your fridge")
    print("4. Share a leftover meal to your friends")
    print("5. View shared meals from your friends")
    print("6. Request an ingredient")
    print("7. View ingredient requests from your friends")
    print("8. Fulfill a request to your friends")
    print("9. See your expiring items")
    print("10. Quit")

# Options:
def option_selection():
    fridge = default_fridge()
    meals = default_meals()
    requests = default_requests()

    while True:
        welcome()
        choice = input("Your choice: ").strip()
        if choice == "1":
            view_fridge(fridge)
        elif choice == "2":
            add_item(fridge)
        elif choice == "3":
            remove_item(fridge)
        elif choice == "4":
            share_leftover(meals)
        elif choice == "5":
            view_meals(meals)
        elif choice == "6":
            request_ingredient(requests)
        elif choice == "7":
            view_requests(requests)
        elif choice == "8":
            fulfill_request(requests)
        elif choice == "9":
            expiring_items(fridge)
        elif choice == "10":
            print("Bye")
            break
        else:
            print("Invalid")


# Run program
def main():
    option_selection()

main()









