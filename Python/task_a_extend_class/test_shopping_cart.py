import unittest
from shopping_cart import ShoppingCart


class TestFindItem(unittest.TestCase):
    def test_find_existing_item(self):
        cart = ShoppingCart()
        cart.add_item("Apple", 1.50, 3)
        result = cart.find_item("Apple")
        self.assertEqual(result, {'name': 'Apple', 'price': 1.50, 'quantity': 3})

    def test_find_missing_item(self):
        cart = ShoppingCart()
        cart.add_item("Apple", 1.50, 3)
        self.assertIsNone(cart.find_item("Milk"))

    def test_find_in_empty_cart(self):
        cart = ShoppingCart()
        self.assertIsNone(cart.find_item("Apple"))


class TestTotalPrice(unittest.TestCase):
    def test_empty_cart(self):
        cart = ShoppingCart()
        self.assertEqual(cart.total_price(), 0)

    def test_single_item(self):
        cart = ShoppingCart()
        cart.add_item("Apple", 1.50, 3)
        self.assertEqual(cart.total_price(), 4.50)

    def test_multiple_items(self):
        cart = ShoppingCart()
        cart.add_item("Apple", 1.50, 3)
        cart.add_item("Banana", 0.75, 2)
        self.assertEqual(cart.total_price(), 6.0)


class TestCheckout(unittest.TestCase):
    def test_single_item_receipt(self):
        cart = ShoppingCart()
        cart.add_item("Apple", 1.50, 3)
        expected = "Receipt:\n- Apple x3: $4.50\nTotal: $4.50"
        self.assertEqual(cart.checkout(), expected)

    def test_multiple_items_receipt(self):
        cart = ShoppingCart()
        cart.add_item("Apple", 1.50, 3)
        cart.add_item("Banana", 0.75, 2)
        expected = "Receipt:\n- Apple x3: $4.50\n- Banana x2: $1.50\nTotal: $6.00"
        self.assertEqual(cart.checkout(), expected)

    def test_empty_cart_receipt(self):
        cart = ShoppingCart()
        expected = "Receipt:\nTotal: $0.00"
        self.assertEqual(cart.checkout(), expected)


if __name__ == "__main__":
    unittest.main()
