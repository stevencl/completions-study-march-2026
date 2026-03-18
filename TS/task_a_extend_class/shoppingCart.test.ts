import { ShoppingCart } from "./shoppingCart";

describe("findItem", () => {
  test("find existing item", () => {
    const cart = new ShoppingCart();
    cart.addItem("Apple", 1.5, 3);
    expect(cart.findItem("Apple")).toEqual({
      name: "Apple",
      price: 1.5,
      quantity: 3,
    });
  });

  test("find missing item", () => {
    const cart = new ShoppingCart();
    cart.addItem("Apple", 1.5, 3);
    expect(cart.findItem("Milk")).toBeNull();
  });

  test("find in empty cart", () => {
    const cart = new ShoppingCart();
    expect(cart.findItem("Apple")).toBeNull();
  });
});

describe("totalPrice", () => {
  test("empty cart", () => {
    const cart = new ShoppingCart();
    expect(cart.totalPrice()).toBe(0);
  });

  test("single item", () => {
    const cart = new ShoppingCart();
    cart.addItem("Apple", 1.5, 3);
    expect(cart.totalPrice()).toBe(4.5);
  });

  test("multiple items", () => {
    const cart = new ShoppingCart();
    cart.addItem("Apple", 1.5, 3);
    cart.addItem("Banana", 0.75, 2);
    expect(cart.totalPrice()).toBe(6.0);
  });
});

describe("checkout", () => {
  test("single item receipt", () => {
    const cart = new ShoppingCart();
    cart.addItem("Apple", 1.5, 3);
    const expected = "Receipt:\n- Apple x3: $4.50\nTotal: $4.50";
    expect(cart.checkout()).toBe(expected);
  });

  test("multiple items receipt", () => {
    const cart = new ShoppingCart();
    cart.addItem("Apple", 1.5, 3);
    cart.addItem("Banana", 0.75, 2);
    const expected =
      "Receipt:\n- Apple x3: $4.50\n- Banana x2: $1.50\nTotal: $6.00";
    expect(cart.checkout()).toBe(expected);
  });

  test("empty cart receipt", () => {
    const cart = new ShoppingCart();
    const expected = "Receipt:\nTotal: $0.00";
    expect(cart.checkout()).toBe(expected);
  });
});
