num_1 = float(input("Input first number: "))
num_2 = float(input("Input second number: "))
if num_2 == 0:
    print(f"You can't divide by 0!")
else:
    print(f"The remainder of two numbers are", num_1 % num_2)