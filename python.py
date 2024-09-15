# List of fruits with associated values
fruits = [
    ("Apple", 10),
    ("Orange", 8),
    ("Banana", 3),
    ("Strawberry", 6),
    ("Kiwi", 12),
    ("Pineapple", 20)
]

# Print fruit names with their indices (starting from 1)
for index, (fruit, value) in enumerate(fruits, start=1):
    print(f"{index}. {fruit}")

# Ask the user to enter a number between 1 and 6
user_input = int(input("Enter a number from 1 to 6: "))

# Check if input is within the valid range
if 1 <= user_input <= fruit.length:
    # Get the value associated with the entered index
    selected_value = fruits[user_input - 1][1]
    print(f"The value associated with the selected fruit is: {selected_value}")
else:
    print("Invalid input. Please enter a number between 1 and 6.")
