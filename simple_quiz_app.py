import random

questions = [
    {
        "question": "What is the capital of France?",
        "answer": "Paris",
        "explanation": "Paris is the capital and most populous city of France, known for landmarks like the Eiffel Tower and the Louvre."
    },
    {
        "question": "What is 2 + 2?",
        "answer": "4",
        "explanation": "2 + 2 = 4 is a basic arithmetic equation. It's often used as a simple example in mathematics."
    },
    {
        "question": "Who wrote 'Romeo and Juliet'?",
        "answer": "William Shakespeare",
        "explanation": "William Shakespeare, an English playwright and poet, wrote 'Romeo and Juliet' in the late 16th century."
    }
]

def run_quiz():
    question = random.choice(questions)
    print(question["question"])
    user_answer = input("Your answer: ").strip()
    
    if user_answer.lower() == question["answer"].lower():
        print("Correct!")
    else:
        print(f"Sorry, that's incorrect. The correct answer is: {question['answer']}")
    
    print("\nExplanation:")
    print(question["explanation"])

if __name__ == "__main__":
    print("Welcome to the Simple Quiz App!")
    while True:
        run_quiz()
        play_again = input("\nWould you like to try another question? (yes/no): ").lower()
        if play_again != 'yes':
            print("Thank you for playing!")
            break
