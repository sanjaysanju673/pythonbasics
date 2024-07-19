'''@Author: v sanjay kumar
@Date: 2024-07-18 11:00:30
@Last Modified by: v sanjay kumar
@Last Modified time: 2024-07-18 11:00:30
@Title : Flip Coin and print percentage of Heads and Tails

'''
def harmonic(n):
    """
    Description:
        Calculates the n-th harmonic number.

    Parameters:
        n (int): The number of terms in the harmonic series.

    Returns:
        float: The n-th harmonic number.
    """
    sum = 0
    for i in range(1, n + 1):
        sum += 1 / i
    return sum

def main():
    number = int(input('Enter a number: '))
    result = harmonic(number)
    print(f'The {number}-th harmonic number is: {result}')

if __name__ == "__main__":
    main()
