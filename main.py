import time
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
    time.sleep(2)
    # LOGIC FOR temperature conversion
    print("\n\tDegrees Fahrenheit:\t\t\t {}".format(temp))
    print("\tDegrees Celcius:\t\t\t {}".format(round(((temp-32)*5/9),4)))
    print("\tDegrees Kelvin:\t\t\t\t {}".format(round(((temp-32)*5/9 + 273.15),4)))

# MAIN PROGRAM
usr_data = usr_input()
temp_conversion_result = temp_conversion(usr_data[0],usr_data[1])

while True:
    condn = input("Do you want to continue using this application? (y/n): ")
    if condn.lower() == "y":
        usr_data = usr_input()
        temp_conversion_result = temp_conversion(usr_data[0],usr_data[1])
    else:
        print("\n\tTHANK YOU!")
        break