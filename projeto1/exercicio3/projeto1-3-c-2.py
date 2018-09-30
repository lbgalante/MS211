ns = [4, 16, 64, 128, 256]
t = [0.0]*len(ns)
m = 10
for j in range(m):
  i = 0
  for n in ns:
    t[i] += solve_system(n)
    i += 1
print("n: t1/t2")
for i in range(len(ns)):
  t[i] = t[i]/m
  print(str(ns[i]) + ": " + str(t[i]))
