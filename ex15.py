# make argv functional
from sys import argv

# unpakcing argv
script, filename = argv

# open a file and assinged to txt
txt = open(filename)

# print out the content of the file
print "Here is your file %r." % filename
print txt.read()

# ask the user to give a filename
print "Type the file name again: "
file_again = raw_input("> ")

# assign the file ot txt_again
txt_again = open(file_again)

# print out the content of txt_again
print txt_again.read()

txt.close()
txt_again.close()
