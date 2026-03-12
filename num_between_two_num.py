num_1 = int(input("Enter first number: "))
num_2 = int(input("Enter second number: "))
start_num = min(num_1, num_2)
end_num = max(num_1, num_2)
num_between = []
for i in range(start_num + 1, end_num):
    num_between.append(str(i))
if num_between:
    final_result = ", ".join(num_between)
    print(f"The numbers between {start_num} and {end_num} is: ", end="")
    print(final_result)
else:
    print(f"There are no numbers in between {start_num} and {end_num}!")