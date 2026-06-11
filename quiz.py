questions = ["What is the capital of France?", "What is 2 + 2?", "Who wrote 'To Kill a Mockingbird'?", "Who is the GOAT?"]
answers = ["Paris", "4", "Harper Lee", "I am"]
score = 0
for i in range(len(questions)):
    user_answer = input(questions[i] + " ")
    if user_answer.strip().lower() == answers[i].strip().lower():
        print("Correct!")
        score += 1
    else:
        print("Incorrect. The correct answer is: " + answers[i])
print("Your final score is: " + str(score) + "/" + str(len(questions))) 