import math
m = int(input("m: "))
n = int(input("n: "))
N = m + n
entropy = ((-m/N) * math.log2(m/N)) - ((n/N) * math.log2(n/N))
print(round(entropy, 3))