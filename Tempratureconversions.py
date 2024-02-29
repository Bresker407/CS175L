#Benedetto Aiello
#CS-175L
#Temp Convert
 
def main():
    controlLoop()
 
def convertToKelvin(Fahrenheit):
    Kelvin = ((Fahrenheit - 32) * (5/9) + 273.15)
    return Kelvin
 
def convertToCentigrade(Fahrenheit):
    Centigrade = (Fahrenheit - 32) * (5/9)
    return Centigrade
 
def doConversion(Fahrenheit):
#getFahrenheit(), get back Fahrenheit
    Kelvin = convertToKelvin(Fahrenheit)
    Centigrade = convertToCentigrade(Fahrenheit)
    print(f'Fahrenheit: {Fahrenheit} Kelvin {Kelvin} Centigrade: {Centigrade}')
    pass
 
def repeat():
    amntofcon = int(input("How many conversions would you like to do this time?"))
    for i in range (amntofcon):
        Fahrenheit = float(getFahrenheit())
        doConversion(Fahrenheit)
        pass
 
def controlLoop():
    conv = input('Do you want to do some conversions(Yes or No)? ')
    if conv == 'yes':
        repeat()
        pass
 
def getFahrenheit():
    while True:
        try:
            Fahrenheit = float(input('Enter Fahrenheit temperature (must be -50 to 130):'))
            if -50.0 <= Fahrenheit <= 130.0:
                return Fahrenheit
            else:
                print('Invalid temp')
        except ValueError:
            print("Invalid input'")
 
   
 
# Call the main function.
if __name__ == '__main__':
    main()
