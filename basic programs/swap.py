'''@Author: v sanjay kumar
@Date: 2024-07-18 12:00:30
@Last Modified by: v sanjay kumar
@Last Modified time: 2024-07-18 3:00:30
@Title : Flip Coin and print percentage of Heads and Tails

'''
def swap(a,b):
    '''
    Description:
       Swaping two Numbers.
    
    Parameters:
         a(int),b(int):first number , second number.
    
    Returns:
        int, int: return the after swaping numbers.
'''
    a = a+b
    b = a-b
    a = a-b
    return a,b



def main():
    first_number = int(input('Enter a number'))
    second_number = int(input('Enter a second number'))
    print('before Swaping',first_number,second_number)
    print('after swaping' ,swap(first_number,second_number) )


if __name__ == "__main__":
    main()