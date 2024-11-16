# Countdown for spaceship launch
def countdown():
    for i in range(10): 
        # Think of this as counting 0 through 9 steps
        print(10 - i, end=" ")
        # Subtract i from 10 to get the countdown number

    # After the loop, print "Liftoff!"
    print("Liftoff!")

countdown()

#another method of countdown using list 

number_list: list[int]=[10,20,30,40,50,60,70,80,90,100]
def count():
    for i in number_list:
        print(i, end=" ")
    print("lift off..!")
count()