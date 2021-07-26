from algorithms.quick_sort import *

def test_selection_sort():
  def compare_ascending(a, b):
    if (a > b):
      return 1
    if (a == b):
      return 0
    return -1

  def compare_descending(a, b):
    if (a < b):
      return 1
    if (a == b):
      return 0
    return -1
    

  test_numbers = [80, 20, 0, 40, 10, 30, 50, 60, 70]
  assert(quick_sort(test_numbers, compare_ascending)) == [0, 10, 20, 30, 40, 50, 60, 70, 80]

  test_numbers = [80, 20, 0, 40, 10, 30, 50, 60, 70]
  assert(quick_sort(test_numbers, compare_descending)) == [80, 70, 60, 50, 40, 30, 20, 10, 0]

  test_strings = ['today is a good day', 'gotta study', 'vqv']
  assert(quick_sort(test_strings, compare_ascending)) == ['gotta study', 'today is a good day', 'vqv']

  test_strings = ['today is a good day', 'gotta study', 'vqv']
  assert(quick_sort(test_strings, compare_descending)) == ['vqv', 'today is a good day', 'gotta study']

  def compare_descending_score(a, b):
    return compare_descending(a.score, b.score)

  class Player:
    def __init__(self, name, score):
      self.name = name
      self.score = score

  john_doe = Player('John', 30)
  jane_doe = Player('Jane', 50)
  fulano = Player('Fulano', 100)

  test_players = [jane_doe, john_doe, fulano]

  assert(quick_sort(test_players, compare_descending_score) == [fulano, jane_doe, john_doe])
