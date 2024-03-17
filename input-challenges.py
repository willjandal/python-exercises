#Functions with input
#
#   def my_function(parameter):
#       Do this with parameter
#       Then do this
#       Finally do this
#


#takes an input from the user
inputString = input("Please enter a string: ")


#takes the input from the user and passes this input as parameter
def displayString(stringInput):
    print(f"The String entered is: {stringInput}")


#calls the function and passes the parameter inputString to the function
displayString(inputString)