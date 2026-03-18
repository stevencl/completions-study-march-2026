# Task A: Extend the ShoppingCart Class

You have a working `ShoppingCart` class in `shopping_cart.py` with `add_item()` and `remove_item()` already implemented.

**Your task:** Add the following three methods to the class.

**Running the tests:** Open a terminal in this folder and run:
```
python -m pytest test_shopping_cart.py -v
```
All 9 tests should pass when you're done.

---

## 1. `find_item(name)`

Searches the cart for an item by name and returns its dict (`{'name': ..., 'price': ..., 'quantity': ...}`). Returns `None` if the item is not in the cart.

**Example:**
```python
cart = ShoppingCart()
cart.add_item("Apple", 1.50, 3)
cart.find_item("Apple")   # Returns {'name': 'Apple', 'price': 1.50, 'quantity': 3}
cart.find_item("Milk")    # Returns None
```

## 2. `total_price()`

Returns the total price of all items in the cart (price × quantity for each item, summed).

**Example:**
```python
cart = ShoppingCart()
cart.add_item("Apple", 1.50, 3)   # 4.50
cart.add_item("Banana", 0.75, 2)  # 1.50
cart.total_price()  # Returns 6.00
```

## 3. `checkout()`

Returns a formatted receipt string. The exact format is:

```
Receipt:
- Apple x3: $4.50
- Banana x2: $1.50
Total: $6.00
```

Each line item shows `- {name} x{quantity}: ${line_total:.2f}`
The final line shows `Total: ${total:.2f}`
Items appear in the order they were added.

**Example:**
```python
cart = ShoppingCart()
cart.add_item("Apple", 1.50, 3)
cart.add_item("Banana", 0.75, 2)
print(cart.checkout())
```

Output:
```
Receipt:
- Apple x3: $4.50
- Banana x2: $1.50
Total: $6.00
```
