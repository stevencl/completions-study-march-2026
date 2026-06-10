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
    def find_item(self, name: str):
        for item in self.items:
            if item['name'] == name:
                return item
        return None

    def total_price(self):
        return sum(item['price'] * item['quantity'] for item in self.items)

    def checkout(self):
        lines = ["Receipt:"]
        for item in self.items:
            line_total = item['price'] * item['quantity']
            lines.append(f"- {item['name']} x{item['quantity']}: ${line_total:.2f}")
        lines.append(f"Total: ${self.total_price():.2f}")
        return "\n".join(lines)
