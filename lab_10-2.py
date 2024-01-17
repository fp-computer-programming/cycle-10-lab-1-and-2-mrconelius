# List of numbers
numbers = [1, 3, 6, 9, 12, 15, 18, 21, 24, 27, 30]

# Iterate through the list
for number in numbers:
    # Check if the number is not a multiple of 3
    if number % 3 != 0:
        # Skip to the next iteration using continue
        continue
    
    # Print the number if it is a multiple of 3
    print(number)
