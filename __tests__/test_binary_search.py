from algorithms.binary_search import *

def test_binarySearch():
  test_array = [10, 20, 30, 40, 50, 60, 70, 80, 90]

  assert binary_search(test_array, 10) == 0
  assert binary_search(test_array, 90) == 8
  assert binary_search(test_array, 40) == 3
  assert binary_search(test_array, 50) == 4
  assert binary_search(test_array, -30) == -1
  assert binary_search(test_array, 200) == -1