inp = input( 'Enter a fahrenheit temperature: ') # the function input is a keyword reserved for request to the user 

try: 
    fahr = float(inp)
    cel = (fahr - 32) * 5 / 9
    print( f'The temperature in Celsius is {cel:.2f}')
except:
    print( 'Please enter a valid temperature')
    