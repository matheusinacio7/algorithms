from google_foobar_reid import *

def test_get_minion_index():
  expected_string = '35711'
  assert(get_minion_index(0)) == expected_string

  expected_string = '23293'
  assert(get_minion_index(11)) == expected_string

  expected_string = '93197'
  assert(get_minion_index(100)) == expected_string
