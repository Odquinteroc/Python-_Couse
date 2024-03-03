'''
3. Write a program to sum a series of numbers entered by the user and print the sum. The program should also calculate and print the average of the numbers entered.  The program should first prompt the user for how many numbers are to be summed. The program should then prompt the user for each of the numbers in turn and print out a total sum after all the numbers have been entered. Hint: Use an input statement in the body of the loop.
'''
def main():
    counter = 0
    total = 0
    try:
        HowMany = eval(input('How many numbers do you want to enter? '))
    except:
        print("You must enter a number!")
        return
    while counter < HowMany:
        try:
            number = eval(input("Enter a number: "))
        except:
            print("You must enter a number!")
            return
        total += number
        counter += 1
        continue
    average = total / counter
    print("The sum is", total)
    print("The average is", average)

main()