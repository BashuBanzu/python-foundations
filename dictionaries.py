print("Welcome to the quiz!") 
name = input("What is your name? ").capitalize()
print("Hi " + name + ", let's get started with the quiz!")  
quiz = {"What is the capital of France?": "Paris", "What is 2 + 2?": "4", "Who wrote 'To Kill a Mockingbird'?": "Harper Lee", "Who is the GOAT?": "I am"    }
score = 0
for question, answer in quiz.items():
    user_answer = input(question + " ")
    if user_answer.strip().lower() == answer.strip().lower():
        print("Correct!")
        score += 1  
    else:
        print("Incorrect. The correct answer is: " + answer)        
print("Well " + name + ", your final score is: " + str(score) + "/" + str(len(quiz))) 