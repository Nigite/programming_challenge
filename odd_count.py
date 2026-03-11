odd_count = 0
for i in range(10):
    number = float(input(f"Enter number {i + 1} out of 10: "))
    if number % 2 != 0:
        odd_count += 1
print(f"The total odd numbers are {odd_count}!")