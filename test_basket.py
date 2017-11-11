import unittest
from basket import Basket


class TestBasket(unittest.TestCase):

    def setUp(self):
        self.basket = Basket()

    def test_add_items(self):
        self.basket.add_items('CH1')
        self.assertEqual(self.basket.items.count('CH1'), 1)

        self.basket.add_items('CH1')
        self.assertEqual(self.basket.items.count('CH1'), 2)

        self.basket.check_out()
        self.assertEqual(len(self.basket.items), 0)

    def test_checkout(self):
        self.basket.add_items('CH1, AP1, CF1, MK1')
        self.basket.check_out()
        self.assertEqual(len(self.basket.items), 0)

    def test_milk_dis(self):
        self.basket.add_items('CH1, AP1, CF1, MK1')
        self.assertAlmostEqual(self.basket.total(), 20.34, places=2)

    def test_simple_add(self):
        self.basket.add_items('MK1, AP1')
        self.assertAlmostEqual(self.basket.total(), 10.75, places=2)

    def test_BOGO(self):
        self.basket.add_items('CF1')
        self.assertAlmostEqual(self.basket.total(), 11.23, places=2)
        self.basket.check_out()

        self.basket.add_items('CF1, CF1')
        self.assertAlmostEqual(self.basket.total(), 11.23, places=2)

        self.basket.add_items('CF1, CF1')
        self.assertAlmostEqual(self.basket.total(), 22.46, places=2)

    def test_get_disc(self):
        item = {'Code': 'AP1', 'Price': 4.50}
        self.assertEqual(self.basket.get_discount_code(item),
                         {'name': 'APPL', 'disc': 4.50})
        item = {'Code': 'AP1', 'Price': 2.25}
        self.assertEqual(self.basket.get_discount_code(item),
                         {'name': 'APOM', 'disc': .5})
        item = {'Code': 'AP1', 'Price': 3.00}
        self.assertEqual(self.basket.get_discount_code(item),
                         {'name': 'APOM', 'disc': .5})

        item = {'Code': 'MK1', 'Price': 0}
        self.assertEqual(self.basket.get_discount_code(item),
                         {'name': 'CHMK', 'disc': 4.75})

        item = {'Code': 'CF1', 'Price': 0}
        self.assertEqual(self.basket.get_discount_code(item),
                         {'name': 'BOGO', 'disc': 11.23})

    def test_APPL_disc(self):
        self.basket.add_items('AP1, AP1, CH1, AP1')
        self.assertAlmostEqual(self.basket.total(), 16.61, places=2)

    def test_APOM_disc(self):
        self.basket.add_items('AP1, AP1, CH1, AP1, OM1')
        self.assertAlmostEqual(self.basket.total(), 18.05, places=2)


if __name__ == '__main__':
    unittest.main()
