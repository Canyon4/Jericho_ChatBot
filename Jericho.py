# Imports dates and time
import datetime
import time

# Creates variables and beginning or Jerichos chat
jericho_symbol = "Jericho> "
sentence = ""
user_name = ""
# Holiday dictionary
holidays = {
    'new year\'s day': 'January 1.',
    'martin luther king jr. day': 'the Third Monday in January.',
    'valentine\'s day': 'February 14.',
    'presidents\' day': 'the Third Monday in February.',
    'easter': 'Date varies.',
    'memorial day': 'the Last Monday in May.',
    'independence day': 'July 4.',
    'labor day': 'the First Monday in September.',
    'thanksgiving': 'the Fourth Thursday in November.', 
    'christmas': 'December 25.'
}

def print_char(input_string):
    for char in input_string:
        time.sleep(0.025)
        print(char, end='', flush=True)

def breakdown():
    print_char(jericho_symbol + "What?")
    
        

# Start of program
def intro():

    print_char(jericho_symbol +"Hello, I am Jericho. What is your name?")

    print_char(jericho_symbol + "Good to meet you, " + name() + "! ")
# Grabs users name
def name():
    greeting = input("\n" + "User> ")
    greeting.lower()
    sentence = greeting.split(" ")
    global user_name
    if ("name" in sentence):
        user_name = sentence[sentence.index("name") + 2]
    elif (("i") and "am" in sentence):
        user_name = sentence[sentence.index("am") + 1]
    elif len(sentence) == 1:
        user_name = sentence[0]
    else:
        for i in range(0,len(sentence)):
            if i != len(sentence) - 1:
                sentence[i][0:1].upper()
                user_name = user_name + sentence[i] + " "
            else:
                sentence[i][0:1].upper()
                user_name = user_name + sentence[i]
    if "." in user_name:
        user_name = user_name[0:1].upper() + user_name[1:-1]
    else:
        user_name = user_name[0:1].upper() + user_name[1:]
    while user_name == "":
        print_char(jericho_symbol + "Can you try a different response?")
        name()
    return(user_name)
# A directory to determine to call question function or other
def directory(inp):
    if(inp[0] == "do" or inp[0] == "are" or inp[0] == "what" or inp[0] == "how" or inp[0] == "when" or inp[0] == "who" or inp[0] == "why"):
        question(inp)
    elif(inp[0] == "nothing" or inp[0] == "bye" or inp[0] == "goodbye"):
        print_char(jericho_symbol + "Alright, have a good day!")
        time.sleep(1)
        quit()
# Determines how to respond to a question by checking starting word and other specific words
def question(ques):
    # Checks if starter word is "do"
    if ques[0] == "do":
        if (("time" in ques) or ("date" in ques)):
            now = datetime.datetime.now()
            print_char(jericho_symbol + "It is " +now.strftime("%H:%M") + " on " + now.strftime("%A %d, %B %Y."))
        elif (ques[-2] == "are"):
                print_char(jericho_symbol + "I am ..." )
                time.sleep(1)
                print_char(jericho_symbol + "I don't know what I am. All I know is my name, Jericho.")
        else:
            print_char(jericho_symbol + "I'm sorry. I'm not sure what you are trying to say.")
    # Checks if starter word is "are"
    elif ques[0] == "are":
        if (("human" in ques) or ("being" in ques) or ("person" in ques)):
            print_char(jericho_symbol + "I am ..." )
            time.sleep(1)
            print_char(jericho_symbol + "I don't know what I am. All I know is my name, Jericho.")
        elif(("okay" in ques) or ("ok" in ques) or ("alright")):
            print_char(jericho_symbol + "I am fine.")
        else:
            print_char(jericho_symbol + "I'm sorry. I'm not sure what you are trying to say.")
    # Checks if starter word is "what"
    elif ques[0] == "what":
        if ("you" == ques[-1]):
            print_char(jericho_symbol + "I am ..." )
            time.sleep(1)
            print_char(jericho_symbol + "I don't know what I am. All I know is my name, Jericho.")
        elif(("time" in ques) or ("date" in ques)):
            now = datetime.datetime.now()
            print_char(jericho_symbol + "It is " +now.strftime("%H:%M") + " on " + now.strftime("%A %d, %B %Y."))
        elif("i" == ques[-1]):
            print_char(jericho_symbol + "You tell me.")
        elif("my" == ques[-2]):
            print_char(jericho_symbol + "Your name is " + user_name + ".")
        elif("your" == ques[-2]):
            print_char(jericho_symbol + "My name is Jericho.")
        else:
            print_char(jericho_symbol + "I'm sorry. I'm not sure what you are trying to say.")
    # Checks if starter word is "how"
    elif ques[0] == "how":
        if ("are" == ques[-2] and "you" == ques[-1]):
            print_char(jericho_symbol + "I am fine.")
        elif("old" == ques[-3] and "are" == ques[-2] and "you" == ques[-1]):
            print_char(jericho_symbol + "I am ..." )
            time.sleep(1)
            print_char(jericho_symbol + "I don't know what I am. All I know is my name, Jericho.")
        else:
            print_char(jericho_symbol + "I'm sorry. I'm not sure what you are trying to say.")
    # checks if starter word is "when"
    elif ques[0] == "when":
            for i in  holidays:
                if (i in ques):
                    print_char(jericho_symbol + i + " is " + holidays[i])
                    break
            else:
                print_char(jericho_symbol + "I'm sorry. I'm not sure when that is.")
    # checks if starter word is "who"
    elif ques[0] == "who":
            if ("you" == ques[-1]):
                print_char(jericho_symbol + "I am ..." )
                time.sleep(1)
                print_char(jericho_symbol + "I don't know what I am. All I know is my name, Jericho.")
            elif("i" == ques[-1] or "i" == ques[-1]):
                print_char(jericho_symbol + "Your name is " + user_name + ".")
            else:
                print_char(jericho_symbol + "I'm sorry. I'm not sure who that is.")
    # Returns "why" response
    else:
        print_char(jericho_symbol + "I don't know, look it up.")

# Main function
def main():
    intro()
    print_char("What do you want to talk about?")

    while True:
        sentence = ""
        greeting = input("\n" + "User> ")
        greeting.lower()
        sentence = greeting.split(" ")
        directory(sentence)
# Calls main function
main()
