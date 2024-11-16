# Write a program that asks a user to enter a number. Your program will then double that number and print out the result.
#  It will repeat that process until the value is 100 or greater.
#userinput with type casting
def main():
    user_input= int(input("Enter Your number."))
    #using while loop  
    while user_input <= 100:
        user_input =2 * user_input
        print(user_input, end=" ")
main()

