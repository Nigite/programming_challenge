numbers = []
for i in range(10):
    num = int(input(f"Enter number {i + 1} out of 10: "))
    numbers.append(num)
unique_num = []
for num in numbers:
    if numbers.count(num) == 1:
        unique_num.append(str(num))
if unique_num:
    print("Numbers with no duplication: ", end="")
    print(", ".join(unique_num))
else:
    print("Every number you entered had a duplicate")