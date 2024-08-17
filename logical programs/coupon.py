'''@Author: v sanjay kumar
   @Date: 2024-07-18 12:00:30
   @Last Modified by: v sanjay kumar
   @Last Modified time: 2024-07-18 3:00:30
   @Title : program to coupon numbers

'''
import random
def generate_coupon_numbers(n):
        """
        Generates a list of N distinct coupon numbers.

        Parameters:
        - n (int): The number of distinct coupon numbers.

        Returns:
        - list: A list containing N distinct coupon numbers.
        """
        coupon_numbers = set()
        while len(coupon_numbers) < n:
            coupon_numbers.add(random.randint(1, n))
        return list(coupon_numbers)

 
def simulate_coupon_collection(n):
    """
        Simulates the process of collecting all N distinct coupon numbers randomly.

        Parameters:
        - n (int): The number of distinct coupon numbers.

        Returns:
        - int: Total random numbers needed to have all distinct numbers.
    """
    distinct_coupons = set()
    total_random_numbers = 0
    while len(distinct_coupons) < n:
        random_number = random.randint(1, n)
        total_random_numbers += 1
        distinct_coupons.add(random_number)
    return total_random_numbers



def main():
    n = int(input('Enter the number of distinct coupon numbers (N): '))

    coupon_numbers = generate_coupon_numbers(n)

    print('Distinct coupon numbers:', coupon_numbers)
    
   
    total_random_numbers = simulate_coupon_collection(n)

    print('Total random numbers needed:', total_random_numbers)

if __name__ == "__main__":
     main()
