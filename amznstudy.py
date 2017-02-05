import random
import time
import os

# Store each principle and its description in a dictionary
leadership_principles = {
            "Customer Obsession": "Leaders start with the customer and work backwards. They work vigorously to earn and keep customer trust. Although leaders pay attention to competitors, they obsess over customers.",
            "Ownership": "Leaders think long term and don’t sacrifice long-term value for short-term results. They act on behalf of the entire company, beyond just their own team. They never say \“that’s not my job\".",
            "Invent and Simplify": "Leaders expect and require innovation and invention from their teams and always find ways to simplify. They are externally aware, look for new ideas from everywhere, and are not limited by “not invented here\". As we do new things, we accept that we may be misunderstood for long periods of time.",
            "Are Right, A Lot": "Leaders have strong judgment and good instincts. They seek diverse perspectives and work to disconfirm their beliefs.",
            "Learn and Be Curious": "Leaders are never done learning and always seek to improve themselves. They are curious about new possibilities and act to explore them.",
            "Hire and Develop The Best": "Leaders raise the performance bar with every hire and promotion. They recognize exceptional talent, and willingly move them throughout the organization. Leaders develop leaders and take seriously their role in coaching others.  We work on behalf of our people to invent mechanisms for development like Career Choice.",
            "Insist on the Highest Standards": "Leaders are continually raising the bar and driving their teams to deliver high quality products, services and processes. Leaders ensure that defects do not get sent down the line and that problems are fixed so they stay fixed.",
            "Think Big": "Leaders create and communicate a bold direction that inspires results. They think differently and look around corners for ways to serve customers.",
            "Bias for Action": "Many decisions and actions are reversible and do not need extensive study. We value calculated risk taking.",
            "Frugality": "Constraints breed resourcefulness, self-sufficiency and invention.  There are no extra points for growing headcount, budget size or fixed expense.",
            "Earn Trust": "Leaders listen attentively, speak candidly, and treat others respectfully. They are vocally self-critical, even when doing so is awkward or embarrassing.  Leaders do not believe their or their team’s body odor smells of perfume.  They benchmark themselves and their teams against the best.",
            "Dive Deep": "Leaders operate at all levels, stay connected to the details, audit frequently, and are skeptical when metrics and anecdote differ. No task is beneath them.",
            "Have Backbone; Disagree and Commit": "Leaders are obligated to respectfully challenge decisions when they disagree, even when doing so is uncomfortable or exhausting. Leaders have conviction and are tenacious. They do not compromise for the sake of social cohesion. Once a decision is determined, they commit wholly.",
            "Deliver Results": "Leaders focus on the key inputs for their business and deliver them with the right quality and in a timely fashion. Despite setbacks, they rise to the occasion and never settle."
}

# Initialize some variables
answer_list = ["", "", "", ""]
correct_answers = 0
incorrect_answers = 0

# Generates a question, displays it, and handles answering
def ask_question():
    # Pick a random dictionary item to be the question to ask
    question = random.choice(list(leadership_principles.keys()))

    # Store the answer to the question
    answer = leadership_principles[question]

    # Add the answer to the question to the list of possible answers displayed
    answer_list[0] = answer

    # Copy the dictionary so we can later prevent the same possible answer from being shown multiple times
    remaining_items = leadership_principles.copy()

    # Initialize some variables
    response = 0
    global correct_answers
    global incorrect_answers

    # Remove the correct answer from the list of items so it doesn't appear multiple times
    del remaining_items[question]

    # Populate the rest of the list of possible answers
    i = 1
    while i < 4:
        falsequestion = random.choice(list(remaining_items.keys()))
        answer_list[i] = remaining_items[falsequestion]

        # Remove this from the dictionary to prevent multiple of the same possible answers
        del remaining_items[falsequestion]
        i += 1
    
    # Randomize the list of possible answers so the 0 indexed answer is not always the correct answer
    random.shuffle(answer_list)
        
    # Print the quiz question and an empty line
    print(question)
    print()
    
    # Print the list of possible questions and directions to enter a response
    i = 0
    while i < 4:
        print(str(i + 1) + ". " + answer_list[i])
        i += 1
    print()
    print("Please enter a number between 1 and " + str(len(answer_list)))
    
    # Get the answer from the user
    try:
        response = int(input())
    except KeyboardInterrupt:
        exit()
    except:
        pass

    # Make sure the answer is valid
    while response < 1 or response > 4:
        print("Please enter a number between 1 and " + str(len(answer_list)))
        try: 
           response = int(input())
        except KeyboardInterrupt:
            exit()
        except:
            pass
    
    # Clear the screen and let the user know if they answered correctly or not. Increment each counter
    os.system('clear')
    if answer_list[response - 1] == answer:
        print("Correct!")
        correct_answers += 1
    else:
        print("Incorrect!")
        incorrect_answers += 1
    
    # Clear the screen after 1 second
    time.sleep(1)
    os.system('clear')

def ask_answer():
    # Pick a random dictionary item to be the question to ask
    question = random.choice(list(leadership_principles.keys()))

    # Store the answer to the question
    answer = leadership_principles[question]

    # Add the answer to the question to the list of possible answers displayed
    answer_list[0] = question

    # Copy the dictionary so we can later prevent the same possible answer from being shown multiple times
    remaining_items = leadership_principles.copy()

    # Initialize some variables
    response = 0
    global correct_answers
    global incorrect_answers

    # Remove the correct answer from the list of items so it doesn't appear multiple times
    del remaining_items[question]

    # Populate the rest of the list of possible answers
    i = 1
    while i < 4:
        falsequestion = random.choice(list(remaining_items.keys()))
        answer_list[i] = falsequestion
     
        # Remove this from the dictionary to prevent multiple of the same possible answers
        del remaining_items[falsequestion]
        i += 1

    # Randomize the list of possible answers so the 0 indexed answer is not always the correct answer
    random.shuffle(answer_list)
    
    # Print the quiz question and an empty line
    print(answer)
    print()
    
    # Print the list of possible questions and directions to enter a response
    i = 0
    while i < 4:
        print(str(i + 1) + ". " + answer_list[i])
        i += 1
    print()
    print("Please enter a number between 1 and " + str(len(answer_list)))
    
    # Get the answer from the user
    try:
        response = int(input())
    except KeyboardInterrupt:
        exit()
    except:
        pass

    # Make sure the answer is valid
    while response < 1 or response > 4:
        print("Please enter a number between 1 and " + str(len(answer_list)))
        try: 
           response = int(input())
        except KeyboardInterrupt:
            exit()
        except:
            pass
    # Clear the screen and let the user know if they answered correctly or not. Increment each counter
    os.system('clear')
    if answer_list[response - 1] == question:
        print("Correct!")
        correct_answers += 1
    else:
        print("Incorrect!")
        incorrect_answers += 1
    
    # Clear the screen after 1 second
    time.sleep(1)
    os.system('clear')

# Clear the screen on first run
os.system('clear')

# Ask multiple questions
l = 0
number_of_questions = 50
while l < number_of_questions:
    # Randomly alternate between asking about principles or their descriptions
    if random.randint(0, 1) == 0:
        ask_answer()
    else:
        ask_question()
    ask_question()
    l += 1

# Let the user know how they did
print("You answered " + str(correct_answers) + " correctly out of " + str(number_of_questions) + " total questions.")

# Exit
exit()