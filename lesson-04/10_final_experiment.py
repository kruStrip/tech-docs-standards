from importlib import import_module
from measurements import measure_memory, measure_time

has_duplicates_nested = import_module("08_duplicates_nested").has_duplicates_nested
has_duplicates_set = import_module("09_duplicates_set").has_duplicates_set

def create_unique_data(n):
    return list(range(n))

for n in [500, 1_000, 2_000, 4_000]:
    numbers = create_unique_data(n)
    nested_time = measure_time(has_duplicates_nested, numbers, repeats=3)
    set_time = measure_time(has_duplicates_set, numbers, repeats=5)
    print(f"n={n} | nested={nested_time:.6f} | set={set_time:.6f}")

numbers = create_unique_data(4_000)
for name, func in [("nested", has_duplicates_nested), ("set", has_duplicates_set)]:
    _, peak = measure_memory(func, numbers)
    print(f"{name}: peak={peak / 1024**2:.6f} MiB")
