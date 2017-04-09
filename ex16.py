from sys import argv

script, filename = argv

print "we are going to erase %r." % filename
print "if you don't want that, hit Ctrl-c (^c)."
print "if you do want that, hit RETURN."

raw_input("?")

print "Open the file..."
target = open(filename, 'w')

print "Truncating the file. Goobye!"
target.truncate()

print "Now I'm going to ask	 you for three lines."

line1 = raw_input("line1: ")
line2 = raw_input("line2: ")
line3 = raw_input("line3: ")

print "I'm going to write these to the file."

Alline = line1 + "\n" + line2 + "\n" + line3 + "\n"

target.write(Alline)

print "And finally, we close it."
target.close()

