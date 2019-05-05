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
     \/\/     \/\/
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
print "Welcome to The Pig Search!"
print "Your name is Piggie the astronaut pig."
print "Your friends have been kidnapped by Gaint Bad Guy Pig."
print "He broke your spaceship and left to planet Piglandius."
print "You will have to get them back!"
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
question1 = ask_question("What do you want to do first?", ["Get your spacesuit", "Go to the mechanic"])

# Take the question one answer and print a different response for each option
if question1 == "1":
    print "No dummy you have to get your ship fixed first. Lets just go to the mechanic."

elif question1 == "2":
    print "Good job you picked the right one now lets go to the mechanic"

# Ask question two
question2 = ask_question("Which road do you want to go in?", ["The left road", "The right road"])

# Take the question two answer and print a different response for each option
if question2 == "1":
    print "Good job you got to the mechanic."

elif question2 == "2":
    print "You died by walking in lava"
    print DEAD_PIG
    sys.exit()

# Ask question three
print "Hi I'm the mechanic!"
question3 = ask_question("What do you want?", ["I need my ship fixed!", "I need my scooter fixed!"])

# Take the question one answer and print a different response for each option
if question3 == "1":
    print "Ok your ship will be ready in a couple hours."

elif question3 == "2":
    print "The mechanic blew up your scooter!"
    print BACON
    sys.exit()

wait(10)

print "There you go theres your ship!"
question4 = ask_question("What do you want to do next?", ["Get your spacesuit", "Go to your spaceship"])

if question4 == "1":
    print "You put your spacesuit on and went in to your spaceship"

elif question4 == "2":
    print "You died by a lack of oxygen."
    print DEAD_PIG
    sys.exit()

print "GRRRRRRRRR,bwhoo! What was that noise! Wait! I need GAS!"
question5 = ask_question("What road do need to go in to the gas station?", [" The north road","The south road"])

if question5 == "1":
    print "Yay we're at the gas station!"

elif question5 == "2":
    print "You walked into a spikey bush"
    print DEAD_PIG
    sys.exit()

print "Your ship has been filled with gas. Yay now we can go in space!You got into your ship."
question6 = ask_question("What button should you press?", ["The red button", "The blue button"])

if question6 == "1":
    print "You pressed the selfdistruct button"
    print BACON
    sys.exit()

elif question6 == "2":
    print "You pressed the right button. You flew up and landed on the planet Pig."

print "AAAAAAhHH!Theres pigs every where! Wait i'm a pig!!?!?!?!?!?!?!?!?"
print "I am ready to battle some evil pigs. Oink is very effective."
question7 = ask_question("Which attack do you want to do?", ["Oink", "Punch"])

if question7 == "1":
    print "OOOOOOOOIIIIIIIIINNNNNNKKKKKKKK!!!!!!!!!!!!!!!!!!!"
    print "Yay! All the pigs are gone!But I think we'er going to have to fight aliens later!"


elif question7 == "2":
    print  "PCHT! Uh oh we made the pigs mad!!!!!"
    print DEAD_PIG
    sys.exit()

print "Thank goodness I got all those pigs to go away."

question8 = ask_question("Which way do you want to go?", ["Dark way", "The nice rainbow funland way"])

if question8 == "1":
  print "Yay we went the right way because the nice things and the rainbows are pig eating evil things"

elif question8 == "2":
 print "The nice things and rainbows cooked you into bacon and ate you"

 print BACON
 sys.exit()
print "I'm saving my friends out in space!"
print " Da da da da da daaaa da!!!!"
print "Wait... look"

print " thats a lot of craters!"

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

question21 = ask_question("Which lever will you pull",["The green lever","The purple lever"])

if question21 == "1":
    print "You pulled the green lever and the floor below you dropped into lava with you"
    print BACON
    sys.exit()

elif question21 == "2":
    print "You pulled the purple lever and the door opened"

print "You went through the door and there were chefs!"

question22 = ask_question("What will you do",["Run to the door","Punch them all in the face and run to the door"])

if question22 == "1":
    print "You werent fast enough so the chefs caught you"
    print DEAD_PIG
    sys.exit()

elif question22 == "2":
    print "You punched them all so they got knocked out and you ran to the door and got out"

print "The next room had evil sharks!"

question23 = ask_question("What will you do",["Ride a shark","Run to the door"])

if question23 == "1":
    print "You rode a shark but all the other sharks were still trying to get you but you jumped off at the right moment so the sharks are beating themselves up"

elif question23 == "2":
    print "You swim really slowly so the sharks caught you and ate you"
    print DEAD_PIG
    sys.exit()

print "You got to the next door and opened it. In there was more evil pigs!"

question24 = ask_question("What will you do",["Run to the door","Have a piggie back ride"])

if question24 == "1":
    print "You were going to run but the pigs screeched so loud you died"
    print DEAD_PIG
    sys.exit()

elif question24 == "2":
    print "You went on the evil pigs back and jumped on him and the same with the others"

print "You went through the finale door and there in his throne was sharketek. If you want to get to the next planet you need gas which you need to defeat sharketek to get"
print "So your finally here piggie. I have been waiting for this moment ever since you defeated Octupsioslandeka. So let the battle begin"

question25 = ask_question("Which attack will you do",["Punch","Bite"])

if question25 == "1":
    print "You punched sharketek it did a third of his health"

elif question25 == "2":
    print "You bit him it did nothing so he threw you in a pool of sharks"
    print DEAD_PIG
    sys.exit()

print "Ha! You are as strong as I thought"

question26 = ask_question("Which attack will you do",["Punch","Kick"])

if question26 == "1":
    print "You were going to punch him but he predited that and threw you in a lava pit"
    print BACON
    sys.exit()

elif question26 == "2":
    print "You kicked him and it did another third of his health"

print "Your not going to defeat me!"

question27 = ask_question("Which finishing move will you use?",["Bone crunching bite","Ear drum infecting oink"])

if question27 == "1":
    print "You bit him so hard he got knocked out but then the sharks started getting hungry so you fed him to the sharks"

elif question27 == "2":
    print "You oinked so loud that you earatated him so he sizzled you until you were bacon"
    print BACON
    sys.exit()

print "Now wheres that gas?"

question28 = ask_question("Where do you want to search for the gas?",["The shark tank","Sharketeks throne"])

if question28 == "1":
    print "You walked over to the shark tank to look but you fell in"
    print DEAD_PIG
    sys.exit()

elif question28 == "2":
    print "You checked sharketeks throne there is lever there you pull the lever then behind his throne a door opens theres gallons of gas in there"

print "You carried all the gas back to the ship and filled up the ship but some aliens want to steal your ship"

question29 = ask_question("What attack will you do",["Punch","Kick"])

if question29 == "1":
    print "You were going to punch them but they heard from other aliens that they got punched so they dodged it and attacked you"
    print DEAD_PIG
    sys.exit()

elif question29 == "2":
    print "You kicked them in the face and ran back into the spaceship and took off"

wait(10)

print "The planet you landed on was planet pigeter."
print "Wow!This is full of civilization!"
print "A strange looking alien was coming up to you. he said welcome to alienopilous! be free to have some alien coffee or stay at a alien hotel just make sure to never and I mean never say bloopa"
print "A strange bubble apeared and he got in it."

question30 = ask_question("What will you do to the alien?",["Jump on the bubble and break the glass","Jump on the bubble and yell let me come!"])

if question30 == "1":
    print "You broke the glass but the alien got a high tech laser and blasted you"
    print BACON
    sys.exit()

elif question30 == "2":
    print "You asked to come in and he opened the glass. both together you flew to the city."

print "Wow this is a amazing view. Literaly the city is a maze!"
print "I know I have to carry a map every were."

print "Suddenly a giant alien monster flew up and started attacking the ship"

question31 = ask_question("How will you fight the alien?",["Grab the freeze ray gun","Tell a Yo Mama joke"])

if question31 == "1":
    print "While you were searching for the freeze ray gun the alien monster grabbed you and gave you to a chef."
    print BACON
    sys.exit()

elif question31 == "2":
        print "You told the alien monster, Yo Mama so fat, when she asked for a water bed she got a blanket over the Pacific Ocean"
        print "You made him cry and run away"

print "Thanks for saving my life back there"
print "You repilied with, Your Welcome"
print "I think is should show you who I really am, the alien pulled off a mask,"
print "IT WAS GIANT BAD GUY PIG!!!"

wait(30)

print "The next thing you know you are in a giant metal cell with evil pig guards surounding you..."

question32 = ask_question("What will you do to the guards?",["Bribe them with a cookie","Snatch the key from one of their pockets"])

if question32 == "1":
    print "You threw the cookie in a corner and they all ran there, fighting over the cookie"

elif question32 == "2":
        print "The guard caught you trying to grab the key and turned you in"
        print DEAD_PIG
        sys.exit()

print "You walked right past the guards and ran into Giant Bad Guy Pig's room, right there in the middle of the bed is Giant Bad Guy Pig with the key around his neck to your friends cell's"

question33 = ask_question("How will you get the key?",["Carefully and quietly climb on Giant Bad Guy Pig and get the key","Get the grappling hook on his desk and snatch the keys with that"])

if question33 == "1":
    print "When you approached Giant Bad Guy pig you stepped on a squeeky plank and woke him up"
    print DEAD_PIG
    sys.exit()

elif question33 == "2":
    print "The grappling hook was really quiet so you were able to grab the keys in no time"

print "you ran out of the room and found your friends cages"
print "but then after you let your friends out you hear Giant Bad Guy Pig waking up from his nap"

print "quickly you grab your friends and run to your ship but there were obstacles in the way"

question34 = ask_question("Where will you go to avoid the obstacles?",["Over the rock","Under the rock"])

if question34 == "1":
    print "You safely got over the rock"

elif question34 == "2":
    print "There was a Giant Mutated Mole under the rock that ate you"
    print BACON
    sys.exit()

print "You got over the obstacles but now there are mad aliens in your way"

question35 = ask_question("How will you deal with the aliens?",["Kick them in the face","Punch the in the stomach"])

if question35 == "1":
    print "The aliens cant get hurt in the face so they just get angrier"
    print DEAD_PIG
    sys.exit()

elif question35 == "2":\
    print "The aliens weak spot is in their stomach so they explode"

print "You look behind you, Giant Bad Guy Pig is there, shooting fire balls from his mouth"

question36 = ask_question("Where will you go to dodge the fireballs",["Left","Right"])

if question36 == "1":
    print "The fireball hit you and you got burnt to a crisp"
    print BACON
    sys.exit()

elif question36 == "2":
    print "You dodged the fire ball perfectly but it hit your ship"

print "How are we getting home now, one of your friends ask"
print "I have a plan, you say"
print "you turn around and tell you friends to hide behind a rock"
print "you approach Giant Bad Guy Pig and tell him you want to fight"

question37 = ask_question("What will be your first move?",["Fire Starting Punch","Lightning Strike Kick"])

if question37 == "1":
    print "Giant Bad Guy Pig catches your punch and flings you across the world"
    print BACON
    sys.exit()

elif question37 == "2":
    print "You Kick him right in the gut"

print "Giant Bad Guy Pig punches you so hard you go flying into your ship"
print "Almost dead, out of pure rage you throw out your most powerful move"

question38 = ask_question("What move will you finish Bad Guy Pig with?",["10.5 Magnetude Earthquake","F10 Tornado"])

if question38 == "1":
    print "The earthquake sent him underground, but from there he went right underneath you and jetted upward hitting you"
    print DEAD_PIG
    sys.exit()

elif question38 == "2":
    print "The tornado was so strong it sent him into the sun killing him"

print "You finally did it you killed Giant Bad Guy Pig"
print "You and your friends went into Bad Guy Pig's lair and saw two ships"

question39 = ask_question("Which ship will you go in?",["The Red Ship","The Purple Ship"])

if question39 == "1":
    print "You went into the ship which was really a bomb a were exploded"
    print BACON
    sys.exit()

elif question39 == "2":
    print "You got into the ship with your friends and went into space"

print "Though you are lost"

question40 = ask_question("Where do you go to go home?",["The Right","The Left"])

if question40 == "1":
    print "you got sucked into a black hole"
    print DEAD_PIG
    sys.exit()

elif question40 == "2":
    print "You finally got home..."

print "You finally got home with your friends and killed Giant Bad Guy Pig"
print "Your adventure is over, you saved your friends defeated the bad guy and got home safely"
print "Meanwhile, at the mechanics shop the mechanic is making something mysterious, something futureistic"



