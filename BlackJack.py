import random
from sys import exit

def sumcard(ok):
	for i  in range(0, len(ok)):
	
		if ok[i] == "J" or ok[i] == "Q" or ok[i] == "K":
			ok[i] = 10
		else:
			pass

	ok.sort()
	if ok.count("A") == 2:
		ok[-2] = 1
	elif ok.count("A") == 3:
		ok[-2] = 1
		ok[-3] = 1
	elif ok.count("A") == 4:
		ok[-2] = 1
		ok[-3] = 1
		ok[-4] = 1
	else:
		pass
		
	if ok.count("A") == 0:
	
		x = 0	
	
		for j in range(0, len(ok)):	
			x = x + ok[j]
	
		return x
	
	elif ok.count("A") == 1:
	
		x1 = 0
	
		for k in range(0, len(ok) - 1):
			x1 = x1 + ok[k]
	
		if x1 <= 10:
			x1sum = x1 + 11
			return x1sum
			
		else:
			x1sum = x1 + 1
			return x1sum
		
	else:
		pass

def boss_term(bosscard, ok, deck):
	
	print "The boss reveals his first card. It is %d." % bosscard[1]
	boss_current = sumcard(bosscard)
	yourpoint = sumcard(ok)
	print "His current point is %d" % boss_current
	print "Your final point is %d" % yourpoint
	
	while sumcard(bosscard) < 17:
		print "The Boss decided to ask for one more card."
		Addional = deck.pop()
		print "He got a [%r]" % Addional
		bosscard.append(Addional)
		
		if sumcard(bosscard) > 21:
			print "His point is larger than 21. You win!!"
			exit()
		else:
			print "His current point is %d" % sumcard(bosscard)
		
	else:
		print "He decides not to ask for more cards."
		return sumcard(bosscard)
		
deck_of_cards = []
Boss_card = []
Your_card = []
newlist = []
	
for j in range(1, 5):
	for i in ["A", 2, 3, 4, 5, 6, 7, 8, 9, 10, "J", "Q", "K"]:
		deck_of_cards.append(i)
	
print "The deck has %d cards"  % len(deck_of_cards)


random.shuffle(deck_of_cards)
	
Boss_first_card = deck_of_cards.pop()
Boss_card.append(Boss_first_card)
print "\nThe Boss give him self a card."
print "The card faces down on the table. So you cannot know what extacly it is.\n"
		
Your_first_card = deck_of_cards.pop()
Your_card.append(Your_first_card)
newlist.append(Your_first_card)
print "The boss then give you a card."
print "Would you like to take a look?"
look = raw_input('yes or no ?\n')
		
if look == "yes":
	print "You got %r" % Your_card
else:
	pass
		
Boss_second_card = deck_of_cards.pop()
Boss_card.append(Boss_second_card)
Your_second_card = deck_of_cards.pop()
Your_card.append(Your_second_card)
newlist.append(Your_second_card)
print "\nThe Boss then give himself anotehr card [%r]" % Boss_second_card
print "Then he give you another card [%r]" % Your_second_card


while True:
	print "\t\tWhat would you like to do know?"
	print "\t\t'ask' for more cards."
	print "\t\t'call' to end your turn."
	print "\t\t'check' to check your all of your cards."
	print "\t\t'see' to check what the boss has on the table"
	act = raw_input('> ')
	
	if act == "ask":
		Additional_card = deck_of_cards.pop()
		newlist.append(Additional_card)
		Your_card.append(Additional_card)
		print "The Boss give you another card [%r]." % Additional_card
		final = sumcard(Your_card)
		
		if final > 21:
			print "The sum of your cards is %d" % final
			print "It is bigger than 21. Boom!!!"
			print "You lose!"
			exit()
		else:
			continue
	
	elif act == "call":
		final = sumcard(Your_card)
		boss_final = boss_term(Boss_card, Your_card, deck_of_cards)
		
		if boss_final > final:
			print "The boss has in total %d point! More than that of yours!"
			print "You lose!"
			exit()
		elif boss_final < final:
			print "The boss only has %d point. You Win!!" % boss_final
			exit()
		else:
			print "No one wins....."
			exit()

	elif act == "check":
		print newlist
	
	elif act == "see":
		print Boss_second_card
