odd_count = []
current_number = 1
while current_number <= 100:
    odd_count.append(str(current_number))
    current_number += 2
final_result = ", ".join(odd_count)
print("Odd numbers count from 1 to 100: ", end="")
print(final_result)