from algorithms.dijkstra_algorithm import *

def test_dijkstra_algorithm():
  graph = {
    'a': {
      'b': 5,
      'c': 2,
    },
    'b': {
      'd': 7,
      'e': 2,
    },
    'c': {
      'b': 8,
      'e': 7,
    },
    'd': {
      'e': 6,
      'f': 3,
    },
    'e': {
      'f': 1,
    },
    'f': {},
  }

  expected_costs = {'b': 5, 'c': 2, 'd': 12, 'e': 7, 'f': 8}
  assert(dijkstra_algorithm(graph, 'a')['costs']) == expected_costs

  expected_traceback = ['a', 'b', 'e', 'f']
  assert(dijkstra_traceback(graph, 'a', 'f')) == expected_traceback
