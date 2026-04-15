import unittest
from cart import ShoppingCart

class TestShoppingCart(unittest.TestCase):
    def setUp(self):
        """Her testten önce temiz bir sepet oluşturulur."""
        self.cart = ShoppingCart()

    
    def test_add_item_calculates_correct_subtotal(self):
        self.cart.add_item("Apple", 2.50, 2)
        self.assertEqual(self.cart.get_total(), 5.00)

    def test_add_existing_item_increases_quantity_cumulatively(self):
        self.cart.add_item("Apple", 2.50, 1)
        self.cart.add_item("Apple", 2.50, 2)
        self.assertEqual(self.cart.get_item_count(), 3)
        self.assertEqual(self.cart.get_total(), 7.50)

    def test_remove_existing_item_updates_total(self):
        self.cart.add_item("Apple", 2.50, 2)
        self.cart.add_item("Banana", 1.00, 1)
        self.cart.remove_item("Apple")
        self.assertEqual(self.cart.get_total(), 1.00)

    def test_add_item_with_zero_or_negative_quantity_raises_value_error(self):
        with self.assertRaises(ValueError):
            self.cart.add_item("Apple", 2.50, -1)

    def test_apply_valid_percentage_discount_reduces_total(self):
        self.cart.add_item("Headphones", 100.00, 1)
        self.cart.apply_discount("SAVE10")
        self.assertEqual(self.cart.get_total(), 90.00)

    def test_apply_discount_exactly_at_boundary_threshold_applies_successfully(self):
        self.cart.add_item("Keyboard", 50.00, 1)
        self.cart.apply_discount("SAVE20")
        self.assertEqual(self.cart.get_total(), 40.00)

    def test_get_item_count_returns_correct_total_quantity(self):
        self.cart.add_item("Apple", 2.00, 2)
        self.cart.add_item("Banana", 1.00, 3)
        self.assertEqual(self.cart.get_item_count(), 5)

if __name__ == '__main__':
    unittest.main(verbosity=2)