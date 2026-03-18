interface CartItem {
  name: string;
  price: number;
  quantity: number;
}

export class ShoppingCart {
  items: CartItem[] = [];

  addItem(name: string, price: number, quantity: number = 1): void {
    this.items.push({ name, price, quantity });
  }

  removeItem(name: string): void {
    this.items = this.items.filter((item) => item.name !== name);
  }

  // ---- Add your methods below this line ----
}
