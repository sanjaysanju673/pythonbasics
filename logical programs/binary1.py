def to_binary(num):
    """
    Converts an integer to its 8-bit binary representation.

    Parameters:
    num (int): The integer to be converted.

    Returns:
    str: The 8-bit binary representation of the integer.
    """
    return format(num, '08b')

def swap_nibbles(num):
    """
    Swaps the nibbles in an 8-bit number.

    Parameters:
    num (int): The integer whose nibbles are to be swapped.

    Returns:
    int: The integer with swapped nibbles.
    """
    if num < 0 or num > 255:
        raise ValueError("The number must be between 0 and 255.")
    
    left_nibble = (num & 0xF0) >> 4
    right_nibble = (num & 0x0F) << 4
    return left_nibble | right_nibble

def is_power_of_two(num):
    """
    Checks if a number is a power of 2.

    Parameters:
    num (int): The integer to be checked.

    Returns:
    bool: True if the number is a power of 2, False otherwise.
    """
    if num <= 0:
        return False
    return (num & (num - 1)) == 0

def main():
    try:
        num = int(input("Enter an integer (0 to 255): "))
        
        binary_representation = to_binary(num)
        print(f"Binary Representation: {binary_representation}")
        
        swapped_number = swap_nibbles(num)
        print(f"Number after swapping nibbles: {swapped_number}")
        
        is_power = is_power_of_two(swapped_number)
        print(f"Is the resultant number a power of 2? {is_power}")
    
    except ValueError as e:
        print(e)

if __name__ == "__main__":
    main()
