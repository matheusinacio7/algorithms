from algorithms.breadth_first_search import *

def test_breadth_first_search():
  myGraph = {}
  myGraph['Me'] = ['Alice', 'Bob', 'Claire']
  myGraph['Bob'] = ['Anuj', 'Peggy']
  myGraph['Alice'] = ['Peggy']
  myGraph['Claire'] = ['Thom', 'Jonny']
  myGraph['Anuj'] = []
  myGraph['Peggy'] = []
  myGraph['Thom'] = []
  myGraph['Jonny'] = []

  def sellsMangoes(person):
    return person[len(person) - 1] == 'm'

  assert(breadth_first_search(myGraph, 'Me', sellsMangoes)) == 'Thom'
  
