import random
from sys import exit

# check the sum of the card on your hand
def sumcard(yourcard):
	# Calculate "J", "Q", "K" as 10 points
	for i  in range(0, len(yourcard)):
	
		if yourcard[i] == "J" or yourcard[i] == "Q" or yourcard [i] == "K":
			yourcard[i] = 10
		else:
			pass
	
	# Treat "A" specially. First, we need to know how many A in our hand. 
	# if you have more than two "A", except the first "A", other "As" should be calculated as 1 point.
	yourcard.sort()
	if yourcard.count("A") == 2:
		yourcard[-2] = 1
	elif yourcard.count("A") == 3:
		yourcard[-2] = 1
		yourcard[-3] = 1
	elif yourcard.count("A") == 4:
		yourcard[-2] = 1
		yourcard[-3] = 1
		yourcard[-4] = 1
	
	# Now, there are only two situation left. You have a "A" or You do not have any "A".
	# if you do not have any "A", the calculation is simple.
	if yourcard.count("A") == 0:
	
		x = 0	
	
		for j in range(0, len(yourcard)):	
			x = x + yourcard[j]
	
		return x
	
	#if you have one "A", the value of "A" depends on the sum of other cards.
	elif yourcard.count("A") == 1:
	
		x1 = 0
	
		for k in range(0, len(yourcard) - 1):
			x1 = x1 + yourcard[k]
	
		if x1 <= 10:
			x1sum = x1 + 11
			return x1sum
		else:
			x1sum = x1 + 1
			return x1sum
		
	else:
		pass

# when game is finished, ask the player if he would like to play again.
def play_again():
	print "You have %i in cash now" % Player1.money
	
	control = True
	while control:
		print "Do you want to play again?"
		input1 = raw_input('yes or no > ')
		
		if input1.lower() == "yes":
			a_game.play()
		elif input1.lower() == "no":
			exit(0)
		else:
			pass
	

class checkbet(object):

	# Make sure the input from player could be turned into integer
	def checkint(self, str1):
		x = False
		
		for i in range(len(str1)):
			if ord(str1[i]) < 48 or ord(str1[i]) > 57:
				x = True
			else:
				pass
				
		return x
		
	# Make sure the input from the player is bug free
	def checkall(self):
		con1 = True
		
		while con1:
			print "\t\t\tHow much you would like to put on the table?"
			print "\t\t\t(please give me an integer)?"
			str1 = raw_input('> ')
			con1 = calculator.checkint(str1)
		
		yourbet = int(str1)
		
		if yourbet > Player1.money:
			print "\t\t\tYou do not have enough money!"
			calculator.checkall()
		else:
			return yourbet
	
	# When the splitting happens, 
	# This function is used to compared player's points and the opponent's point.
	def checkresult(self, op, fp, sp):
		if op > max(fp, sp):
			print "\t\t\tYou lose all the bet!"
			return 0
		elif op < min(fp, sp):
			print "\t\t\tYou win all the bet!"
			return a_game2.reward_rate_normal * (Player1.yourfirstbet + Player1.yoursecondbet)
		elif op < fp and op > sp:
			print "\t\t\tYou win the first bet but lose the second bet."
			return a_game2.reward_rate_normal * Player1.yourfirstbet
		elif op < fp and op > sp:
			print "\t\t\tYou lose the first bet but win the second bet."
			return a_game2.reward_rate_normal * Player1.yoursecondbet
		elif op == fp and op < sp:
			print "\t\t\tYou win the second bet!"
			return a_game2.reward_rate_normal * Player1.yoursecondbet + Player1.yourfirstbet
		elif op == fp and op > sp:
			print "\t\t\tYou lose the second bet!"
			return Player1.yourfirstbet
		elif op > fp and op == sp:
			print "\t\t\tYou lose the first bet!"
			return Player1.yoursecondbet
		elif op < fp and op == sp:
			print "\t\t\tYou win the first bet!"
			return a_game2.reward_rate_normal * Player1.yourfirstbet + Player1.yoursecondbet
		else:
			print "\t\t\tEven!"
			return Player1.yourfirstbet + Player1.yoursecondbet
			
	# Check if the opponent's points are not more than 21 and the opponent's cards are less than five.		
	def check_oppoent1(self, op, opli):
		if op > 21:
			print "\t\t\tThe opponent has %s now." % Player2.bosscarddeck2
			print "\t\t\tIt is over 21 points. You win!" 
			print "\t\t\tYou win the bet %i" % Player1.yourfirstbet
			Player1.money = Player1.money + a_game2.reward_rate_normal * Player1.yourfirstbet
			play_again()
		elif op < 21 and len(opli) == 5:
			print "\t\t\tThe opponent has 5 cards in the deck. You lose!"
			print "\t\t\tYou lose the bet %i" % Player1.yourfirstbet
			play_again()
		else:
			pass
			
	# Check if the opponent's points are not more than 21 and the opponent's cards are less than five.		
	def check_oppoent2(self, op, opli):
		if op > 21:
			print "\t\t\tThe opponent has %s now." % Player2.bosscarddeck2
			print "\t\t\tIt is over 21 points. You win!" 
			print "\t\t\tYou win the bet %i" % Player1.yoursecondbet
			Player1.money = Player1.money + a_game2.reward_rate_normal * Player1.yoursecondbet
			play_again()
		elif op < 21 and len(opli) == 5:
			print "\t\t\tThe opponent has 5 cards in the deck. You lose!"
			print "\t\t\tYou lose the bet %i" % Player1.yoursecondbet
			play_again()
		else:
			pass
	
	def check_oppoent3(self, op, opli):
		if op > 21:
			print "\t\t\tThe opponent has %s now." % Player2.bosscarddeck2
			print "\t\t\tIt is over 21 points. You win!" 
			print "\t\t\tYou win the bet %i" % (Player1.yoursecondbet + Player1.yourfirstbet)
			Player1.money = Player1.money + a_game2.reward_rate_normal * (Player1.yoursecondbet + Player1.yourfirstbet)
			play_again()
		elif op < 21 and len(opli) == 5:
			print "\t\t\tThe opponent has 5 cards in the deck. You lose!"
			print "\t\t\tYou lose the bet %i" % (Player1.yoursecondbet + Player1.yourfirstbet)
			play_again()
		else:
			pass
			

			
class Start_Scene(object):
	
	additional_deck = []
	
	def play(self):
	# check whether the player have enough money. if not, the game would not start.
		if Player1.money <= 0:
			print "You are out of money. You lose!"
			exit(0)
		else:
			pass
		
		if len(deck_of_cards) < 14:
			for j in range(1, 9):
				for i in ["A", 2, 3, 4, 5, 6, 7, 8, 9, 10, "J", "Q", "K"]:
					self.additional_deck.append(i)
			
			random.shuffle(self.additional_deck)	
			deck_of_cards.extend(self.additional_deck)
		else:
			pass
		
		Player1.yourcarddeck = []
		Player1.yoursplitdeck = []
		Player2.bosscarddeck = []
		
		print "\t\t\tYou have %i dollars in cash" % Player1.money
		print "\t\t\tYou are in a casino."
		print "\t\t\tThe table is for BlackJack"
		
		Player1.yourfirstbet = calculator.checkall()
		Player1.money = Player1.money - Player1.yourfirstbet
		
		print "\t\t\tYou bet %i" % Player1.yourfirstbet
		print "\t\t\tYou got two cards."
		your_first_card = deck_of_cards.pop()
		your_second_card = deck_of_cards.pop()
		boss_first_card = deck_of_cards.pop()
		boss_second_card = deck_of_cards.pop()
		Player1.yourcarddeck.append(your_first_card)
		Player1.yourcarddeck.append(your_second_card)
		Player1.yourcarddeck2 = Player1.yourcarddeck[:]
		Player2.bosscarddeck.append(boss_first_card)
		Player2.bosscarddeck.append(boss_second_card)
		print "\t\t\tyou have %s" % Player1.yourcarddeck
		print "\n\t\t\tThe opponent give himself a card."
		print "\t\t\tThe card faces down on the table." 
		print "\t\t\tTherefore, you cannot know what extacly it is."
		print "\t\t\tThe opponent then give himself anotehr card [%r]" % boss_second_card
		a_game2.enter()
		

class Second_Scene(object):
	
	reward_rate_5card = 3
	reward_rate_normal = 2
	
	def enter(self):
		control = True
		while control:
			print "What would you want to do?"
			print "1. Ask for one more card\n2. Ask for splitting\n3. Check your cards on hand."
			print "4. Check boss card\n5. Finish your turn"
			print "Choose 1, 2, 3, 4 or 5"
			action = raw_input('>')
			
			if action in ["1", "2", "3", "4", "5"]:
				control = False
			else:
				control = True
			
		if action == "1":
			additional_card = Player1.drawcard()
			Player1.yourcarddeck.append(additional_card)
			Player1.yourcarddeck2.append(additional_card)
			print "\t\t\tYou have %s" % Player1.yourcarddeck2
			
			if sumcard(Player1.yourcarddeck) > 21:
				print "\t\t\tYou are over 21 points. You lose!"
				play_again()
			elif len(Player1.yourcarddeck) == 5:
				print "\t\t\tYou win!"
				Player1.money = Player1.money + self.reward_rate_5card * Player1.yourfirstbet
				play_again()
			else:
				a_game2.enter()
		
		elif action == "2":
			Player1.splitcard()
			Player1.yourcarddeck2 = Player1.yourcarddeck[:]
			Player1.yoursplitdeck2 = Player1.yoursplitdeck[:]
			a_game2.after_split()
		
		elif action == "3":
			Player1.checkcards()
			a_game2.enter()
			
		elif action == "4":
			Player2.checkbosscard()
			a_game2.enter()
			
		elif action == "5":
			a_game2.Opponent_turn()
			
		else:
			a_game2.enter()
			
	def after_split(self):
		if (sumcard(Player1.yourcarddeck) > 21 or len(Player1.yourcarddeck) == 5) and (sumcard(Player1.yoursplitdeck) > 21 or len(Player1.yoursplitdeck) == 5):
			play_again()
		else:
			pass
		
		control = True
		while control:
			print "What would you want to do?"
			print "1. Ask for one more card for the first deck\n2. Ask for one more card for the second deck\n3. Check your cards on hand."
			print "4. Check boss card\n5. Finish your turn"
			print "Choose 1, 2, 3, 4 or 5"
			action = raw_input('>')
			
			if action in ["1", "2", "3", "4", "5"]:
				control = False
			else:
				control = True
			
		if action == "1" and sumcard(Player1.yourcarddeck) <= 21 and len(Player1.yourcarddeck) < 5:
			additional_card = Player1.drawcard()
			Player1.yourcarddeck.append(additional_card)
			Player1.yourcarddeck2.append(additional_card)
			print "\t\t\tThe deck is %s" % Player1.yourcarddeck2
			
			if sumcard(Player1.yourcarddeck) > 21:
				print "\t\t\tYou are over 21 points."
				print "\t\t\tYou lose your first bet %i!" % Player1.yourfirstbet
				a_game2.after_split()
			elif len(Player1.yourcarddeck) == 5:
				print "\t\t\tYou win the first bet %i!" % Player1.yourfirstbet
				Player1.money = Player1.money + self.reward_rate_5card * Player1.yourfirstbet	
			else:
				a_game2.after_split()
		
		elif action == "2" and sumcard(Player1.yoursplitdeck) <= 21 and len(Player1.yoursplitdeck) < 5:
			additional_card = Player1.drawcard()
			Player1.yoursplitdeck.append(additional_card)
			Player1.yoursplitdeck2.append(additional_card)
			print "\t\t\tThe deck is %s" % Player1.yoursplitdeck2
			
			if sumcard(Player1.yoursplitdeck) > 21:
				print "\t\t\tYou are over 21 points."
				print "\t\t\tYou lose your second bet %i!" % Player1.yoursecondbet
				a_game2.after_split()
			elif len(Player1.yoursplitdeck) == 5:
				print "\t\t\tYou win the second bet %i!" % Player1.yourfirstbet
				Player1.money = Player1.money + self.reward_rate_5card * Player1.yoursecondbet	
			else:
				a_game2.after_split()
		
		elif action == "3":
			Player1.checkcards()
			a_game2.after_split()
			
		elif action == "4":
			Player2.checkbosscard()
			a_game2.after_split()
			
		elif action == "5":
			a_game2.Opponent_turn()
			
		else:
			print "\t\t\tYou cannot do it."
			a_game2.after_split()
			
	def Opponent_turn(self):
		#Calculate the final point of the player
		if sumcard(Player1.yourcarddeck) > 21 or len(Player1.yourcarddeck) == 5:
			Player_point = sumcard(Player1.yoursplitdeck)
		elif len(Player1.yoursplitdeck) != 0 and (sumcard(Player1.yoursplitdeck) > 21 or len(Player1.yoursplitdeck) == 5):
			Player_point = sumcard(Player1.yourcarddeck)
		elif len(Player1.yoursplitdeck) == 0:
			Player_point = sumcard(Player1.yourcarddeck)
		else:
			Player_point = list((sumcard(Player1.yourcarddeck), sumcard(Player1.yoursplitdeck)))
		
		print Player_point
		
		#The opponent check which cards player has. Of course, he cannot see the card which is upside down.
		if len(Player1.yoursplitdeck) == 0:
			Player_card = Player1.yourcarddeck[1:]
			scenario = 1
		elif type(Player_point) == type(20):
			if sumcard(Player1.yourcarddeck) <= 21 and len(Player1.yourcarddeck) < 5:
				Player_card = Player1.yourcarddeck[1:]
				scenario = 1
			elif sumcard(Player1.yoursplitdeck) <= 21 and len(Player1.yoursplitdeck) < 5:
				Player_card = Player1.yoursplitdeck[1:]
				scenario = 2
			else:
				pass		
		elif type(Player_point) == list:
			Player_card = [Player1.yourcarddeck[1:], Player1.yoursplitdeck[1:]]
			scenario = 3
		else:
			pass
			
		print Player_card
		print "\t\t\tThe opponent reveals his deck." 
		print "\t\t\tHe has %s" % Player2.bosscarddeck
		Player2.bosscarddeck2 = Player2.bosscarddeck[:]
		
		# Based on what he saw and his current card, he makes decision to draw or not to draw the card and to call or not to call the player.
		opponent_think = True
		while opponent_think:
			if scenario == 1:
				if sumcard(Player2.bosscarddeck) < sumcard(Player_card):
					additional_card = Player2.drawcard()
					Player2.bosscarddeck.append(additional_card)
					Player2.bosscarddeck2.append(additional_card)
					calculator.check_oppoent1(sumcard(Player2.bosscarddeck), Player2.bosscarddeck)
		
				elif sumcard(Player2.bosscarddeck) < 21 and sumcard(Player2.bosscarddeck) > sumcard(Player_card) + 11:
					print "\t\t\tThe opponent decides to finish his turn as well."
					print "\t\t\tYou have %s, %i points" % (Player1.yourcarddeck2, Player_point)
					print "\t\t\tThe opponent has %s, %i points" % (Player2.bosscarddeck2, sumcard(Player2.bosscarddeck))
					print "\t\t\tYou lose the bet %i" % Player1.yourfirstbet
					play_again()
					
				elif sumcard(Player2.bosscarddeck) < 16:
					additional_card = Player2.drawcard()
					Player2.bosscarddeck.append(additional_card)
					Player2.bosscarddeck2.append(additional_card)
					calculator.check_oppoent1(sumcard(Player2.bosscarddeck), Player2.bosscarddeck)

				elif sumcard(Player2.bosscarddeck) <= 18 and len(Player2.bosscarddeck) == 4:
					additional_card = Player2.drawcard()
					Player2.bosscarddeck.append(additional_card)
					Player2.bosscarddeck2.append(additional_card)
					calculator.check_oppoent1(sumcard(Player2.bosscarddeck), Player2.bosscarddeck)

				else:
					print "\t\t\tThe opponent decides to finish his turn as well."
					print "\t\t\tYou have %s, %i points" % (Player1.yourcarddeck2, Player_point)
					print "\t\t\tThe opponent has %s, %i points" % (Player2.bosscarddeck2, sumcard(Player2.bosscarddeck))
					if sumcard(Player2.bosscarddeck) > Player_point:
						print "\t\t\tYou lose the bet %i" % Player1.yourfirstbet
						play_again()
					elif sumcard(Player2.bosscarddeck) < Player_point:
						print "\t\t\tYou win the bet %i" % Player1.yourfirstbet
						Player1.money = Player1.money + self.reward_rate_normal * Player1.yourfirstbet
						play_again()
					else:
						print "\t\t\tEven!"
						Player1.money = Player1.money + Player1.yourfirstbet
						play_again()
						
			elif scenario == 2:
				if sumcard(Player2.bosscarddeck) < sumcard(Player_card):
					additional_card = Player2.drawcard()
					Player2.bosscarddeck.append(additional_card)
					Player2.bosscarddeck2.append(additional_card)
					calculator.check_oppoent2(sumcard(Player2.bosscarddeck), Player2.bosscarddeck)
					
				elif sumcard(Player2.bosscarddeck) < 21 and sumcard(Player2.bosscarddeck) > sumcard(Player_card) + 11:
					print "\t\t\tThe opponent decides to finish his turn as well."
					print "\t\t\tYou have %s, %i points" % (Player1.yoursplitdeck2, Player_point)
					print "\t\t\tThe opponent has %s, %i points" % (Player2.bosscarddeck2, sumcard(Player2.bosscarddeck))
					print "\t\t\tYou lose the bet %i" % Player1.yoursecondbet
					play_again()
				
				elif sumcard(Player2.bosscarddeck) < 16:
					additional_card = Player2.drawcard()
					Player2.bosscarddeck.append(additional_card)
					Player2.bosscarddeck2.append(additional_card)
					calculator.check_oppoent2(sumcard(Player2.bosscarddeck), Player2.bosscarddeck)
		
				elif sumcard(Player2.bosscarddeck) <= 18 and len(Player2.bosscarddeck) == 4:
					additional_card = Player2.drawcard()
					Player2.bosscarddeck.append(additional_card)
					Player2.bosscarddeck2.append(additional_card)
					calculator.check_oppoent2(sumcard(Player2.bosscarddeck), Player2.bosscarddeck)
				
				else:
					print "\t\t\tThe opponent decides to finish his turn as well."
					print "\t\t\tYou have %s, %i points" % (Player1.yoursplitdeck2, Player_point)
					print "\t\t\tThe opponent has %s, %i points" % (Player2.bosscarddeck2, sumcard(Player2.bosscarddeck))
					if sumcard(Player2.bosscarddeck) > Player_point:
						print "\t\t\tYou lose the bet %i" % Player1.yoursecondbet
						play_again()
					elif sumcard(Player2.bosscarddeck) < Player_point:
						print "\t\t\tYou win the bet %i" % Player1.yoursecondbet
						Player1.money = Player1.money + self.reward_rate_normal * Player1.yoursecondbet
						play_again()
					else:
						print "\t\t\tEven!"
						Player1.money = Player1.money + Player1.yoursecondbet
						play_again()	
			
			elif scenario == 3:
				if sumcard(Player2.bosscarddeck) < max(sumcard(Player_card[0]), sumcard(Player_card[1])):
					additional_card = Player2.drawcard()
					Player2.bosscarddeck.append(additional_card)
					Player2.bosscarddeck2.append(additional_card)
					calculator.check_oppoent3(sumcard(Player2.bosscarddeck), Player2.bosscarddeck)
					
				elif sumcard(Player2.bosscarddeck) < 21 and sumcard(Player2.bosscarddeck) > max(sumcard(Player_card[0]), sumcard(Player_card[1])) + 11:
					print "\t\t\tThe opponent decides to finish his turn as well."
					print "\t\t\tYou have [%s, %s], %s points" % (Player1.yourcarddeck2, Player1.yoursplitdeck2, Player_point)
					print "\t\t\tThe opponent has %s, %i points" % (Player2.bosscarddeck2, sumcard(Player2.bosscarddeck))
					print "\t\t\tYou lose the bet %i" % (Player1.yoursecondbet + Player1.yourfirstbet)
					play_again()
				elif sumcard(Player2.bosscarddeck) < 16:
					additional_card = Player2.drawcard()
					Player2.bosscarddeck.append(additional_card)
					Player2.bosscarddeck2.append(additional_card)
					calculator.check_oppoent3(sumcard(Player2.bosscarddeck), Player2.bosscarddeck)
			
				elif sumcard(Player2.bosscarddeck) <= 18 and len(Player2.bosscarddeck) == 4:
					additional_card = Player2.drawcard()
					Player2.bosscarddeck.append(additional_card)
					Player2.bosscarddeck2.append(additional_card)
					calculator.check_oppoent3(sumcard(Player2.bosscarddeck), Player2.bosscarddeck)
	
				else:
					print "\t\t\tThe opponent decides to finish his turn as well."
					print "\t\t\tYou have [%s, %s], %i and %i points" % (Player1.yourcarddeck2, Player1.yoursplitdeck2, Player_point[0], Player_point[1])
					print "\t\t\tThe opponent has %s, %i points" % (Player2.bosscarddeck2, sumcard(Player2.bosscarddeck))
					outcome = calculator.checkresult(sumcard(Player2.bosscarddeck), Player_point[0], Player_point[1])
					Player1.money = Player1.money + outcome
					play_again()
	

class player(object):
	money = 1000
	yourcarddeck = []
	yourcarddeck2 = []
	yoursplitdeck = []
	yoursplitdeck2= []
	yourfirstbet = 0
	yoursecondbet = 0
	bosscarddeck = []
	bosscarddeck2 = []
	
	def __init__(self, name):
		self.name = name
		
	def drawcard(self):
		print "\t\t\tAsk for one more card."
		additonal_card = deck_of_cards.pop()
		print "\t\t\t..........\n"
		print "\t\t\tThe card is [%r]" % additonal_card
		return additonal_card
	
	def splitcard(self):
		if sumcard(self.yourcarddeck[:1]) == sumcard(self.yourcarddeck[1:]) and len(self.yoursplitdeck) == 0 and self.money != 0:
			print "\t\t\tYou separate the cards into two decks" 
		
			self.yoursecondbet = calculator.checkall()
			self.money = self.money - self.yoursecondbet
			
			self.yourcarddeck = self.yourcarddeck[:1]
			self.yoursplitdeck = self.yourcarddeck[:1]
			a_additional_card = deck_of_cards.pop()
			b_additional_card = deck_of_cards.pop()
			self.yourcarddeck.append(a_additional_card)
			self.yourcarddeck2 = self.yourcarddeck[:]
			self.yoursplitdeck.append(b_additional_card)
			self.yoursplitdeck2 = self.yoursplitdeck[:]
			print "\t\t\tThe boss split the card and" 
			print "\t\t\tgive you an additional card to each of your card deck"
			print "\t\t\tNow you have %s and %s" % (self.yourcarddeck, self.yoursplitdeck)
			
		else:
			print "\t\t\tYou cannot do it." 
			print "\t\t\tOnly if your two cards were the same points" 
			print "\t\t\tand you had at least 1 dollar left,"
			print "\t\t\tyou could split the card."
			a_game2.enter()	
			
	def checkcards(self):
		if len(self.yoursplitdeck) > 0:
			print "\t\t\tYou have %s and %s" % (self.yourcarddeck2, self.yoursplitdeck2)
		else:
			print "\t\t\tYou have %s on hand" % self.yourcarddeck2
	
	def checkbosscard(self):
		print "\t\t\tOn the table, your opponent has [%s]" % self.bosscarddeck[1]
		

# Create a deck of cards (52 * 2) and shuffle it
deck_of_cards = []
for j in range(1, 9):
	for i in ["A", 2, 3, 4, 5, 6, 7, 8, 9, 10, "J", "Q", "K"]:
		deck_of_cards.append(i)

random.shuffle(deck_of_cards)			

	
# Start the game
calculator = checkbet()						
Player1 = player('Peggy')
Player2 = player('Boss')
a_game2 = Second_Scene()
a_game = Start_Scene()
a_game.play()
			
