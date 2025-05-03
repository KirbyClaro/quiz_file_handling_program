#Create the Quiz program that read the output file of the Quiz Creator. 
#The user will answer the randomly selected 
#question and check if the answer is correct.

#ask user for file name
def get_filename():
    while True:
        filename = input("Enter the filename to load question").strip()
        if filename:
            if not filename.endswith(".txt"):
                filename  += ".txt"
            return filename
        print("Filename cannot be empty!")
        return
#access the file and read it
def load_questions(filename):
    questions = []
    try:
        with open(filename, "r") as file:
            content = file.read().strip().split("---\n")
            for block in content:
                if block.strip() == "":
                    continue
                lines = block.strip().split("\n")
                question_data = {}
                for line in lines:
                    if line.startswith("QUESTION:"):
                        question_data["question"] = line[len("QUESTION:"):].strip()
                    elif line.startswith("A:"):
                        question_data["A"] = line[2:].strip()
                    elif line.startswith("B:"):
                        question_data["B"] = line[2:].strip()
                    elif line.startswith("C:"):
                        question_data["C"] = line[2:].strip()
                    elif line.startswith("D:"):
                        question_data["D"] = line[2:].strip()
                    elif line.startswith("CORRECT:"):
                        question_data["correct"] = line[len("CORRECT:"):].strip()
                if question_data:
                    questions.append(question_data)
    except FileNotFoundError:
        print(f"❌ File '{filename}' not found.")
    return questions

#display the questions
def display_question(question_data):
    print("\n" + "="*50)
    print(f"Question:")
    print(question_data["question"])
    print(f"A. {question_data['A']}")
    print(f"B. {question_data['B']}")
    print(f"C. {question_data['C']}")
    print(f"D. {question_data['D']}")
    print("="*50)
    
#accept and check user answer
def get_user_answer():
    while True:
        answer = input("Your answer (A/B/C/D): ").upper().strip()
        if answer in ['A', 'B', 'C', 'D']:
            return answer
        print("Invalid input. Please enter A, B, C, or D.")

def check_answer(user_answer, correct_answer):
    """Checks if the user's answer is correct."""
    return user_answer == correct_answer

#run quiz and score
#main function with replay option

def main():
    filename = get_filename()
    questions = load_questions(filename)
    
if __name__ == "__main__":
    main()