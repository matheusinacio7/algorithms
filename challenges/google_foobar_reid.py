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
