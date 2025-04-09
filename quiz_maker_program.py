#Create a program that ask user for a question, 
#it will also ask for 4 possible answer (a,b,c,d) 
#and the correct answer. Write the collected data 
#to a text file. Ask another question until 
#the user chose to exit.

def get_question():
    """Gets a question from the user with validation."""
    while True:
        question = input("Enter your question: ").strip()
        if question:
            return question
        print("Question cannot be empty!")
        
def get_answers():
    """Gets four possible answers from the user."""
    answers = []
    for label in ['A', 'B', 'C', 'D']:
        while True:
            answer = input(f"Enter answer {label}: ").strip()
            if answer:
                answers.append(answer)
                break
            print(f"Answer {label} cannot be empty!")
    return answers

def save_to_file(question, answers, correct_answer):
    """Saves the question and answers to a file."""
    with open("quiz_questions.txt", "a") as file:
        file.write(f"QUESTION:{question}\n")
        file.write(f"A:{answers[0]}\n")
        file.write(f"B:{answers[1]}\n")
        file.write(f"C:{answers[2]}\n")
        file.write(f"D:{answers[3]}\n")
        file.write(f"CORRECT:{correct_answer}\n")
        file.write("---\n")

def main():
    print("~~~~~~~~Welcome to Quiz Creator!~~~~~~~~")
    print("Press Control + C to quit.")
    
    while True:
        data = {
            "question": get_question(),
            "answers": get_answers(),
            "coorect":
        }
        
        save_to_file(data["answers"], data["question"])
        print("Question saved successfully!")

        cont = input("\nWould you like to add another question? (yes/no): ").lower()
        if cont != 'yes':
            break
        
        print("\nThank you for using Quiz Creator!")
        print("\n I hoped you liked it! :D")
    
if __name__ == "__main__":
    main()