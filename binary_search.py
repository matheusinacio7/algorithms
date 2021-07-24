# Big O runtime
# O(log n)
import math

def recursion_binary(array, target, low, high):
  mid = math.floor((low + high) / 2)

  if (array[mid] == target):
    return mid
  elif (low > high):
    return -1
  elif (array[mid] < target):
    return recursion_binary(array, target, mid + 1, high)
  else:
    return recursion_binary(array, target, low, mid - 1)

def binary_search(array, target):
  return recursion_binary(array, target, 0, len(array) - 1)
