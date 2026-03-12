result_num = float(input("Enter number 1 of 10: "))
for i in range(1,10):
    current_number = float(input(f"Enter number {i + 1} of 10: "))
    result_num -= current_number
print(f"The difference of first number minus all the remaining numbers is {result_num}")