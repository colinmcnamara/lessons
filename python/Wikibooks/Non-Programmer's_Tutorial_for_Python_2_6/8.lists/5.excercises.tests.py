#/usr/bin/python
# Expand the test.py program so it has a menu giving the option of taking the test\
#, viewing the list of questions and answers, and an option to quit. Also, add a new\
# question to ask, "What noise does a truly advanced machine make?" with the answer \
# of "ping".
def get_questions():
    return [["What color is the daytime sky on a clear day? ", "blue"],
    ["what is the answer to life, the universe and everything? ", "42"],
    ["what is a three letter word for mouse trap? ", "cat"],
    ["What noise does a truly advanced machine make? ", "ping"]]
    
def check_questions(question_and_answer):
    question = question_and_answer[0]
    answer = question_and_answer[1]
    
    given_answer = raw_input(question)
    
    if answer == given_answer:
        print "Correct"
        return True
    else:
        print "Incorrect, correct was:", answer
        return False
    
def run_test(questions):
    if len(questions) == 0:
        print "No questions were given."
        
        return
    index = 0
    right = 0
    while index < len(questions):
        
        if check_questions(questions[index]):
            right = right + 1
            
        index = index + 1
        
    print "You got", right * 100 / len(questions),\
        "% right out of ", len(questions)
        
def print_options():
    print "Options:"
    print " '1' take the test"
    print " '2' view the list of questions and answers"
    print " '3' quit the program"

def showquestions():
    q = 0
    while q < len(get_questions):
        a = 0 
        print "Q:" , questions[q][a]
        a = 1 
        print "A:" , questions[q][a]
        q = q  + 1

choice = "p"
while choice != "3":
    if choice == "1":
        run_test(get_questions())
    elif choice == "2":
         showquestions()
    elif choice != "3":
        print_options()
    choice = raw_input("option: ")
    

