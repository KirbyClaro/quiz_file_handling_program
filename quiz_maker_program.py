#Create a program that ask user for a question, 
#it will also ask for 4 possible answer (a,b,c,d) 
#and the correct answer. Write the collected data 
#to a text file. Ask another question until 
#the user chose to exit.

def get_answers():
    """Gets four possible answers from the user."""
    answers = []
    for label in ['A', 'B', 'C', 'D']:
        answer = input(f"Enter answer {label}: ").strip()
        answers.append(answer)
    return answers

def get_correct_answer():
    """Gets the correct answer from the user."""
    while True:
        correct = input("Enter the correct answer (A/B/C/D): ").upper().strip()
        if correct in ['A', 'B', 'C', 'D']:
            return correct
        print("Invalid input! Please enter A, B, C, or D.")

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
    print("Welcome to Quiz Creator!")
    print("Press Control + C to quit.")
    
    while True:
        question = input("\nEnter your question: ").strip()
        if question.lower() == 'quit':
            break
        
        answers = get_answers()
        correct_answer = get_correct_answer()
        
        save_to_file(question, answers, correct_answer)
        print("Question saved successfully!")
    
if __name__ == "__main__":
    main()