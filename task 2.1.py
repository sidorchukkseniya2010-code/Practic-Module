import random

random.seed(42)
print("random()           :", round(random.random(), 6))
print("uniform(1, 10)     :", round(random.uniform(1, 10), 3))
print("randint(1, 6)      :", random.randint(1, 6))
print("randrange(0,100,5) :", random.randrange(0, 100, 5))

print("\n--- Бросок двух кубиков, 5 раз ---")
for i in range(1, 6):
    a, b = random.randint(1, 6), random.randint(1, 6)
    print(f"Бросок {i}: {a} + {b} = {a + b}")

print("\n--- Статистика 10000 бросков одного кубика ---")
random.seed(2026)
counts = {i: 0 for i in range(1, 7)}
N = 10_000

for _ in range(N):
    counts[random.randint(1, 6)] += 1

for face, cnt in sorted(counts.items()):
    percentage = cnt / N * 100
    deviation = percentage - 16.67
    bar = "#" * (cnt // 50)
    dev_sign = "+" if deviation >= 0 else ""
    print(f"{face}: {cnt:5d} ({percentage:5.2f}%) | Отклонение: {dev_sign}{deviation:.2f}% | {bar}")
