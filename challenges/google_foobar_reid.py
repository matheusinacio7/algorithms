def get_next_prime(target, array):
  isPrime = True

  for existing_prime in array:
    if (target % existing_prime == 0):
      isPrime = False
    if (target / existing_prime < 2):
      break
  
  if (isPrime):
    return target
  return get_next_prime(target + 1, array)

def get_minion_index(n):
  rolling_primes = [2]
  rolling_string = '2'
  next_prime = 3
  
  while len(rolling_string) < n + 6:
    rolling_primes.append(next_prime)
    rolling_string += str(next_prime)
    next_prime = get_next_prime(next_prime + 1, rolling_primes)

  return rolling_string[n:n + 5]

import json

def try_get_cached_primes():
  try:
    file = open('./primes.json', 'r')
    parsed_primes = json.load(file)
    file.close()
    return parsed_primes
  except IOError:
    return [2]

def save_primes_to_cache(primes):
  try:
    prime_string = json.dumps(primes)
    file = open('./primes.json', 'w')
    file.write(prime_string)
    file.close()
  except IOError:
    print('Failed to save primes to cache')
    

def get_minion_index_cache(n):
  rolling_primes = try_get_cached_primes()
  rolling_string = '2'
  has_cache_increased = False
  next_prime = 3
  next_prime_index = 1

  while len(rolling_string) < n + 6:
    rolling_string += str(next_prime)
    largest_existing_prime = rolling_primes[len(rolling_primes) - 1]

    if (largest_existing_prime < next_prime):
      rolling_primes.append(next_prime)

    if (largest_existing_prime <= next_prime):
      next_prime = get_next_prime(next_prime + 1, rolling_primes)
      has_cache_increased = True
    else:
      next_prime = rolling_primes[next_prime_index + 1]
    
    next_prime_index += 1

  if has_cache_increased:
    save_primes_to_cache(rolling_primes)
  
  return rolling_string[n:n + 5]
