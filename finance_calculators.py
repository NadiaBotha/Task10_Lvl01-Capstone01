import math
# The program starts by providing the user information on what the program does.
print("-"*100)
print("Good day, this program enables you to access an investment and a home loan\
 repayment calculator.")
print("-"*100)
print()

# Provides instruction to the user on how to input information.
# Request the user to select a calculator type.
print("Choose either 'investment' or 'bond' from the menu below to proceed: ")
print()
print("investment \t- to calculate the amount of interest you'll earn on interest.")
print("bond \t\t- to calculate the amount you'll have to pay on a home loan.")
print()

# Request the input and converts the input string to lower case letters. This
# ensures that the program is not case sensitive.
print("Please type your option: ")
calc_type = input()
calc_type = calc_type.lower()
print()

# Checks if the calculator type is equal to 'investment'. If true, it requests further
# input parameters.
# The 'investment' option can be further split into 'simple' and 'compound' interest.
# Different calculations are performed, based on which option is chosen by the user.
if (calc_type == "investment"):
    deposit = float(input("Please enter the deposit amount in Rands: "))
    int_rate = float(input("Please enter the percentage interest rate: "))
    int_rate_per = (int_rate/100)
    years = float(input("Please enter the amount of years you would like to invest: "))
    interest = input("Would you like to invest with 'simple' or 'compound' interest: ")
    interest = interest.lower()

    # Checks if the interest is equal to 'simple'. If true, the calculation in this
    # block is performed and the answer is printed out to the user. 
    if (interest == "simple"):
        total = deposit*(1+int_rate_per*years)
        print()
        print("*"*90)
        print("Investing R{:.2f} at {}% {} interest for {} years, gives a total of \
 R{:.2f}.".format(deposit, int_rate, interest, years, total))
        print("*"*90)

    # Checks if the interest is equal to 'compound'. If true, the calculation in this
    # block is performed and the answer is printed out to the user.
    elif (interest == "compound"):
        total = deposit*math.pow((1+int_rate_per),years)
        print()
        print("*"*90)
        print("Investing R{:.2f} at {}% {} interest for {} years, gives a total of \
 R{:.2f}.".format(deposit, int_rate, interest, years, total))
        print("*"*90)

    # Executes this statement, if the user entered an invalid option or made a typo when
    # selecting the interest type.
    else:
        print("Please enter a valid option.")
        
# The command to print the result is placed within the individual if strings, which prevents
# the program from crashing, if a typo is made with 'simple' or 'compound'. It
# does make the program longer, but also more robust.

# Checks if the calculator type is equal to 'bond'. If true, it requests further
# input parameters, and calculates the total payable each month, which is printed
# out to the user.
elif (calc_type == "bond"):
    house_val = float(input("Please enter the value of the house in Rands: "))
    int_rate = float(input("Please enter the percentage interest rate: "))
    int_rate_per = (int_rate/100)
    month_int_rate = (int_rate_per/(12))
    months = float(input("Please enter the number of months in which you would like to pay back the bond: "))
    total = (month_int_rate*house_val)/(1-math.pow((1+month_int_rate),(-months)))
    print()
    print("*"*125)
    print("The monthly payment for a R{:.2f} bond, at an interest rate of {}%, paid back \
over {} months, is R{:.2f} per month.".format(house_val,int_rate,months,total))
    print("*"*125)

# Executes this statement if the user entered an invalid option or made a typo when selecting
# the calculator type.
else:
    print("Please enter a valid option.")
    
    



        

    

