def quick_sort(array, comparing_function):
  if (len(array) < 2):
    return array
  pivot = array[0]
  above = [i for i in array[1:] if comparing_function(i, pivot) >= 0]
  below = [i for i in array[1:] if comparing_function(i, pivot) < 0]
  return quick_sort(below, comparing_function) + [pivot] + quick_sort(above, comparing_function)
