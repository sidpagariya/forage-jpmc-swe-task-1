import unittest
from client3 import getDataPoint, getRatio

class ClientTest(unittest.TestCase):
  def test_getDataPoint_calculatePrice(self):
    quotes = [
      {'top_ask': {'price': 121.2, 'size': 36}, 'timestamp': '2019-02-11 22:06:30.572453', 'top_bid': {'price': 120.48, 'size': 109}, 'id': '0.109974697771', 'stock': 'ABC'},
      {'top_ask': {'price': 121.68, 'size': 4}, 'timestamp': '2019-02-11 22:06:30.572453', 'top_bid': {'price': 117.87, 'size': 81}, 'id': '0.109974697771', 'stock': 'DEF'}
    ]
    """ ------------ Add the assertion below ------------ """
    assert getDataPoint(quotes[0]) == ('ABC', 120.48, 121.2, 120.84)
    assert getDataPoint(quotes[1]) == ('DEF', 117.87, 121.68, 119.775)

  def test_getDataPoint_calculatePriceBidGreaterThanAsk(self):
    quotes = [
      {'top_ask': {'price': 119.2, 'size': 36}, 'timestamp': '2019-02-11 22:06:30.572453', 'top_bid': {'price': 120.48, 'size': 109}, 'id': '0.109974697771', 'stock': 'ABC'},
      {'top_ask': {'price': 121.68, 'size': 4}, 'timestamp': '2019-02-11 22:06:30.572453', 'top_bid': {'price': 117.87, 'size': 81}, 'id': '0.109974697771', 'stock': 'DEF'}
    ]
    """ ------------ Add the assertion below ------------ """
    assert getDataPoint(quotes[0]) == ('ABC', 120.48, 119.2, 119.84)
    assert getDataPoint(quotes[1]) == ('DEF', 117.87, 121.68, 119.775)


  """ ------------ Add more unit tests ------------ """
  def test_getRatio_calculateRatio(self):
    assert getRatio(100, 50) == 2
    assert getRatio(50, 100) == 0.5
    assert getRatio(0, 100) == 0
    assert getRatio(100, 0) == None



if __name__ == '__main__':
    unittest.main()
