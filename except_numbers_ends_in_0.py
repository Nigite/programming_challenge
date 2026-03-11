print("Numbers from 0 to 100, excluding those ending in zero: ", end="")
num = []
for i in range(101):
    if i % 10 != 0:
        num.append(str(i))
final_output = ", ".join(num)
print(final_output)