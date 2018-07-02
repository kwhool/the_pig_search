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
print "he broke your spaceship and left to planet piglandius."
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
    sys.stdout.write("waiting")
    for i in range(1,duration):
        sys.stdout.write('.')
        sys.stdout.flush()
        time.sleep(1)
    print ""

# Ask question one
question1 = ask_question("what do you want to do first?", ["get your spacesuit", "go to the mechanic"])

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

wait(10)

print "there you go theres your ship!"
question4 = ask_question("what do you want to do next?", ["get your spacesuit", "go to your spaceship"])

if question4 == "1":
    print "you put your spacesuit on and went in to your spaceship"

elif question4 == "2":
    print "your spaceship exploded by accidentally dropping a bomb."
    print DEAD_PIG
    sys.exit()

print "gr bho! what was that noise! wait! I need GAS!"
question5 = ask_question("what road do need to go in to the gas station?", [" the north road","the south road"])

if question5 == "1":
    print "yay we're at the gas station!"

elif question5 == "2":
    print "you walked into a spikey bush"
    print DEAD_PIG
    sys.exit()

print "your ship has been filled with gas.yay now we can go in space!you got into your ship."
question6 = ask_question("what button should you press?", ["the red button", "the blue button"])

if question6 == "1":
    print "you pressed the selfdistruct button"
    print BACON
    sys.exit()

elif question6 == "2":
    print "you pressed the right button. you flew up and landed on the planet pig."

print "aaaaaahhh!theres pigs every where! wait i'm a pig!!?!?!?!?!?!?!?!?"
print "I am ready to battle some evil pigs. oink is very effective."
question7 = ask_question("which attack do you want to do?", ["oink", "punch"])

if question7 == "1":
    print "OOOOOOOOIIIIIIIIINNNNNNKKKKKKKK!!!!!!!!!!!!!!!!!!!"
    print "yay!all the pigs are gone!but I think we'er going to have to fight aliens later!"


elif question7 == "2":
    print "pcht!!uh oh we made the pigs mad!!!!!"
    print DEAD_PIG
    sys.exit()

print "thank goodness I got all those pigs to go away."

question8 = ask_question("which way do you want to go?", ["dark way", "the nise rainbow funland way"])

if question8 == "1":
  print "yay we went the right way because the nice things and the rainbows are pig eating evil things"

elif question8 == "2":
 print "the nice things and rainbows made you into bacon and ate you"

 print BACON
 sys.exit()
print "im saving my friends out in space im going to risk my life to save my friends"
print " da da da da da daaaa da!!!!"

print "uhhh thats a lot of craters!"

question9 = ask_question("which crater do you go in?",["dark crater", "light crater"])

if question9 == "1":
    print "puuh! you landed in the in the crater and found the lair of the octupsioslandeka. You: Yes I found what I need to get to the next planet but I need to kill the octupsioslandeka!"

elif question9 == "2":
    print "boom! the light thing in the crater was a bomb with a torch on it"
    print BACON
    sys.exit()
print "How do I bust through the door to the Octupsioslandeka's lair?"

question10 = ask_question("how do you bust the door open?",["with your hoof", "with fire"])

if question10 == "1":
    print "you kicked the door down then you walk into the lair but its pitch black."

elif question10 == "2":
    print "you got a match out and lit the door then the fire spread on you."
    print BACON
    sys.exit()
print "as you step into blackness you hear a click. you stepped on a pressure plate then lights turned on. you see two other pressure plates."

question11 = ask_question("Which pressure plate do you step on?", ["the left pressure plate", "the right pressure plate"])

if question11 == "1":
    print "arrows fired at your head"
    print DEAD_PIG
    sys.exit()
elif question11 == "2":
    print "the door in front of you opened"

print "when the door opened you saw another trap. there are two ropes over lava the left rope and the right rope."

question12 = ask_question("which rope do want to go on?",["the left rope","the right rope"])

if question12 == "1":
    print "you safely walked across it as the right rope snapped"

elif question12 == "2":
    print "you walked across the right rope but the it snapped"
    print BACON
    sys.exit()

print "You went into the next room in there is the octupsioslandeka! Octupsioslandeka:mwha ha ha ha! hello astronaut pig! come to battle me?! well your going to have a mighty rough time battling me!"

question13 = ask_question(" what attack will you use?",["punch","bite"])

if question13 == "1":
    print "you punched him but it did no damage so the he knocked in the other room in the lava and made you bacon"
    print BACON
    sys.exit()

elif question13 == "2":
    print " you bit the Octupsioslandeka it knocked him out!"

question14 = ask_question("what finishing move will you use?",["ear drum infecting oink","skull craking punch"])

if question14 == "1":
    "the oink woke him up and he threw you to the ground"
    print BACON
    sys.exit()

elif question14 == "2":
    print "the punch was so hard it flatened him so he was really light so you threw him in the lava"

print "as you walk back to your spaceship you realize that you have no gas. so you yell in space does anyone have gas!then out of no where aliens come out and attack you"

question15 = ask_question("which attack will you do",["punch the aliens and get the gas","ask nicley"])

if question15 == "1":
    print "you punched all the aliens and they all got knocked then you stole the gas and safely got away."

elif question15 == "2":
    print "you asked nicley to them but that was somthing really offensive in thier laguage so they killed you"
    print DEAD_PIG
    sys.exit()

print "that was close i knew we would encounter aliens later"
print "its time to fill the gas tank!"

question16 = ask_question("which gas tank will you fill?",["the red gas tank","the blue gas tank"])

if question16 == "1":
    print "you filled the gas tank up and pressed the button then your ship exploded"
    print DEAD_PIG
    sys.exit()

elif question16 == "2":
    print "you filled up the blue gas tank and pressed the button and went of in space"

wait(10)

print "after a while you landed on planet pigot"
print "once you got to the door you forgot which button to get out"

question17 = ask_question("which button will you press to get out",["the yellow button","the blue button"])

if question17 == "1":
    print "you pressed the yellow button and the door opened"

elif question17 == "2":
    print "you pressed the button and the ship exploded"
    print DEAD_PIG
    sys.exit()

print "woah this place looks a lot like the ocean"
print "but wait where do I go?"


question18 = ask_question("which side will you go?",["the red coral side","the yellow coral side"])

if question18 == "1":
    print "you walked over to the red coral side but it really was a monster and attacked you"
    print DEAD_PIG
    sys.exit()

elif question18 == "2":
    print "you walked over to the yellow coral side and you saw a door its the door to get farther on the planet there has to be a lever some where"

question19 = ask_question("where do you want to look for the lever",["the red coral","the yellow coral"])

if question19 == "1":
    print "you walked over to the red coral but it was a monster so it ate you"
    print DEAD_PIG
    sys.exit()

elif question19 == "2":
    print " you looked at the yellow coral closly then you saw a switch so you pulled it then the door opened"

print "you went through the door and saw more of the planet but this time it was dark and scary. you heard many sounds"

question20 = ask_question("which sound will you follow",["the happy song","the scary dark song"])

if question20 == "1":
    print "the nice and happy song was the rainbows and nice things again so they ate you"
    print BACON
    sys.exit()

elif question20 == "2":
    print "you went to the dark and scary song but then saw light.the other way was the rainbows again"

print "you went through the next door and in front of you is the door to the evil sharketeks lair. but there are two switches"

question21 = ask_question("which lever will you pull",["the green lever","the purple lever"])

if question21 == "1":
    print "you pulled the green lever and the floor below you dropped into lava with you"
    print BACON
    sys.exit()

elif question21 == "2":
    print "you pulled the purple lever and the door opened"

print "you went through the door and there were chefs!"

question22 = ask_question("what will you do",["run to the door","punch them all in the face and run to the door"])

if question22 == "1":
    print "you wernt fast enough so the chefs caught you"
    print DEAD_PIG
    sys.exit()

elif question22 == "2":
    print "you punched them all so they got knocked out and you ran to the door and got out"

print "the next room had evil sharks!"

question23 = ask_question("what will you do",["ride a shark","run to the door"])

if question23 == "1":
    print "you rode a shark but all the other sharks were still trying to get you but you jumped off at the right moment so the sharks are beating themselves up"

elif question23 == "2":
    print "you swim really slowly so the sharks caught you and ate you"
    print DEAD_PIG
    sys.exit()

print "you got to the next door and opened it. in there was more evil pigs!"

question24 = ask_question("what will you do",["run to the door","have a piggie back ride"])

if question24 == "1":
    print "you were going to run but the pigs screeched so loud you died"
    print DEAD_PIG
    sys.exit()

elif question24 == "2":
    print "you went on the evil pigs back and jumped on him and the same with the others"

print "you went through the finale door and there in his throne was sharketek. if you want to get to the next planet you need gas which you need to defeat sharketek to get"
print "so your finally here piggie. i have been waiting for this moment ever since you defeated Octupsioslandeka.so let the battle begin"

question25 = ask_question("which attack will you do",["punch","bite"])

if question25 == "1":
    print "you punched sharketek it did a third of his health"

elif question25 == "2":
    print "you bit him it did nothing so he threw you in a pool of sharks"
    print DEAD_PIG
    sys.exit()

print "ha you are as strong as i thought"

question26 = ask_question("which attack will you do",["punch","kick"])

if question26 == "1":
    print "you were going to punch him but he predited that and threw you in a lava pit"
    print BACON
    sys.exit()

elif question26 == "2":
    print "you kicked him and it did another third of his health"

print "your not going to defeat me!"

question27 = ask_question("which finishing move will you use?",["bone crunching bite","ear drum infecting oink"])

if question27 == "1":
    print "you bit him so hard he got knocked out but then the sharks started getting hungry so you fed him to the sharks"

elif question27 == "2":
    print "you oinked so loud that you earatated him so he sizzled you until you were bacon"
    print BACON
    sys.exit()

print "now wheres that gas?"

question28 = ask_question("where do you want to search for the gas?",["the shark tank","sharketeks throne"])

if question28 == "1":
    print "you walked over to the shark tank to look but you fell in"
    print DEAD_PIG
    sys.exit()

elif question28 == "2":
    print "you checked sharketeks throne there is lever there you pull the lever then behind his throne a door opens theres gallons of gas in there"

print "you carried all the gas back to the ship and filled up the ship but some aliens want to steal your ship"

question29 = ask_question("what attack will you do",["punch","kick"])

if question29 == "1":
    print "you were going to punch them but they heard from other aliens that they got punched so they dodged it and attacked you"
    print DEAD_PIG
    sys.exit()

elif question29 == "2":
    print "you kicked them in the face and ran back into the spaceship and took off"

wait(10)

print "The planet you landed on was planet pigeter."
print "Wow!This is full of civilization!"
print "A strange looking alien was coming up to you. he said welcome to alienopilous! be free to have some alien coffee stay at a alien hotel just make sure to never and I mean never say bloopa"
print "a strange bubble apeared and he got in it."

question30 = ask_question("what will you do to the alien?",["jump on the bubble and break the glass","jump on the bubble and yell let me come!"])

if question30 == "1":
    print "you broke the glass but the alien got a high teck laser and blasted you"
    print BACON
    sys.exit()

elif question30 == "2":
    print "you asked to come in and he opened the glass. both together you flew to the city."

print "wow this is a amazing view. literaly the city is a maze!"
print "I know I have to carry a map every were."

print "Suddenly a giant alien monster flew up and started attacking the ship"
