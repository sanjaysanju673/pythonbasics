'''
   @Author: v sanjay kumar
   @Date: 2024-07-19 12:00:30
   @Last Modified by: v sanjay kumar
   @Last Modified time: 2024-07-19 12:00:30
   @Title : program to find monthlypayments

'''
def monthlypayments(year,principal,rate_intrest):
    '''Calculate the monthlypayments to return the how much pay the monthly
       payments.
    
    Parameters:
    principal (int): Principal.
    Year (int):Take the No of years.
    Rate of intrest = take the rate of intrest

    Returns:
    int: monthly Installments.
    '''
    n = year*12
    r = rate_intrest/(12*100)
    if r == 0:
       
        monthly_payment = principal / n
    else:
        
        monthly_payment = (principal * r) / (1 - (1 + r) ** -n)
    
    return monthly_payment



def main():
    principal = int(input('Enter The total principal :'))
    year = float(input('Enter the No of years :'))
    rate_of_intrest = int(input('enter the rate of intrest :'))
    g = monthlypayments(year,principal,rate_of_intrest)
    print(f'You need to pay monthly payment is:{g:.2f}')

if __name__ == '__main__':
    main()