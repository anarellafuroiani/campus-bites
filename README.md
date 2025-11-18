# campus-bites
Campus Bites: shared fridge, meal sharing, and ingredient requests app (ADS Final Project)
Campus Bites is a platform designed to help university students reduce food waste, save money, and improve collaboration in shared living environments.
Our app allows students and young adults to keep track of their shared fridge items, share leftover meals, and request ingredients from friends.

**Installation:**
To run the program, make sure you have:
1. Python 3.8 or higher
2. You don't need external libraries, just built in models: heapq and datetime

**How to Run:**
1. Download or copy this repository
2. Open app.py
4. Run the entire program 

**USAGE**
After entering Campus Bites, the user will be welcomed and asked what they want to do.
The menu includes the following options:
1. View your fridge items
2. Add a new item
3. Remove an item
4. Share a leftover meal
5. View shared meals
6. Request an ingredient
7. View ingredient requests
8. Fulfill a request
9. See expiring items
10. Quit

Viewing your fridge:
- The system displays all currently saved items in your shared fridge with your roommates.
- **Input:** None
- **Output:** List of items

Adding a new fridge item:
- This allows the user to store a new item in the shared fridge.
- **Input:** Item name, quantity, expiration date, owner name
- **Output:** Confirmation message
- Data structure used: hash tables

Removing an item from the frige:
- Used when food has been consumed.
- **Input:** Name of the item consumed
- **Output:** Confirmation message or error if the food is not in the fridge
- Deletion from hash tables was used

Sharing a leftover meal:
- User can share leftover food (whole meals)
- **Input:** meal name, ingredients, availability date, owner
- **Output:** confirmation message

View shared meals:
- Display all meals shared by friends
- **Input:** None
- **Output:** meal’s name, owner, ingredients, and availability

Requesting an ingredient:
- Allows a student to request something they’re missing.
- **Input:** ingredient, name of who is requesting it
- **Output:** Confirmation message

Viewing ingredients requested:
- Shows the list of pending or fulfilled requests.
- **Input:** None
- **Ouput:** Ingredient, who r4equested it, status (pending or fulfilled)

Fulfilling a request:
- Mark a request from your friends as fulfilled
- **Input:** Ingredient to fulfill
- **Output:** Confirmation message

View expiring items:
- Shows items expiring in the next 3 days
- **How it works:** uses a minheap from heapq so that items closest to expiration appear first
- **Algorithm used:** heaps (push and pop)
- **Output:** list of items soon to expire

**DATA STRUCTURES USED:**

**1. Hash Tables:**
- Used for: fridge items, meals storage, ingredients requests
- **Why:** Allows O(1) (avg) insertion, deletion, and lookup.

**2. Heaps:**
- Used for: Sorting fridge items by expiration date, finding items expiring soon
- **Why:** Provides efficient priority based retrieval (for expiration).

**ALGORITHMS IMPLEMENTED:**
1. Insertion
2. Deletion
3. Searching

**CREDITS:**
Isabella Lizarraga
Natalia Gonzalez
Federico Osorio
Alejandro Gonzalez
Armando Hernandez
Anarella Furoiani
