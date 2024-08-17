'''
   @Author: v sanjay kumar
   @Date: 2024-07-19 10:00:30
   @Last Modified by: v sanjay kumar
   @Last Modified time: 2024-07-19 10:00:30
   @Title : program to siqure root

'''
import math

def sqrt(c):
   
   ''' Descripion
         -compute the squre root of the given number.

        Parameters:
        - number(int): taking the  start_time,End_time

        Returns:
        - int:squre root of the number.
    '''
   t = c
   epsilon = 1e-15
   while abs(t - c/t) > epsilon*t:
      t =(t+c/t)/2.0
    
   return t
    
   
def main():
   number = int(input("enter a number"))
   print(f"the squreroot of the number is:{sqrt(number):.2f}")

if __name__ == "__main__":
   main()

    
   