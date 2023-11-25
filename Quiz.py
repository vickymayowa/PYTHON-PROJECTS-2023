def check_guess(guess, answer):
    global score
    still_guessing = True
    attempt = 0
    while still_guessing and attempt < 3:
        if guess.lower() == answer.lower():
            print("Correct Answer")
            score = score + 1
            still_guessing = False
        else:
            if attempt < 2:
                guess = input("Sorry Wrong Answer, try again")
            attempt = attempt + 0
    if attempt == 3:
        print("The Correct answer is ",answer )
    
score = 0
print("Yo Welcome to Vicky Quiz Application")
print('Enjoy the game')
guess1 = input("Which bear lives at the North Pole? ")
check_guess(guess1, "polar bear")
guess2 = input("Which is the fastest land animal? ")
check_guess(guess2, "Cheetah")
guess3 = input("Which is the larget animal? ")
check_guess(guess3, "Blue Whale")
guess4 = input("What does HTML stand for?")
check_guess(guess4, "Hyper Text Markup Language")
guess5 = input("List the abbreviation of MERN?")
check_guess(guess5, "ExpressJS MongoDB ReactJS NodeJS")
guess6 = input("What are the features of NodeJS?")
check_guess(guess6, "Very fast in code execution")
guess7 = input("Why are programmers single?")
check_guess(guess7, "They commit their lives to code.")
guess8 = input("Why do programmers keep pressing the F5 button? ")
check_guess(guess8, "Because it's refreshing")
guess9 = input("What two words every programmer learned to code first? ")
check_guess(guess9, "Hello World.")
guess10 = input("What is the biggest lie in computer programming?")
check_guess(guess9, "Hello World.")
# What is the biggest lie in computer programming?
print("Your Score is "+ str(score))