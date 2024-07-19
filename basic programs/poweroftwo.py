'''@Author: v sanjay kumar
@Date: 2024-07-18 10:00:30
@Last Modified by: v sanjay kumar
@Last Modified time: 2024-07-18 10:00:30
@Title :compute the power of two

'''




def power_of_two(n):
    """
    Description:
        Prints the powers of two from 0 to the given number.

    Parameters:
        n (int): The highest exponent for the power of two calculations.

    Returns:
        None
    """
    for i in range(n + 1):
        print("2 ^", i, "==", 2 ** i)




def main():
    number = int(input('Enter a number: '))
    power_of_two(number).__doc__()

if __name__ == "__main__":
    main()
