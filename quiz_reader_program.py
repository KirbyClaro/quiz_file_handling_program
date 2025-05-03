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
#display the questions
#accept and check user answer
#run quiz and score
#main function with replay option