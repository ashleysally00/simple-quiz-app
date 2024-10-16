import random

questions = [
    {
        "question": "What keyword is used to define a function in Python?",
        "answer": "def",
        "explanation": "In Python, we use the 'def' keyword to define a function, followed by the function name and parameters in parentheses."
    },
    {
        "question": "Which of these is NOT a valid Python data type: int, string, float, array?",
        "answer": "array",
        "explanation": "Python has int, string, and float as built-in data types, but it uses 'list' instead of 'array'. Arrays are available through the NumPy library."
    },
    {
        "question": "What symbol is used for comments in Python?",
        "answer": "#",
        "explanation": "In Python, we use the '#' symbol for single-line comments. Multi-line comments can be created using triple quotes (''' or \"\"\")."
    },
    {
        "question": "What is the correct way to create a list in Python?",
        "answer": "my_list = []",
        "explanation": "In Python, we create an empty list using square brackets []. We can also initialize a list with values: my_list = [1, 2, 3]."
    },
    {
        "question": "What does the 'len()' function do in Python?",
        "answer": "Returns the length of an object",
        "explanation": "The len() function returns the number of items in an object. It can be used with strings, lists, tuples, and other sequence or collection objects."
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
    print("Welcome to the Python Quiz App!")
    while True:
        run_quiz()
        play_again = input("\nWould you like to try another question? (yes/no): ").lower()
        if play_again != 'yes':
            print("Thank you for playing!")
            break
