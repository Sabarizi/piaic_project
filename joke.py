#joke bot 
PROMPT:str="What do you want?"
JOKE:str="Why do programmers prefer dark mode?Because light attracts bugs! 😄"

#define function    
def joke_bot ():
    #get user input
    user_input =input(PROMPT)
    print(user_input)
    #  if else statements .lower is used for user can type joke captil or small letter
    if user_input.lower() == "joke":
        print(JOKE)
    else:
        print("sorry, i only tells jokes")

joke_bot()