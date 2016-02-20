import sys
import time

BACON = '''
          __      _.._
       .-'__`-._.'.--.'.__.,
      /--'  '-._.'    '-._./
     /__.--._.--._.'``-.__/
     '._.-'-._.-._.-''-..'
'''

DEAD_PIG = '''
    ,__         __,
     \)`\_..._/`(/
     .`  _   _  `.
    /    X\ /X   \\
    |    .-.-.    |  _
    |   /() ()\   | (,`)
   / \  '-----'  / \ .'
  |   '-..___..-'   |
  |                 |
  |                 |
  ;                 ;
   \      / \      /
    \-..-/'-'\-..-/
 jgs \/\/     \/\/
'''

print '''
  _______ _            _____ _          _____                     _     _
 |__   __| |          |  __ (_)        / ____|                   | |   | |
    | |  | |__   ___  | |__) |  __ _  | (___   ___  __ _ _ __ ___| |__ | |
    | |  | '_ \ / _ \ |  ___/ |/ _` |  \___ \ / _ \/ _` | '__/ __| '_ \| |
    | |  | | | |  __/ | |   | | (_| |  ____) |  __/ (_| | | | (__| | | |_|
    |_|  |_| |_|\___| |_|   |_|\__, | |_____/ \___|\__,_|_|  \___|_| |_(_)
                                __/ |
                               |___/
'''
print "welcome to the pig search!"
print "your name is piggie the astronaut pig."
print "your friends have been kidnapped by gaint bad guy pig."
print "he broke your ship and left to planet piglandius."
print "you will have to get them back!"
print ""

def ask_question(question, options):
    print question
    for number, option in enumerate(options):
        number = str(number + 1)
        print number + ") " + option
    answer = raw_input("choose: ")
    print "~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~\n"
    return answer

def wait(duration):
    print "waiting..."
    for i in range(1,duration):
        sys.stdout.write('*')
        sys.stdout.flush()
        time.sleep(1)
    print ""

# Ask question one
question1 = ask_question("what do you want to do first?", ["get your space suit", "go to the mechanic"])

# Take the question one answer and print a different response for each option
if question1 == "1":
    print "no dummy you have to get your ship fixed first. Lets just go to the mechanic."

elif question1 == "2":
    print "good job you picked the right one now lets go to the mechanic"

# Ask question two
question2 = ask_question("which road do you want to go in?", ["the left road", "the right road"])

# Take the question two answer and print a different response for each option
if question2 == "1":
    print "good job you got to the mechanic."

elif question2 == "2":
    print "you died by walking in lava"
    print DEAD_PIG
    sys.exit()

# Ask question three
print "hi I'm the mechanic!"
question3 = ask_question("what do you want?", ["I need my ship fixed!", "I need my scooter fixed!"])

# Take the question one answer and print a different response for each option
if question3 == "1":
    print "ok your ship will be ready in a couple hours."

elif question3 == "2":
    print "the mechanic blew up your scooter!"
    print BACON
    sys.exit()

wait(15)

print "there you go theres your ship!"
