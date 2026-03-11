# num_1 = float(input("Input first number: "))
# num_2 = float(input("Input second number: "))
# if num_2 == 0:
#     print(f"You can't divide by 0!")
# else:
#     print(f"The remainder of two numbers are", num_1 % num_2)

num_1 = float(input("Enter the first number: "))
num_2 = float(input("Enter the second number: "))

if num_2 != 0:
    remainder = num_1 % num_2
    print(f"The remainder is: {remainder}")
else:
    print("Error: Cannot divide by zero.")