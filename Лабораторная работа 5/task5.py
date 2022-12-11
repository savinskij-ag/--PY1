import random

chars = 'abcdefghijkmnpqrstuvwxyzABCDEFGHJKLMNPQRSTUVWXYZ0123456789'

def get_random_password(n: int) -> str:
  password = random.sample(chars, n)
  return ''.join(password)

print(get_random_password(8))
