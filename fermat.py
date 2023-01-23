import random


def prime_test(N, k):
	# This is main function, that is connected to the Test button. You don't need to touch it.
	return fermat(N,k), miller_rabin(N,k)


def mod_exp(x, y, N):
  if y == 0: 
    return 1
  z = mod_exp(x, y // 2, N)
  even = y % 2
  if even == 0:
    return z * z % N
  else:
    return z * z * x % N
	

def fprobability(k):
    return 1 - .5**k


def mprobability(k):
    return 1 - .25**k


def fermat(N,k):
    for i in range(k):
      a = random.randint(2, N - 1)
      mod = mod_exp(a, N-1, N)
      if mod != 1:
        return "composite"
    return "prime"

def miller_rabin(N,k):
  for i in range(k):
    a = random.randint(2, N - 1)
    e = N-1
    while True:
      mod = mod_exp(a, e, N)
      if (mod != 1):
        #mod == -1 and mod = N - 1 are the same
        if mod != -1 and mod != N - 1:
          return "composite"
        else:
          break
      #Loop until we cannot divide by two anymore
      if e % 2 != 0:
        break
      e = e // 2
  return "prime"