import random
from sys import exit

yourlife = 30
remedynumber = 0
attachtype = "off"
hardness = 40


def sword(power):
	if power == "on":
		sword_attack = random.randrange(5, 10)
	else:
		sword_attack = random.randrange(1, 5)
	return sword_attack

def remedy(number_of_remedy):
	if number_of_remedy == 0:
		return 0
	else:	
		increase_life = random.randrange(15, 16)
		return increase_life

def game_over():
	print "Game Over...\n"
	exit(0)

def boss():
	boss_attack = random.randrange(1, 10)
	return boss_attack

def special_boss_event():
	event = random.randrange(1, 5)
	if event == 1:
		print "Evil Peggy is angry! She poops on your face."
		return 10
	elif event == 2:
		print "Evil Peggy uses her CHANEL Attack. Your life remain only 1!"
		return 1
	else:
		return 3
	

def final_stage(*args):
	boss_life, your_life, power, number_of_remedy = args
	print "\nThe world is endangered because the Boss 'Evil Peggy' is attacking the world."
	print "You are the only hope! Raise your sword and fight!\n"

	while boss_life > 0:
		print "\t\tchoose your action."
		print "\t\t1: use sword"
		print "\t\t2: use remedy"
		print "\t\t3: flee "
	
		choice = raw_input('> ')
	
		if choice == "1":
			attack = sword(power)
			boss_life = boss_life - attack
		
			if boss_life > 0:
				print "\nYou make %d damage" % attack 
			else:
				print "The boss life is 0!"
				break
			
		elif choice == "2":
			number_of_remedy = number_of_remedy - 1
			if number_of_remedy > 0:
				your_life += remedy(number_of_remedy)
				print "Your are cured. Your life is %d now." % your_life
				print "You have %d remedy left." % number_of_remedy
				
			else:
				print "\nYou have no more remedy!"
	
		elif choice == "call the holy dog":
			print "\nThe dog comes out and barks~~~~Awoo~~~~~~~~~~~~~~~~~~~."
			print "you feel much more powerful now."
			print "Your attack power has been increased!"
			power = "on"
		
		elif choice == "4":
			print "The world is doomed!"
			game_over()
		
		else:
			print "your choice is not valid, please choose again."
			continue
	
		boss_attack = boss()
		your_life = your_life - boss_attack
		print "You are hurted by the boss. Your life decrease %d." % boss_attack
		print "\nYour life is %d" % your_life
		print "Evil Peggy has %d\n" % boss_life
	
		if your_life <= 0: 
			print "You are defeated!  The world is doomed!"
			game_over()
		else:
			event = special_boss_event()
		
			if event == 10 or event == 1:
				your_life = event
				print "You life is now %d\n" % your_life
			else:
				print "Evil Peggy: I will rule the world.\n"
		
	print "You save the world!"


def start2():
	print "\n\t\tThere are two ways in front of you."
	print "\t\tLeft or Right.\n\t\tYour decision?"
	decision = raw_input('> ')
	
	if decision == "Left":
		holy_dog2()
	elif decision == "Right":
		final_stage(hardness, yourlife, attachtype, remedynumber)
	else:
		print "I do not understand what you are saying?"
		start2()


def start():
	print "\n\t\tThere are two ways in front of you."
	print "\t\tLeft or Right.\n\t\tYour decision?"
	decision = raw_input('> ')
	
	if decision == "Left":
		holy_dog()
	elif decision == "Right":
		final_stage(hardness, yourlife, attachtype, remedynumber)
	else:
		print "I do not understand what you are saying?"
		start()
	
def holy_dog():
	holy_array = ['kichen', 'smoke', 'dog food', 'hello kitty', 'ironman', 'spiderman']
	print "\t\tIn front of you, there is a dog. The dog, shining with white beans, is the holy dog."
	print "\t\tWhat would you do?", "talk to him?", " kick him?", " or say: he is so cute!"
	you_say = raw_input('> ')
	
	if you_say == "talk to him":
		print "He says: to get the power of the holy dog\n You have to pass two holy challenges created by me"
		print "The first challenges. Which is the power source of the holy dog?"
		print "\n"
		print holy_array
		first_one = raw_input('> ')
	
		if first_one == "dog food":
			print "correct!"
		else:
			print "You do not understand the great mind of the holy dog....>.<"
			start()
	
		print "How many man are there in the list?"
		second_one = raw_input('> ')
			
		if second_one == "2":
			print "correct!"
			print "You are the one!!!!!!!"
			print "Here are the five remedys"
			print "You learn the ancient magic spell 'call the holy dog'!"
			print "When you feel weak.... Remeber to use the spell!"
			pass
		else:
			print "You do not understand the great mind of the holy dog....>.<"
			start()
	elif you_say == "kick him":
		print "The holy dog is angry. He poops on your face."
		print "You are sent back to the cross road."
		start()
	else:
		print "\nNothing happened....."
		holy_dog()

def holy_dog2():
	print "You already have all you need to fight Evil Peggy."
	print "Remember to use the spell 'call the holy dog' ASAP!"
	print "You want to 'stay' or 'leave'?"
	decision2 = raw_input('> ')
	
	if decision2 == 'leave':
		start2()
	else:
		holy_dog2()
	
		
start()
print "\nyou leave the room and go back to the cross road."
remedynumber = 5
start2()



#final_stage(hardness, yourlife, attachtype, remedynumber)
