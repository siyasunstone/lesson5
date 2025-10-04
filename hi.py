base = float(input("Enter base: "))
exp = int(input("Enter power: "))
res = 1
for _ in range(abs(exp)):
    res *= base
print(res if exp >= 0 else 1/res)
