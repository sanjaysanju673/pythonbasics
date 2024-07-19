'''@Author: v sanjay kumar
   @Date: 2024-07-18 12:00:30
   @Last Modified by: v sanjay kumar
   @Last Modified time: 2024-07-18 3:00:30
   @Title : program to find Vowel or Consonant

'''
def largestof3(a,b,c):
    """
    Description:
        find the largest number in the given three numbers.

    Parameters:
        a(int),b(int),c(int):take the three numbers.

    Returns:
        int: the function is returns the largest number in given three numbers
    """
    if a > b:
        if a > c:
            return a
        else:
            return c
    elif c > a:
        return c
    else:
        return b


def main():
    first_number = int(input('Enter a number:'))
    second_number = int(input('Enter a second number:'))
    third_number  = int(input('enter a third number:'))
    print('the largest of the three numbers is',largestof3(first_number,second_number,third_number))

if __name__ == "__main__":
    main()