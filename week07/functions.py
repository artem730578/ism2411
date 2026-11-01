# --- Self-Assessment ---
# 1- The first bug I spotted was the missing colon on line 10. VS Code showed it
# in the Problems tab before I even ran the file, and when I ran it the traceback
# said "SyntaxError: expected ':'with an arrow pointing right at it. The second
# bug I found with a debug print that showed i = 5 right before the IndexError.
# The third one had no error at all, I only noticed it because $90 was clearly not
# the sum of the sales. My instinct is to trust the traceback first, but the logic
# bug showed me that I also need to check if the answer actually makes sense.
#
# 2- apply_discount takes two inputs: a price (a number) and a tier (a word like
# "gold", "silver" or "bronze"). It returns the price after the discount: 15% off
# for gold, 10% for silver, 5% for bronze, and no discount for anything else. A
# colleague could use it without reading the code, just by knowing the name, the
# two inputs, and that it gives back the new price.
#
# AI use: I used Claude to assist me with this lab. It explained some of the module
# concepts. For Exercise 5 I used It after I couldn't figure out the rest of the bugs,
# and to explain the logic of the bug, so that in the future I can avoid it.


# --Exercise 1--

# Defining a function
def calculate_tax(price, rate):
    return price * rate

# Calling the function

tax = calculate_tax(100, 0.07)
tax2 = calculate_tax(250, 0.08)

print(f"Tax on $100 at 7%: ${tax:.2f}")
print(f"Tax on $250 at 8%: ${tax2:.2f}")


# --Exercise 2--

# Defined a function with multiple parameters
def apply_discount(price, tier):
    if tier == "gold":
        return price * 0.85  
    elif tier == "silver":
        return price * 0.90
    elif tier == "bronze":
        return price * 0.95
    else:
        return price


# Calling the function with different tiers
original_price = 200

for tier in ["gold", "silver", "bronze", "none"]:
        print(f"{tier + ':':7} ${apply_discount(original_price, tier):.2f}")

# --Exercise 3--

discounted = apply_discount(200, "gold")
print(f"After gold discount: ${discounted:.2f}")
with_tax = discounted + calculate_tax(discounted, 0.07)
print(f"After tax: ${with_tax:.2f}")

def final_price(price, tier, tax_rate):
    discounted_price = apply_discount(price, tier)
    tax = calculate_tax(discounted_price, tax_rate)
    return discounted_price + tax

print(f'final_price(200, "gold", 0.07) = ${final_price(200, "gold", 0.07):.2f}')


# --Exercise 4--
orders = [(200, "gold"), (150, "silver"), (80, "bronze"), (500, "none")]
for price, tier in orders:
    total = final_price(price, tier, 0.07)
    print(f"Price: ${price} | Tier: {tier} | Final: ${total:.2f}")

# --Exercise 5--
# Fixed version of broken_sales.py
sales = [120, 80, 250, 175, 90]

# Bug 3 (logic error): it said total = sale, so every loop replaced the total
# with the current sale instead of adding to it. Python gave no error, it just
# printed $90 (the last sale) instead of $715. Fixed by using += to add each sale.
total = 0
for sale in sales:
    total += sale
print(f"Total: ${total}")

# Bug 1 (SyntaxError): the for loop was missing a colon at the end of the line.
# Because of this Python would not run any line of the file, not even the ones
# above it. Fixed by adding the colon.
count = 0
for sale in sales:
    count += 1
print(f"Count: {count}")

# Bug 2 (IndexError): it said i <= len(sales). The list has 5 items with
# indexes 0 to 4, but <= let i reach 5, and sales[5] does not exist. I found
# it with a debug print that showed i = 5 right before the crash.
# Fixed by using < so the loop stops at 4.
i = 0
while i < len(sales):
    print(sales[i])
    i += 1

# --Exercise 6--

x = 100

def double_it():
    x = 999
    return x * 2
print(x)
print(double_it())
print(x)

# Prediction: 100, 1998, 100. The output matched.
# The x = 999 inside double_it() is a local variable. It only exists while the
# function runs, and it is a different x from the global x = 100 outside. So the
# function returns 999 * 2 = 1998, but the global x never changes and is still
# 100 after the function call.