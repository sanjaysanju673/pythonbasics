

def fib(n):
    """
    Generates and prints the Fibonacci sequence up to the nth term.

    Parameters:
    - n (int): The number of terms in the Fibonacci sequence to generate.

    Returns:
    - None
    """
    a, b = 0, 1 
    print(a, b, end=' ') 

    i = 2 
    while i <= n:
        a, b = b, a + b  
        print(b, end=' ')  
        i += 1  



def main():
    n = int(input('Enter a number: '))
    print('fibonoci serice of the given number range')
    fib(n)


if __name__ == "__main__" :
    main() 


