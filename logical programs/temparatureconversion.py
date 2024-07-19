
def temperature_conversion(temp, unit):
    """
    Converts temperature between Celsius and Fahrenheit.

    Parameters:
    temp (float): The temperature value to be converted.
    unit (str): The unit of the input temperature ('C' for Celsius, 'F' for Fahrenheit).

    Returns:
    tuple: A tuple containing:
        - float: The converted temperature.
        - str: The unit of the converted temperature ('C' or 'F').

    Raises:
    ValueError: If the unit is not 'C' or 'F'.
    """
    if unit == 'C':
        #convert celsius to fahrenheit
        converted_temp = (temp * 9/5) + 32
        return converted_temp, 'F'
    elif unit == 'F':
        #fahrenheit to Celsius
        converted_temp = (temp - 32) * 5/9
        return converted_temp, 'C'
    else:
        raise ValueError("Invalid unit. Use 'C' for Celsius or 'F' for Fahrenheit.")

def main():
    temp = float(input("Enter the temperature: "))
    unit = input("Enter the unit (C for Celsius, F for Fahrenheit): ").upper()

    try:
        converted_temp, new_unit = temperature_conversion(temp, unit)
        print(f"Converted temperature: {converted_temp:.2f}%{new_unit}")
    except ValueError as e:
        print(e)




if __name__ == "__main__":
   main()
