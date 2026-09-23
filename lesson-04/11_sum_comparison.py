from measurements import measure_time

def manual_sum(numbers):
    result = 0
    for number in numbers:
        result += number
    return result

def builtin_sum(numbers):
    return sum(numbers)

numbers = list(range(1_000_000))
print(f"manual: {measure_time(manual_sum, numbers):.6f}")
print(f"sum():  {measure_time(builtin_sum, numbers):.6f}")
