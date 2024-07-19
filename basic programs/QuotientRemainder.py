'''@Author: v sanjay kumar
@Date: 2024-07-18 12:00:30
@Last Modified by: v sanjay kumar
@Last Modified time: 2024-07-18 12:30:30
@Title : Flip Coin and print percentage of Heads and Tails

'''

def compute_quotient_and_remainder(dividend, divisor):
    """
    Description:
        Computes the quotient and remainder of the division of two numbers.

    Parameters:
        dividend (int): The number to be divided.
        divisor (int): The number by which to divide.

    Returns:
        tuple: A tuple containing the quotient and remainder.
    """
    quotient = dividend // divisor
    remainder = dividend % divisor
    return quotient, remainder

def main():
    dividend = int(input('Enter the dividend: '))
    divisor = int(input('Enter the divisor: '))
    
    if divisor == 0:
        print("Division by zero is not allowed.")
    else:
        quotient, remainder = compute_quotient_and_remainder(dividend, divisor)
        print(f'The quotient of {dividend} divided by {divisor} is: {quotient}')
        print(f'The remainder of {dividend} divided by {divisor} is: {remainder}')

if __name__ == "__main__":
    main()
