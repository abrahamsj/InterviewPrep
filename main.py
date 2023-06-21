import random

isInTurn = True

# Define the interview questions and answers
interview_questions = {
    "Data Engineering": {
        "What is ETL?": "ETL stands for Extract, Transform, Load. It is the process of extracting data from various sources, transforming it to fit the desired format, and loading it into a target system or database.",
        "What is a data warehouse?": "A data warehouse is a large, centralized repository of data that is used to support decision-making and reporting activities.",
    },
    "Data Analysis": {
        "What is exploratory data analysis (EDA)?": "Exploratory data analysis is an approach to analyzing data sets to summarize their main characteristics, often with visual methods.",
        "What is the purpose of data cleansing?": "Data cleansing, also known as data cleaning or data scrubbing, is the process of identifying and correcting or removing errors, inconsistencies, and inaccuracies in data.",
        "What makes relational databases relational?" :"A relational database stores associated information across multiple tables; hence data from one table relate to or have relationships with data from other tables in the database."
    },
    "Software Programming": {
        "What is object-oriented programming (OOP)?": "Object-oriented programming is a programming paradigm that organizes data and behaviors into reusable structures called objects.",
        "What is a loop in programming?": "A loop is a control structure that repeats a block of code until a certain condition is met.",
    },
    "HTML": {
        "What does HTML stand for?": "HTML stands for HyperText Markup Language.",
        "What is the purpose of the <head> element in HTML?": "The <head> element is used to define the header section of an HTML document, which typically contains meta information, scripts, and stylesheets.",
    }
}

# Function to prompt the user with a question and validate the answer
def prompt_question(category):
    question = random.choice(list(interview_questions[category].keys()))
    answer = interview_questions[category][question]

    print(f"\n{category} Question:")
    print(question)

    while isInTurn:
        user_answer = input("Your Answer: ").strip()

        if user_answer == answer:
            print("Correct answer! Great job!")
            break
        else:
            print("\nIncorrect answer. The correct (more detailed) answer is shown below\n ")
            print(answer)
            isInTurn = False

# Main program loop
while True:
    print("Interview Questions Program\n")
    print("Choose a category:")
    print("1. Data Engineering")
    print("2. Data Analysis")
    print("3. Software Programming")
    print("4. HTML")
    print("0. Quit")

    choice = input("\nEnter your choice (0-4): ").strip()

    if choice == "0":
        break
    elif choice == "1":
        prompt_question("Data Engineering")
    elif choice == "2":
        prompt_question("Data Analysis")
    elif choice == "3":
        prompt_question("Software Programming")
    elif choice == "4":
        prompt_question("HTML")
    else:
        print("Invalid choice. Please try again.")
