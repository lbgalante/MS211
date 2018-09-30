from pprint import pprint
from numpy import dot, subtract
import time

def create_system(n):
  A = [[(2.0 if i == j else -1.0 if abs(i-j) == 1 else 0.0) for i in range(n)] for j in range(n)]
  x = [4*( (k/(n+1)) - (k/(n+1))**2 ) for k in range(1, n+1)] # analytic solution
  b_val = 8.0 / (n+1)**2
  b = [b_val for i in range(n)]
  return (A, x, b)

def solve_system(n):
  A, x, b = create_system(n)

  print("A: ")
  pprint(A, width=30)
  print("b: ")
  pprint(b, width=30)
  print("x: ")
  pprint(x, width=30)

  start = time.time()
  _, _, _, x1 = decompose_and_solve(A, b)
  end = time.time()
  t1 = end - start
  print("\nx1 = decompose_and_solve(A, b): ")
  pprint(x1, width=30)

  start = time.time()
  _, _, _, x2 = tridiagonal_decompose_and_solve(A, b)
  end = time.time()
  t2 = end - start
  print("\nx2 = tridiagonal_decompose_and_solve(A, b): ")
  pprint(x2, width=30)

  e1 = subtract(x, x1)
  print("\nnormal factorization error (x - x1): ")
  pprint(e1, width=30)

  e2 = subtract(x, x2)
  print("\ntridiagonal specific factorization error (x - x2): ")
  pprint(e2, width=30)

  print("\ne1 == e2: " + str((e1 == e2).all()))

  print("\nt1: " + str(t1) + " | t2: " + str(t2))
  print("t1 > t2" if t1 > t2 else "t1 < t2")
  print("t1/t2 == " + str(t1/t2))
