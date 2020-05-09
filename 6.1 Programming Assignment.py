#File: 6.1 Programming Assignment
#Name: David Suffolk
#Date: April 19th, 2019
#Course: DSC510-T303 Introduction to Programming (2195-1)
#Assignment Number: 6.1
#Purpose: Gather temperature inputs, validate their value, return largest, smallest, and total entries.

#Create an empty list called temperatures
temperatures = []

#Error Handling: function will test that input is a number. If any letters are added, the program will close
def testTemperature(x):
    try:
        i = float(x)
        newTemp = i/1 #dividing by one to validate input is a number
    except:
        print("Invalid Entry. Please start program again.")
        quit() #Program will end if anything other than a number is entered

#Add and check: Function that adds validated input to list and checks length of list
#If temperatures list has 5 values, the loop will end
def addTemperature(d):
    temperatures.append(int(d))
    for t in temperatures:
        if len(temperatures) == 5:
            break
        else: #If there are less than 5 values, a new input will be asked for and the functions will run again
            inp = input("Please enter a temperature\n")
            testTemperature(inp)
            addTemperature(inp)

#Beginning of program for User. Instructions for 5 temperatures and prompt for first input.
print("The program five temperatures. Please input one at a time.\n")
inp = input("Please enter a temperature\n")

#calls the function that tests the input
testTemperature(inp)

#calls the function that adds to list and verifies list length
addTemperature(inp)

#converts length of full list to string for output
counter = str(len(temperatures))

#sorts values into numerical order
temperatures.sort()

#OUTPUT TEXT
print("Thank you! Here are your results.")
print("Largest Temperature: " + str(temperatures[-1])) #calls last index in sorted list
print("Smallest Temperature: " + str(temperatures[0])) #calls first index in sorted list
print("Total Temperatures Entered: " + counter) #uses the counter variable to output number of values
print(temperatures)
