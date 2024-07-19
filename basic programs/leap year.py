'''@Author: v sanjay kumar
@Date: 2024-07-18 10:20:30
@Last Modified by: v sanjay kumar
@Last Modified time: 2024-07-18 10:30:30
@Title : Flip Coin and print percentage of Heads and Tails

'''
def check_leap_year(year):

    """
    Description:
        Checks if a given year is a leap year and ensures the year has four digits.

    Parameters:
        year (int): The year to check.

    Returns:
        str: A message indicating whether the year is a leap year or not.
    """

    if len(str(year)) < 4:
        return "The year must have four digits"
    elif (year % 4 == 0 and year % 100 != 0) or year % 400 == 0:
        return "Given year is a leap year"
    else:
        return "Given year is not a leap year"

def main():
    year = int(input("Enter a year: "))
    result = check_leap_year(year)
    print(result)

if __name__ == "__main__":
    main()
