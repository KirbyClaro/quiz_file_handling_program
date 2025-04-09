#Create a program that ask user for a question, 
#it will also ask for 4 possible answer (a,b,c,d) 
#and the correct answer. Write the collected data 
#to a text file. Ask another question until 
#the user chose to exit.

def get_user_question():
    return input("Enter your question: ").strip()
def main():
    print("Welcome to Quiz Creator!")
    print("Press Control + C to quit.")
    question = get_user_question()
    print(f"You entered: {question}")

if __name__ == "__main__":
    main()