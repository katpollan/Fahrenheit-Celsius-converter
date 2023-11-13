import random #random module for error code generation

#dictonary of random error codes for the 'else' statements
error_codes = ['Please try again','I do not understand, can you try again?','Please check your input and try again','That was not clear, can you try again?',]

user_answer = input('Yes/No')
user_check = input('Would you like to continue?(Yes/No)')


#opening of the program
print('Hello!')
print('Would you like to convert a temperature?')
print(user_answer)

#calculator program if someone inputs yes
if user_answer == 'Yes' or 'yes' or 'YES': #putting in variances to account for user error
    
    #finding out if converting from f to c or c to f
    print('Would you like to convert to Fahrenheit or Celsius?' )
    temp_type =input("Fahrenheit/Celsius")

    #fahrenheit calculator
    if temp_type == 'Fahrenheit' or 'fahrenheit':
        print('What is the temperature in Fahrenheit?')
        print('Numbers only')
        
        #gathering fahrenheit temp from user
        user_fah_temp = input()
        #cast to int
        fah_temp = int(user_fah_temp)
        #conversion to celsius
        calc_cel_temp = ((fah_temp-32)*5/9)

        print(user_fah_temp,"in celsius is",calc_cel_temp)
        print(user_check)

    else:
        print(random.choice(error_codes))
    
    #celsius calculator
    if temp_type == 'Celsius' or 'celsius':
        print('What is the temperature in Celsius?')
        print('Numbers only')
        
        #gathering fahrenheit temp from user
        user_cel_temp = input()
        #cast to int
        cel_temp = int(user_cel_temp)
        #conversion to celsius
        calc_fah_temp = ((cel_temp * 5/9) + 32)

        print(user_cel_temp,"in celsius is",calc_fah_temp)
        print(user_check)
        
    else:
        print(random.choice(error_codes))
    
    #if user puts in something other then fahreinheit or celsius
else:
    print (random.choice(error_codes))


#if user inputs no (for some reason)
if user_answer == 'No' or 'NO' or 'no': #putting in variances to account for user error
    print ('Goodbye!')

#if user inputs something other then yes or no
else:
    print (random.choice(error_codes))