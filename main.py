def main():
    """
    ##################################################
    # Comlete your code here
    Use the same variables: celcius fahrenheit 
    ##################################################
    """
    celcius = float(input("Enter the temperature in celcius: "))
    fahrenheit = (celcius * (9/5)) + 32
    print(f"Fahrenheit: {fahrenheit:.2f}")
    """
    ########################################
    # Do not delete the return statement
    ########################################
    """
    return celcius, fahrenheit


if __name__ == '__main__':
    main()
