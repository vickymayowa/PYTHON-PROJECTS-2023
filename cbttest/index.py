import time

# Display a welcome message
print('\nWELCOME'.center(100))

# Get the number of students taking the test
no_students = int(input('\nHow many students are taking the test: '))

# Initialize dictionaries to store student information and scores
student_info = {}
student_info2 = {}
total_scores = []

# Loop to collect information for each student
for x in range(1, no_students + 1):
    # Collect information for each student
    full_name = input(f"\nStudent {x} Full Name: ")
    mat_no = input(f"\nStudent {x} Matric No: ")
    score = 0
    
    # Store information in a dictionary
    student_info[f"Student {x}: "] = [full_name, mat_no, score]

# Loop through each student to conduct the test
for inf, stud in student_info.items():
    print(stud[0], "Your exam starts now")

    # Dictionary containing multiple-choice questions
    questions = {
        1: "a. The phrase near neighbour...",
        2: "b. The passage suggests that a blue moon is...",
        # ... (add more questions as needed)
    }

    # Loop through each question with a time limit of 30 seconds per question
    time_limit = 30
    for question_number, question_text in questions.items():
        print(f"\n{question_number}. {question_text}")
        
        # Simulate a time limit with time.sleep
        time.sleep(time_limit)
        
        # Get the user's answer
        user_answer = input('\nEnter your answer here: ')

        # Check if the answer is correct and update the score
        if user_answer.lower() == question_number:
            stud[2] += 5

    print('\nPlease wait. Result loading....'.center(100))
    print(f'Your total score is {stud[2]}/25')

    # Store the total score
    total_scores.append(stud[2])
    student_info2[stud[2]] = stud[0]

# Determine the student with the highest score
maximum = max(total_scores)
print(f"Congratulations {student_info2[maximum]}! You scored {maximum}, which is the highest score.")

# Theory Section

score_theory = 0

# List of theory questions and corresponding answers
theory_questions = [
    ("When was the 2023 presidential election conducted? ", "February 25th"),
    ("Who won the 2023 presidential election? ", "Senator Bola Ahmed Tinubu"),
    # ... (add more questions as needed)
]

# Loop through each theory question with a time limit of 30 seconds per question
for question, correct_answer in theory_questions:
    print(question)
    
    # Simulate a time limit with time.sleep
    time.sleep(time_limit)
    
    # Get the user's answer
    user_answer_theory = input()

    # Check if the answer is correct and update the score
    if user_answer_theory.strip().lower() == correct_answer.strip().lower():
        print("correct")
        score_theory += 10
    else:
        print("wrong")

print(f"\nYour total theory score is {score_theory}")

# Objective Section

score_objective = 0

# List of objective questions and corresponding answers
objective_questions = [
    ("Who was the richest man in Africa? ", "c"),
    ("Which political party won the 2023 presidential election? ", "b"),
    # ... (add more questions as needed)
]

# Loop through each objective question with a time limit of 30 seconds per question
for question, correct_answer in objective_questions:
    print(question)
    
    # Simulate a time limit with time.sleep
    time.sleep(time_limit)
    
    # Get the user's answer
    user_answer_objective = input()

    # Check if the answer is correct and update the score
    if user_answer_objective.strip().lower() == correct_answer.strip().lower():
        score_objective += 10

print(f"\nYour total objective score is {score_objective}")

# Display the overall total score
total_score_all_sections = score + score_theory + score_objective
print(f"\nYour overall total score is {total_score_all_sections}")