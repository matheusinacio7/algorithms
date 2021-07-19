# Big O runtime
# O(log n)
import math

def recursionBinary(array, target, low, high):
  mid = math.floor((low + high) / 2)

  if (array[mid] == target):
    return mid
  elif (low > high):
    return -1
  elif (array[mid] < target):
    return recursionBinary(array, target, mid + 1, high)
  else:
    return recursionBinary(array, target, low, mid - 1)

def binarySearch(array, target):
  return recursionBinary(array, target, 0, len(array) - 1)
