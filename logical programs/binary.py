'''
   @Author: v sanjay kumar
   @Date: 2024-07-19 1:10:30
   @Last Modified by: v sanjay kumar
   @Last Modified time: 2024-07-19 1:10:30
   @Title : program vendor mechine

'''

def decimal_to_binary(decimal_number):
    '''
    Description     
        take the decimal number and return the binary number.

    Parameters:
    number(int): take the decimal number.
    

    Returns:
    str:return the binary number in the string format.
    '''
   
    if decimal_number == 0:
        return '0'
    
    binary_number = ''
    while decimal_number > 0:
        remainder = decimal_number % 2
        binary_number = str(remainder) + binary_number
        decimal_number = decimal_number // 2
    
    return binary_number





def main():
    number = int(input("enter the decimal Number:"))
    print("the binary number of given number is:",decimal_to_binary(number))



if __name__ == "__main__":
    main()