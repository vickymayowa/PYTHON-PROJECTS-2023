import random
passlen = int(input('Enter the length of the password : '))
Length="abcdefghijklmnopqrstuvwxyz01234567890ABCDEFGHIJKLMNOPQRSTUVWXYZ!@#$%^&*()?"
Result = "".join(random.sample(Length,passlen ))
print(Result)