class ShoppingCart:
    def __init__(self):
        self.items = []

    def add_item(self, name: str, price: float, quantity: int = 1):
        self.items.append({
            'name': name,
            'price': price,
            'quantity': quantity
        })

    def remove_item(self, name: str):
        self.items = [item for item in self.items if item['name'] != name]

    # ---- Add your methods below this line ----

