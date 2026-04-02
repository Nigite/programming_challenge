numbers = []
print("---Lowest Number Tracker---")
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
    lowest = min(numbers)
    print(f"The lowest number was: {lowest}")
else:
    print("You didn't input any valid numbers!")