print("Grade Generator Project By Vicky_Dev")
test = input ("Enter the name of the test : ")
maximum_score = int(input("Enter the totall Score Of the Test : "))
your_Score = int(input("Enter your Score of the test : "))
score_percentage = (your_Score/maximum_score)*100
if score_percentage >= 90:
    print("You Scored A+")
elif score_percentage >= 80:
    print("You Scored A-")
elif score_percentage >= 70:
    print("You Scored B-")
elif score_percentage >= 60:
    print("You Scored C")
elif score_percentage >= 50:
    print("You Scored D")
else:
    print("You Scored F") 