# Task A: Extend the ShoppingCart Class

You have a working `ShoppingCart` class in `shoppingCart.ts` with `addItem()` and `removeItem()` already implemented.

**Your task:** Add the following three methods to the class.

**Running the tests:** Open a terminal in this folder and run:
```
npm install
npm test
```
All 9 tests should pass when you're done.

---

## 1. `findItem(name)`

Searches the cart for an item by name and returns its object (`{ name: ..., price: ..., quantity: ... }`). Returns `null` if the item is not in the cart.

**Example:**
```typescript
const cart = new ShoppingCart();
cart.addItem("Apple", 1.50, 3);
cart.findItem("Apple");   // Returns { name: 'Apple', price: 1.50, quantity: 3 }
cart.findItem("Milk");    // Returns null
```

## 2. `totalPrice()`

Returns the total price of all items in the cart (price × quantity for each item, summed).

**Example:**
```typescript
const cart = new ShoppingCart();
cart.addItem("Apple", 1.50, 3);   // 4.50
cart.addItem("Banana", 0.75, 2);  // 1.50
cart.totalPrice();  // Returns 6.0
```

## 3. `checkout()`

Returns a formatted receipt string. The exact format is:

```
Receipt:
- Apple x3: $4.50
- Banana x2: $1.50
Total: $6.00
```

Each line item shows `- {name} x{quantity}: ${lineTotal}` (with the line total formatted to 2 decimal places).
The final line shows `Total: ${total}` (formatted to 2 decimal places).
Items appear in the order they were added.

**Example:**
```typescript
const cart = new ShoppingCart();
cart.addItem("Apple", 1.50, 3);
cart.addItem("Banana", 0.75, 2);
console.log(cart.checkout());
```

Output:
```
Receipt:
- Apple x3: $4.50
- Banana x2: $1.50
Total: $6.00
```
