'''
2.  Modify the convert.py program (listed below) with a loop so that it executes 5 times before quitting. Each time through the loop, the program should get another temperature from the user and print the convertedvalue.
# convert.py
# A program to convert Celsius temps to Fahrenheit
def main():
    celsius = eval(input("What is the Celsius temperature? "))
    fahrenheit = 9/5 * celsius + 32
    print("The temperature is", fahrenheit, "degrees Fahrenheit.")
main()

'''

def main():
    counter = 0
    while counter < 5:
        try:
            celsius = eval(input("What is the Celsius temperature? "))
        except:
            print("You must enter a number!")
            return
        fahrenheit = 9/5 * celsius + 32
        print("The temperature is", fahrenheit, "degrees Fahrenheit.")
        counter += 1
main()