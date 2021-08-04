from google_foobar_reid import *

def test_get_minion_index():
  expected_string = '23571'
  assert(get_minion_index(0)) == expected_string

  expected_string = '71113'
  assert(get_minion_index(3)) == expected_string

  expected_string = '92329'
  assert(get_minion_index(11)) == expected_string

  expected_string = '19319'
  assert(get_minion_index(100)) == expected_string

def test_get_minion_index_cache():
  expected_string = '23571'
  assert(get_minion_index_cache(0)) == expected_string

  expected_string = '71113'
  assert(get_minion_index_cache(3)) == expected_string

  expected_string = '92329'
  assert(get_minion_index_cache(11)) == expected_string

  expected_string = '19319'
  assert(get_minion_index_cache(100)) == expected_string
