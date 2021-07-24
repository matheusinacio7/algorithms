def select_single(array, comparing_function) -> int:
  selected = array[0]
  selected_index = 0

  for i in range(0, len(array)):
    if (comparing_function(selected, array[i])):
      selected = array[i]
      selected_index = i

  return selected_index

def selection_sort(array, comparing_function):
  sortedArray = []

  for i in range(0, len(array)):
    selected_index = select_single(array, comparing_function)
    sortedArray.append(array.pop(selected_index))
  
  return sortedArray
