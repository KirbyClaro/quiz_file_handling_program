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

def main():
    print("Welcome to Quiz Creator!")
    print("Press Control + C to quit.")
    
    question = input("Enter your question: ").strip()
    answers = get_answers()
    correct_answer = get_correct_answer()
    
if __name__ == "__main__":
    main()