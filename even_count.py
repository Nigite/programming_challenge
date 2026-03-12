even_count = 0
for i in range(10):
    number = float(input(f"Enter number {i + 1} out of 10: "))
    if number % 2 == 0:
        even_count += 1
print(f"The total even numbers are {even_count}!")