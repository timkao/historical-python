print "This program is designed to read your mind...."
print "Now, think of any integer number in your mind. for example, how old are you, how many shoes do you have?\n"

raw_input("Ready? Press Enter!")
end = "Press Enter to continue..."

print "OK. Here we go. Add 12 to the numberp you think. %s" % end
raw_input()

print "Then, times 2. %s" % end
raw_input()

print "Then, add 7. The ancient secrete number from East. Type the 7 in the screen to add the magic to the machine. %s" % end
raw_input()

print "Then, times 3. %s" % end
raw_input()

print "Then minus 45. The secrete number from Mars. By the way, if your math is bad, you are not qualified to play this game."
raw_input("Are you idiot of Math? Press Ctrl-C if you are or %s" % end)

print "Now, type the current number: "
anwser = raw_input()
truth = int(anwser)

print "The number in your mind was: %d." % (truth / 6 - 8)
