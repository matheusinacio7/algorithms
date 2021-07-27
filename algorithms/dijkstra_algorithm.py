# This algorithm doesn't treat special cases such as
#   when there are negative vectors, or
#   when the target can't be reached from the root

def get_initial_costs(graph, root):
  costs = {}
  keys = [node for node in graph if node != root]

  for key in keys:
    if key in graph[root]:
      costs[key] = graph[root][key]
    else:
      costs[key] = float('inf')
  
  return costs


def get_initial_parents(graph, root):
  parents = {}

  for key in graph[root]:
    parents[key] = root

  return parents


def get_lowest_cost_key(costs, visited):
  lowest = float('inf')
  lowest_key = None
  for key in costs:
    if (costs[key] < lowest and key not in visited):
      lowest = costs[key]
      lowest_key = key
  return lowest_key


def dijkstra_algorithm(graph, root):
  costs = get_initial_costs(graph, root)
  parents = get_initial_parents(graph, root)
  visited = []

  node = get_lowest_cost_key(costs, visited)

  while (node is not None):
    neighbors = graph[node].keys()

    for key in neighbors:
      new_cost = costs[node] + graph[node][key]
      if (new_cost < costs[key]):
        costs[key] = new_cost
        parents[key] = node
    
    visited.append(node)
    node = get_lowest_cost_key(costs, visited)
  
  result = { 'costs': costs, 'parents': parents }
  return result


def dijkstra_traceback(graph, root, target):
  parents = dijkstra_algorithm(graph, root)['parents']
  current_step = target
  steps = [ current_step ]

  while (current_step is not root):
    current_step = parents[current_step]
    steps = [current_step] + steps[0:]
  
  return steps
