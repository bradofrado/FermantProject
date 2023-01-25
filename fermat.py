import random


def prime_test(N, k):
	# This is main function, that is connected to the Test button. You don't need to touch it.
	return fermat(N,k), miller_rabin(N,k)


# Time: Has n recursive calls and does 2 or 3 multiplies and one division at each call, so overall
# it has complexity O(n^3)
# Space: Since we have to store x and y recursively n times, we will have O(n^2) space
def mod_exp(x, y, N):
  if y == 0: 
    return 1
  z = mod_exp(x, y // 2, N)
  even = y % 2
  if even == 0:
    return z * z % N
  else:
    return z * z * x % N
	
#Time: subtraction (n), multiplications (k*n^2) and division (n^2) is O(k*n^2)
#Space: We only have to store k, so O(k)
def fprobability(k):
    return 1 - .5**k

#Time: subtraction (n), multiplications (k*n^2) and division (n^2) is O(k*n^2)
#Space: We only have to store k, so O(k)
def mprobability(k):
    return 1 - .25**k


#Time: The dominant factor in each loop is the mod_exp which is O(n^3). 
# Doing this k times is O(k*n^3)
#Space: We do not need to store anything on the stack, so we will have the space of our biggest
# variable which is mod_exp or O(n^2)
def fermat(N,k):
    for i in range(k):
      a = random.randint(2, N - 1)
      mod = mod_exp(a, N-1, N)
      if mod != 1:
        return "composite"
    return "prime"

#Time: Our complexity is the complexity of the help function O(n^4) k times or O(k*n^4)
#Space: since we are reusing variables, our complexity is that of the helper function or O(n^2)
def miller_rabin(N,k):
  for i in range(k):
    a = random.randint(2, N - 1)
    if miller_rabin_helper(a, N - 1, N) == "composite":
      return "composite"
  return "prime"

#Time: We have n recursive calls of a dominant mod_exp O(n^3). This makes O(n^4) in all
#Space: Since we are resuing the variables and none are on the stack, we just have the complexity
# of mod_exp which is O(n^2)
def miller_rabin_helper(a, e, N):
  mod = mod_exp(a, e, N)
  if (mod != 1):
    #mod == -1 and mod = N - 1 are the same
    if mod != N - 1:
      return "composite"
    else:
      return "prime"
  #If we cannot divide by two anymore then we are done
  if e % 2 != 0:
    return "prime"
  return miller_rabin_helper(a, e // 2, N)