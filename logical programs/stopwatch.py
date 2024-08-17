'''
   @Author: v sanjay kumar
   @Date: 2024-07-18 12:00:30
   @Last Modified by: v sanjay kumar
   @Last Modified time: 2024-07-18 3:00:30
   @Title : program to coupon numbers

'''
from datetime import datetime


def stopwatch(start_time,end_time):
    """
        Descripion
         -compute the Elapsed time.

        Parameters:
        - start_time(int),end_time(int): taking the  start_time,End_time

        Returns:
        - int:Elapsed Time.
    """
    return end_time - start_time


def main():
    start_time_str = input("Enter a start Time in HH:MM:SS :")
    end_time_str = input("Enter a End time in HH:MM:SS :")

    start_time = datetime.strptime(start_time_str,'%H:%M:%S')
    end_time   = datetime.strptime(end_time_str,'%H:%M:%S')
    print(f"The Elapsed time is : { stopwatch(start_time,end_time)}")


if __name__ == "__main__":
    main()
