from measurements import measure_time

def linear_search(numbers, target):
    for number in numbers:
        if number == target:
            return True
    return False

for n in [10_000, 100_000, 1_000_000]:
    numbers = list(range(n))
    elapsed = measure_time(linear_search, numbers, -1)
    print(f"n={n:>10} | time={elapsed:.6f}")
