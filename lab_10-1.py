# Initialize sum to 0
total_sum = 0

while True:
    # Prompt user for input
    user_input = input("Enter a number (or -1 to end): ")

    # Check if the input is a number
    if user_input.isdigit():
        # Convert the input to an integer and add to the sum
        total_sum += int(user_input)
    elif user_input == "-1":
        # If user enters -1, end the loop
        break
    else:
        print("Invalid input. Please enter a number or -1.")

# Display the sum of all numbers entered
print(f"The sum of all numbers entered is: {total_sum}")
