numbers = []
for i in range(10):
    num = input((f"Enter number {i + 1} out of 10: "))
    numbers.append(num)
duplicated_num = set()
first_time_num = []
for num in numbers:
    if num not in duplicated_num:
        first_time_num.append(str(num))
        duplicated_num.add(num)
print("Numbers with first entries only: ", end="")
print(", ".join(first_time_num))
