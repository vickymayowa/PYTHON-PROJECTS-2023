Welcometext = 'My name is Vicky Dev First Python Work'
print(Welcometext)
num1 = int(input('Enter your First Number : '))
num2 = int(input('Enter your Second Number : '))

print("Choose Calculation : \n",
        "Addition \n",
        "Subtraction \n",
        "Multiply \n",
        "Divide "    
    )

calc = input()
if calc == "Addition" :
    Answer = num1 + num2
elif calc == "Subtraction" :
    Answer = num1 - num2
elif calc == "Multiply" :
    Answer = num1 * num2
elif calc == "Divide" :
    Answer = num1 / num2 
print(Answer)