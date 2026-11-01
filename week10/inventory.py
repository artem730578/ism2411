# -- Reflection --

# 1- I was surprised that list indexes start at 0, so the first item is inventory[0], and that 
# negative indexes like [-1] give the last item. I also did not expect .sort() to change
# the original list and return None.

# 2- My family works in Supply Chain, and inventory changes every day. With a list I can add
# new shipments with .append(), remove sold out items with .remove(), and filter or average
# sales in a few lines, instead of editing and re-sorting a spreadsheet by hand each time.


# --Exercise 1--

print ("--- Exercise 1: Build a List ---")

inventory = ["pen", "notebook", "stapler", "tape", "marker"]
print(inventory)
print(len(inventory))

# --- Exercise 2 ---
print(inventory[0]) #always grabs the first item
print(inventory[-1]) #always grabs the last item

middle = len(inventory) // 2
print(inventory[middle]) #grabs the middle item (not hard coded)

# --- Exercise 3 ---
print(inventory[:3]) #grabs the first 3 items
print(inventory[-2:]) #grabs the last 2 items
print(inventory[::2]) #grabs every other item

# --- Exercise 4 ---

print("--- Exercise 4: Modify a List ---")

inventory.append("envelope")
print(inventory)

inventory.remove("tape")
print(inventory)

inventory.sort()
print(inventory)

# --- Exercise 5: Tuple Comparison ---

print("--- Exercise 5: Tuple Comparison ---")
coords = (40.7128, -74.0060) #New York City coordinates

try:
    coords[0] = 99
except TypeError as e:
    print("Error:", e)

print("Tuples are good for coordinates because a location should not change by accident.")
print(coords)

# --- Exercise 6 ---
print("--- Exercise 6: List Average Sales ---")

sales = [100, 250, 75, 480, 200]
total = sum(sales)
count = len(sales)
average = total / count

print(f"Total: {total}")
print(f"Count: {count}")
print(f"Average: {average}")
print(f"Best day: {max(sales)}")
print(f"Worst day: {min(sales)}")


# --- Exercise 7 ---

print("--- Exercise 7: Accumulator ---")

prices = [9.99, 14.99, 4.99, 24.99, 1.99]

discounted = [] #an empty list 
for p in prices:
    discounted.append(round(p * 0.9, 2)) #apply a 10% discount and round to 2 decimal places
print(prices)
print(discounted)


# --- Exercise 8 ---

print("--- Exercise 8: Filter Sales ---")

sales = [340, 127, 589, 204, 467, 88, 731, 315, 62, 490]
high_sales = []
for s in sales:
    if s > 300:
        high_sales.append(s)

print(high_sales)
print(f"Count: {len(high_sales)}")
print(f"Average: {sum(high_sales) / len(high_sales):.2f}")