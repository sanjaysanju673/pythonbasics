'''
   @Author: v sanjay kumar
   @Date: 2024-07-19 10:30:30
   @Last Modified by: v sanjay kumar
   @Last Modified time: 2024-07-19 10:30:30
   @Title : program vendor mechine

'''


def min_notes(change, denominations):
    """
    Calculate the minimum number of notes needed to return the change and the
    denominations of the notes to be returned by the vending machine.

    Parameters:
    change (int): The amount of change to be returned.
    denominations (list): List of available note denominations in descending order.

    Returns:
    tuple: A tuple containing:
        - int: Minimum number of notes needed to return the change.
        - list: List of note denominations that make up the change.
    """
   
    num_notes = 0
    notes_combination = []

   
    for note in denominations:
        if change == 0:
            break

       
        count = change // note

  
        if count > 0:
            num_notes += count
            notes_combination.extend([note] * count)
            change -= note * count

    return num_notes, notes_combination

def main():
    denominations = [1000, 500, 100, 50, 10, 5, 2, 1]

    change = int(input("Enter the change to be returned: "))

    min_num_notes, notes_combination = min_notes(change, denominations)

    print("Minimum number of notes needed:", min_num_notes)
    print("Notes to be returned:", notes_combination)


if __name__ == "__main__":
    main()
   
    
