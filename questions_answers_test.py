

#This program runs a test of knowledge

#First get the test questions
#Later this will be modified to to use file io.

def get_questions():
    #notice how the data is stored as a list of lists
    return [["What color is the sky? ", "blue"],
            ["What color is the grass? ","green"],
            ["What color is the sun? ", "yellow"]]
#This will test a single question
#It takes a single question in
#It returns True if the user typed the correct answer,
#otherwise,False

def check_question(question_and_answer):
    #extract the question and the answer from the list
    #this functon takes a list with two two elements, a question and an answer
    question=question_and_answer[0]
    answer=question_and_answer[1]
    #give the question to the user
    given_answer=input(question)
    #compare the user's answer to the tester's answer
    if answer==given_answer:
        print("Correct")
        return True
    else:
        print("Incorrect, correct was:", answer)
        return False

#this will run through all the questions

def run_test(questions):
    if len(questions)== 0:
        print(" No questions were given.")
        #the return exits the function
        return
    index=0
    right=0
    while index < len (questions):
        #check the question
        #note that this is extracting a question and answer list
        #from the list of lists.
        if check_question(questions[index]):
            right=right + 1
        #go to the next question
        index=index+1
    #notice the order of the computation, first multiply, then divide
    print("You got", right * 100/ len(questions),\
          "% right out of", len(questions))
#now let's get the questions from the get_questions function, and
#send the returned list of lists as an argument to the run_test function.

run_test(get_questions())

#expand the program with more options
questions=[["What noise does a truly advanced machine make? ", "ping"],
            ["What is the answer to life, the universe and everything? ", "42"],
            ["What is a three letter word for mouse trap? ", "cat"]]
#This will test a single question
#It takes a single question in
#It returns True if the user typed the correct answer,otherwise False

def check_question(question_and_answer):
    #extract the question and the answer from the list
    #this functon takes a list with two two elements, a question and an answer
    question=question_and_answer[0]
    answer=question_and_answer[1]
    #give the question to the user
    given_answer=input(question)
    #compare the user's answer to the testers answer
    if answer==given_answer:
        print("Correct")
        return True
    else:
        print("Incorrect, correct was:", answer)
        return False

#this will run through all the questions

def run_test(questions):
    if len(questions)== 0:
        print(" No questions were given.")
        #the return exits the function
        return
    index=0
    right=0
    while index < len (questions):
        #check the question
        #note that this is extracting a question and answer list
        #from the list of lists.
        if check_question(questions[index]):
            right=right + 1
        #go to the next question
        index=index+1
    #notice the order of the computation, first multiply, then divide
    print("You got", right * 100/ len(questions),\
          "% right out of", len(questions))


#continue with showing a list of questions and answers
def showquestions():
    q=0
    while q < len (questions):
        a=0
        print("Q:" ,questions [q][a])
        a=1
        print ("A:",questions [q][a])
        q=q+1

#now let's define the menu function
def menu():
    print("-----------")
    print("Menu:")
    print ("1 - Take the test")
    print("2 - View a list of questions and answers")
    print ("3 - View the menu")
    print("5 - Quit")
    print("-----------")

choice="3"
while choice !="5":
    if choice=="1":
        run_test(questions)
    elif choice=="2":
        showquestions()
    elif choice=="3":
        menu()
    print()
    choice=input("Choose your option from the menu above:")
    





        
    
