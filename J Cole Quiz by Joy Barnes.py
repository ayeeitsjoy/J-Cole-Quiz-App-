from tkinter import *

question = {
    "What is J. Cole's real name?": ['A) Jermaine Jackson', 'B) Jermaine Cole', 'C) Jaden Smith', 'D) Jordan Calloway'],
    "In what city was J. Cole born?": ['A) Raleigh, North Carolina', 'B) Charlotte, North Carolina', 'C) Fayetteville, North Carolina', 'D) Durham, North Carolina'],
    "What was the name of J. Cole's debut studio album?": ['A) Born Sinner', 'B) Forest Hills Drive', 'C) KOD', 'D) Cole World: The Sideline Story'],
    "Which University did J. Cole attend?": ['A) Harvard University', 'B) University of North Carolina', "C) St. John's University", 'D) Duke University'],
    "Which J. Cole album features the hit song 'No Role Modelz'": ['A) 4 Your Eyez Only', 'B) Forest Hills Drive', 'C) The Off-Season', 'D) Born Sinner']
}
answer = ['B) Jermaine Cole','C) Fayetteville, North Carolina','D) Cole World: The Sideline Story',"C) St. John's University",'B) Forest Hills Drive']

user_attempt = 0 #variable to store how many questions are attempted by the user

current_question = 0 # tracks the current question index
correct = 0 # variable to store how many questions the user got correct
incorrect = 0 #variable to store how many questions the user got incorrect


#function to display the next question
def show_question(): 
    question_listed.set(list(question.keys())[current_question]) # this will show the current keys/question from the dictionary 'question'
    options = question[list(question.keys())[current_question]] # this will show the current values from the dictionary 'question'
    for i in range(4): #updates each radio button with the answer choices associated with the current question.
        radio_button[i]['text'] = options[i]
        radio_button[i]['value'] = options[i]
   # feedback_message.set('') #clear previous feedback

#function to check the answer
def check_answer():
    global current_question, user_attempt, correct, incorrect # adds variables from outside the function to inside the function
    selected_answer = user_answer.get() # compares if the stored selected answer and user answer are the same
    #if selected_answer:
        #check if answer is correct 
    if selected_answer == answer[current_question]: # if the selected answer equals the correct answer from the answer list then print message into program
        feedback_message.set('Look at you! You got it!')
        correct += 1 # stores each question that is answered correctly
    else:
        feedback_message.set('Oh nooo, are you a fan or nah??') # if the selected answer does not equal correct answer from answer list then it prints message into program
        incorrect += 1 # stores each question that is answered incorrectly 
        #attempt counter 
    user_attempt += 1 # stores each question submitted by user 
        #move to next question 
    current_question += 1 # once the submit button is selected this moves it to the next question
    if current_question <len(question): #verifies that there is another question left in an if statement otherwise a message is shown
        show_question()
    else: 
        feedback_message.set(f'Quiz Finished! You attempted {user_attempt} questions and got {correct} correct and {incorrect} wrong. Please Try Again')
    #else: 
       # feedback_message.set('Please select an answer...')
        

def reset_quiz(): # sets everything back to zero to restart the program
    global current_question, user_attempt, correct, incorrect
    current_question = 0 
    user_attempt = 0 
    user_answer.set(None)
    correct = 0
    incorrect = 0
    feedback_message.set('')
    show_question()

if __name__ == "__main__": # settings for the main window
    root = Tk()
    #setting up window screen 
    root.title("J. Cole Quiz by Joy Barnes") # title
    root.geometry("850x520") # start size of the quiz box
    root.minsize(800, 400) # user cannot resize the window any smaller than this
    
    #string var to store selected answer 
    user_answer = StringVar()
    user_answer.set(None) #default value for radio buttons
    
    #stores the selected answer
    question_listed = StringVar()

    #create feedback message variable
    feedback_message = StringVar()
    #label to display the question

    #Label is a widget in TK to display text or image 
    #root is the parent widget where the label will be placed 
    #pack.pady=21 a method used to call the label to the window and to manage its layout/spacing
    Label(root, textvariable=question_listed, font=('Arial', 15)).pack(pady=21) 

    #radio button to display the options
    radio_button = []
    for i in range(4):
        radio = Radiobutton(root, text='', variable=user_answer, font=('Arial', 12))
        radio.pack(anchor='w')
        radio_button.append(radio)

#display feedback messages 
Label(root, textvariable=feedback_message, font=('Arial', 12), fg='blue').pack(pady= 10)
#button to submit the answer and move to the next question
Button(root, text='Submit', command=check_answer).pack(pady=21)

Button(root, text='Start Over', command=reset_quiz).pack(pady=10)


show_question()
root.mainloop()