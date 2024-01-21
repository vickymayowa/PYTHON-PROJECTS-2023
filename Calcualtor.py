import time

Welcometext = 'Welcome to My Simple Python Calculator'
print(Welcometext)

# Adding a delay of 2 seconds
time.sleep(2)

num1 = int(input('Enter your First Number: '))
num2 = int(input('Enter your Second Number: '))

print("Choose Calculation: \n"
      "1. Addition \n"
      "2. Subtraction \n"
      "3. Multiply \n"
      "4. Divide ")

choice = int(input("Enter the number for your desired calculation: "))

if choice == 1:
    Answer = num1 + num2
elif choice == 2:
    Answer = num1 - num2
elif choice == 3:
    Answer = num1 * num2
elif choice == 4:
    if num2 != 0:
        Answer = num1 / num2
    else:
        print("Error: Division by zero.")
        Answer = None
else:
    print("Invalid choice. Please choose a number between 1 and 4.")

# Adding a delay of 1 second before displaying the result
if Answer is not None:
    time.sleep(1)
    print("Result:", Answer)
