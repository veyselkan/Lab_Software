class ShoppingCart:
    def __init__(self):
        self._items = {}
        self._discount = None
        self._available_discounts = {
            "SAVE10": {"min_order": 0, "percentage": 10},
            "SAVE20": {"min_order": 50, "percentage": 20}
        }

    def add_item(self, name, price, quantity=1):
        if quantity <= 0:
            raise ValueError("Quantity must be positive")

        if name in self._items:
            # DÜZELTME 1: Üzerine yazmak yerine mevcut miktara ekliyoruz (+=)
            self._items[name]["quantity"] += quantity
        else:
            self._items[name] = {"price": price, "quantity": quantity}

    def remove_item(self, name):
        if name in self._items:
            del self._items[name]

    def get_total(self):
        subtotal = sum(item["price"] * item["quantity"] for item in self._items.values())

        if self._discount:
            # DÜZELTME 2: // yerine / kullanarak yüzdelik hesabı düzelttik
            discount_amount = subtotal * (self._discount["percentage"] / 100)
            return subtotal - discount_amount

        return subtotal

    def apply_discount(self, code):
        if code not in self._available_discounts:
            raise ValueError("Invalid discount code")

        discount = self._available_discounts[code]
        subtotal = self.get_total()

        # DÜZELTME 3: Sınır koşulunu >= olarak değiştirdik
        if subtotal >= discount["min_order"]:
            self._discount = discount
        else:
            raise ValueError(f"A minimum order of ${discount['min_order']:.2f} is required for code {code}. Your current total is ${subtotal:.2f}.")

    def get_item_count(self):
        # DÜZELTME 4: TDD ile yazılan metodu implemente ettik
        return sum(item["quantity"] for item in self._items.values())
