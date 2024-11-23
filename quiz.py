import random
questions = [
    {
        "question": "What is the primary goal of exploratory data analysis (EDA)?",
        "options": ["(a) Making predictions", "(b) Summarizing data characteristics", "(c) Berlin"],
        "answer": "b"
    },
    {
        "question": "What is machine learning?",
        "options": ["(a) A technique for teaching computers to learn from data", "(b) A programming language", "(c) A hardware device"],
        "answer": "a"
    },
    {
        "question": "What is the key difference between supervised and unsupervised learning?",
        "options": ["(a) The presence of labeled data in supervised learning", "(b) The requirement for large datasets in supervised learning", "(c) The absence of algorithms in unsupervised learning"],
        "answer": "a"
    }
]
user = {}
def display_content():
  print("QUIZ APPLICATION")
def register_user():
    username = input("Enter username: ")
    if username in user:
        print("Username already exists! Try another one.")
    else:
        password = input("Enter password: ")
        user[username] = password
        print("Registration successful!")
def login():
    username = input("Enter username: ")
    password = input("Enter password: ")
    if username in user and user[username] == password:
        print("Login successful!")
        return True
    else:
        print("Invalid username or password.")
        return False
def shuffle_questions(questions):
    random.shuffle(questions)
    return questions

def attempt_quiz():
    print("\nStarting Quiz...")
    shuffled_questions = shuffle_questions(questions)
    score = 0

    for q in shuffled_questions:
        print("\n" + q["question"])
        for opt in q["options"]:
            print(opt)
        answer = input("Enter your answer (a/b/c): ").lower()
        if answer == q["answer"]:
            print("Correct!")
            score += 1
        else:
            print(f"Wrong! The correct answer was {q['answer']}.")

    print(f"\nYour final score is {score}/{len(shuffled_questions)}")

def main():
    while True:
        display_content()
        print("1. Register")
        print("2. Login")
        print("3. Exit")
        choice = input("Enter your choice: ")

        if choice == '1':
            register_user()
        elif choice == '2':
            if login():
                attempt_quiz()
        elif choice == '3':
            print("Exiting the quiz application. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
