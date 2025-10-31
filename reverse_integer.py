def reverse_integer(x):
    sign = -1 if x < 0 else 1
    abs_x = abs(x)
    reversed_num = 0

    while abs_x != 0:
        digit = abs_x % 10
        reversed_num = reversed_num * 10 + digit
        abs_x //= 10

    result = reversed_num * sign
    
    # Standard 32-bit integer overflow check
    if not (-2**31 <= result <= 2**31 - 1):
        return 0
        
    return result

# --- Input Logic ---
try:
    user_num_str = input("Enter an integer to reverse: ")
    user_num = int(user_num_str)
    
    reversed_val = reverse_integer(user_num)
    
    print(f"Original: {user_num}")
    print(f"Reversed: {reversed_val}")

except ValueError:
    print("Invalid input. Please enter a valid whole number.")
