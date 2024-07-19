'''@Author: v sanjay kumar
   @Date: 2024-07-18 10:00:30
   @Last Modified by: v sanjay kumar
   @Last Modified time: 2024-07-18 10:00:30
   @Title : Flip Coin and print percentage of Heads and Tails

'''



import random
def flip_coin(num_flips):
    '''
       Description:
        Simulates flipping a coin a specified number of times and calculates the percentage of Heads and Tails.
    
    Parameters:
        num_flips (int): The number of times to flip the coin.
    
    Returns:
        float, float: The percentage of Heads and Tails respectively.
'''

    heads = 0
    tails = 0
    for _ in range(num_flips):
        if random.random() < 0.5:
            tails += 1
        else:
            heads += 1
    total = heads + tails
    return (heads/total)*100,(tails/total)*100




def main():
    num = int(input("Enter a no flips"))
    heads_percentage,tails_percentage = flip_coin(num)
    print(f"Percentage of Heads: {heads_percentage:.2f}%")
    print(f"Percentage of Tails: {tails_percentage:.2f}%")

if __name__ == "__main__":
    main()
