'''@Author: v sanjay kumar
@Date: 2024-07-18 12:00:30
@Last Modified by: v sanjay kumar
@Last Modified time: 2024-07-18 3:00:30
@Title : program to find Vowel or Consonant

'''


def check_vowel_or_consonant(char):
    """
    Checks whether a given character is a vowel or consonant.

    Parameters:
        char (str): The character to check.

    Returns:
        str: Message indicating whether the character is a vowel or consonant.
             Returns an error message if the input is not a single alphabet character.
    """
    if len(char) == 1 and char.isalpha():
        char_lower = char.lower()
        if char_lower in 'aeiou':
            return f'{char} is a vowel'
        else:
            return f'{char} is a consonant'
    else:
        return "Please enter a single alphabet character."

def main():
    alphabet = input("Enter an alphabet: ")
    result = check_vowel_or_consonant(alphabet)
    print(result)

if __name__ == "__main__":
    main()
