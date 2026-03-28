seen_numbers = set()
print("---Duplicate Number Checker---")
print("(Type any letter or word to stop)")
while True:
    try:
        numbers = input("Enter a number: ")
        num = float(numbers)
        if num in seen_numbers:
            print("Duplicate")
        else:
            print("Unique")
            seen_numbers.add(num)
    except ValueError:
        print("\nInvalid input detected. Stopping the program.")
        break