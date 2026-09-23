from measurements import measure_time

def process_pairs(n):
    counter = 0
    for i in range(n):
        for j in range(n):
            counter += 1
    return counter

for n in [100, 200, 400, 800]:
    elapsed = measure_time(process_pairs, n, repeats=5)
    print(f"n={n:>4} | time={elapsed:.6f}")
