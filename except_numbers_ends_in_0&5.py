print("Numbers from 0 to 100, excluding those ending in 0 or 5: ", end="")
numbers = []
for i in range(101):
    if i % 5 != 0:
        numbers.append(str(i))
final_result = ", ".join(numbers)
print(final_result)