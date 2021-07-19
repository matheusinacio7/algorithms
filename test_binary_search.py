from binary_search import *

def test_binarySearch():
  testArray = [10, 20, 30, 40, 50, 60, 70, 80, 90]

  assert binarySearch(testArray, 10) == 0
  assert binarySearch(testArray, 90) == 8
  assert binarySearch(testArray, 40) == 3
  assert binarySearch(testArray, 50) == 4
  assert binarySearch(testArray, -30) == -1
  assert binarySearch(testArray, 200) == -1