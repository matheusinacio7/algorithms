from collections import deque

def breadth_first_search(graph, root, conditionFunc):
  def bfs_recursion(graph, queue, conditionFunc, verified):
    if len(queue) <= 0:
      return False

    current = queue.popleft()

    if current in verified:
      return bfs_recursion(graph, queue, conditionFunc, verified)

    if conditionFunc(current):
      return current

    queue += graph[current]
    verified.append(current)
    return bfs_recursion(graph, queue, conditionFunc, verified)

  queue = deque()
  queue += graph[root]
  verified = []
  return bfs_recursion(graph, queue, conditionFunc, verified)
