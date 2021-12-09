import math

sum = 0
x = math.pi / 4
for n in range(1, 21):
    sum += n * x / math.sin(n * x)
print(sum, ":sum of function\n")

# 2
for n in range(10, 0, -1):
    n /= n**n
    print("Function (N => 0):", n * x / math.sin(n * x))
print()
for n in range(1, 10):
    n **= n ** n
    print("Function (N => ∞):", n * x / math.sin(n * x))
