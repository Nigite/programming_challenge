print("Even numbers from 0 to 100: ",end="")
even_numbers = []
for i in range(0,101,2):
    even_numbers.append(str(i))
final_output = ", ".join(even_numbers)
print(final_output)