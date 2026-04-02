numbers = []
print("---Number Sorter---")
print("(Type any letter or word to stop)")
while True:
    try:
        user_input = input("Enter a number: ")
        num = float(user_input)
        numbers.append(num)
    except ValueError:
        print("\nInvalid input detected. Stopping the program.")
        break
if numbers:
    numbers.sort()
    sorted_num = [str(n) for n in numbers]
    print("Numbers from lowest to highest: ", end="")
    print(", ".join(sorted_num))
else:
    print("You didn't input any valid numbers!")
