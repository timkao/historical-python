# insert headers
from sys import argv
from os.path import exists

# unpacking argv
script, from_file, to_file = argv

print "copy from %s to %s." % (from_file, to_file)

# open the file and assign the data to indata
in_file = open(from_file)
indata = in_file.read()

print "The input file is %d byte long." % len(indata)

# Write the data in to_file
print "Does the output file exists %r?" % exists(to_file)
print "Ready? Hit RETURN to continue, Ctrl-C to abort."
raw_input()

out_file = open(to_file, 'w')
out_file.write(indata)

print "Alright, all done."

# close files
out_file.close()
in_file.close()