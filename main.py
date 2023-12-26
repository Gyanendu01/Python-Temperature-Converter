print("\n\tWELCOME TO THE TEMPERATURE CONVERSION APPLICATION")

def usr_input():
    try:
    # Get the user-name and temperature value
        usr_name = input("\n\tEnter your username: ")
        temp = float(input("\n\tWhat is the given temperature in degrees Fahrenheit: "))
    except ValueError:
        print("\n\tInvalid temperature values")
    return usr_name, temp

def temp_conversion(name,temp):
    print("\n\tHello {}! Temperature Conversion table is as below".format(name))
    
    # LOGIC FOR temperature conversion
    print("\n\tDegrees Fahrenheit:\t\t\t {}".format(temp))
    print("\tDegrees Celcius:\t\t\t {}".format((temp-32)*5/9))
    print("\tDegrees Kelvin:\t\t\t\t {}".format(((temp-32)*5/9)+273.15))

# MAIN PROGRAM
usr_data = usr_input()
temp_conversion = temp_conversion(usr_data[0],usr_data[1])