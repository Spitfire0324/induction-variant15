def f(n):
    return 2**(n + 2) * 3**n + 5 * n - 4


m = 25

bad = []
for n in range(1, 101):
    if f(n) % m != 0:
        bad.append(n)

if len(bad) == 0:
    print("Контрприкладів не знайдено")
else:
    print("Знайдено контрприклади для n:")
    print(bad)
