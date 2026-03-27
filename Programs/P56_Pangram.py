(
total = 0
for i in range(1, n):
    if n % i == 0:
        total += i

sum_val = 0
for j in range(1, n):
    if n % j == 0:
        sum_val += j
|
total = sum(x for x in range(1, n) if n % x == 0)

sum_val = sum(i for i in range(1, n) if n % i == 0)
)

print("Math ready")
