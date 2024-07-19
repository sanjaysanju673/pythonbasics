'''

    @Author: v sanjay kumar
    @Date: 2024-07-18 12:00:30
    @Last Modified by: v sanjay kumar
    @Last Modified time: 2024-07-18 3:00:30
    @Title : program to find even or odd number

'''


def check_even_odd(number):
    """
    Description:
        Checks whether a given number is even or odd.

    Parameters:
        number (int): The number to check.

    Returns:
        str: 'Even' if the number is even, 'Odd' if the number is odd.
    """
    if (number/2)==number:
        return 'even'
    else:
        return 'Odd'


def main():
    number = int(input('Enter a number: '))
    result = check_even_odd(number)
    print(f"The number {number} is {result}.")


if __name__ == "__main__":
    main()
