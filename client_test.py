import unittest
from client3 import getDataPoint

class ClientTest(unittest.TestCase):
  def test_getDataPoint_calculatePrice(self):
    quotes = [
      {'top_ask': {'price': 121.2, 'size': 36}, 'timestamp': '2019-02-11 22:06:30.572453', 'top_bid': {'price': 120.48, 'size': 109}, 'id': '0.109974697771', 'stock': 'ABC'},
      {'top_ask': {'price': 121.68, 'size': 4}, 'timestamp': '2019-02-11 22:06:30.572453', 'top_bid': {'price': 117.87, 'size': 81}, 'id': '0.109974697771', 'stock': 'DEF'}
    ]
    """ ------------ Add the assertion below ------------ """
     # First Let's Calculate expected price for ABC and DEF
    expected_price_ABC = (121.2 + 120.48) / 2
    expected_price_DEF = (121.68 + 117.87) / 2

    # Then let's Test getDataPoint function
    stock_ABC, price_ABC = getDataPoint(quotes[0])
    stock_DEF, price_DEF = getDataPoint(quotes[1])

    self.assertEqual(stock_ABC, 'ABC')
    self.assertAlmostEqual(price_ABC, expected_price_ABC, places=2)

    self.assertEqual(stock_DEF, 'DEF')
    self.assertAlmostEqual(price_DEF, expected_price_DEF, places=2)

  def test_getDataPoint_calculatePriceBidGreaterThanAsk(self):
    quotes = [
      {'top_ask': {'price': 119.2, 'size': 36}, 'timestamp': '2019-02-11 22:06:30.572453', 'top_bid': {'price': 120.48, 'size': 109}, 'id': '0.109974697771', 'stock': 'ABC'},
      {'top_ask': {'price': 121.68, 'size': 4}, 'timestamp': '2019-02-11 22:06:30.572453', 'top_bid': {'price': 117.87, 'size': 81}, 'id': '0.109974697771', 'stock': 'DEF'}
    ]
    """ ------------ Add the assertion below ------------ """

  # we calculate expected price for ABC and DEF
    expected_price_ABC = (119.2 + 120.48) / 2
    expected_price_DEF = (121.68 + 117.87) / 2


    # Test getDataPoint function
    stock_ABC, price_ABC = getDataPoint(quotes[0])
    stock_DEF, price_DEF = getDataPoint(quotes[1])

    self.assertEqual(stock_ABC, 'ABC')
    self.assertAlmostEqual(price_ABC, expected_price_ABC, places=2)

    self.assertEqual(stock_DEF, 'DEF')
    self.assertAlmostEqual(price_DEF, expected_price_DEF, places=2)



  """ ------------ Add more unit tests ------------ """
  # Test empty quotes
  def test_getDataPoint_empty_quotes(self):
      quotes = []
      stock, bid_price, ask_price, price = getDataPoint({})
      self.assertIsNone(stock)
      self.assertIsNone(bid_price)
      self.assertIsNone(ask_price)
      self.assertIsNone(price)

  # Test if missing keys in quotes
  def test_getDataPoint_missing_keys(self):
      quotes = [
          {'top_ask': {'price': 121.2}, 'timestamp': '2019-02-11 22:06:30.572453', 'id': '0.109974697771', 'stock': 'ABC'},
          {'top_bid': {'price': 117.87, 'size': 81}, 'id': '0.109974697771', 'stock': 'DEF'}
      ]
      stock_ABC, bid_price_ABC, ask_price_ABC, price_ABC = getDataPoint(quotes[0])
      stock_DEF, bid_price_DEF, ask_price_DEF, price_DEF = getDataPoint(quotes[1])
      self.assertEqual(stock_ABC, 'ABC')
      self.assertIsNone(bid_price_ABC)
      self.assertIsNone(price_ABC)
      self.assertEqual(stock_DEF, 'DEF')
      self.assertIsNone(ask_price_DEF)
      self.assertIsNone(price_DEF)

    # Test how the function handles quotes with non-numeric bid and ask prices.
  def test_getDataPoint_non_numeric_prices(self):
    quotes = [
        {'top_ask': {'price': 'invalid_price', 'size': 36}, 'timestamp': '2019-02-11 22:06:30.572453', 'top_bid': {'price': 120.48, 'size': 109}, 'id': '0.109974697771', 'stock': 'ABC'},
        {'top_ask': {'price': 121.68, 'size': 4}, 'timestamp': '2019-02-11 22:06:30.572453', 'top_bid': {'price': 'invalid_price', 'size': 81}, 'id': '0.109974697771', 'stock': 'DEF'}
    ]
    stock_ABC, bid_price_ABC, ask_price_ABC, price_ABC = getDataPoint(quotes[0])
    stock_DEF, bid_price_DEF, ask_price_DEF, price_DEF = getDataPoint(quotes[1])
    self.assertEqual(stock_ABC, 'ABC')
    self.assertEqual(bid_price_ABC, 120.48)
    self.assertIsNone(ask_price_ABC)
    self.assertIsNone(price_ABC)
    self.assertEqual(stock_DEF, 'DEF')
    self.assertIsNone(bid_price_DEF)
    self.assertEqual(ask_price_DEF, 121.68)
    self.assertIsNone(price_DEF)

# Additional Test for getRatio function 
class RatioTest(unittest.TestCase):
    def test_getRatio(self):
        from client3 import getRatio
        self.assertIsNone(getRatio(10, 0))
        self.assertEqual(getRatio(10, 5), 2)
        self.assertAlmostEqual(getRatio(3.5, 2.5), 1.4, places=2)

if __name__ == '__main__':
    unittest.main()
