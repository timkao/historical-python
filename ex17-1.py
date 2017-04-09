from sys import argv

script, from_file, to_file = argv

print "copy %s to %s." % (from_file, to_file)
print "Are you sure? RETURN to continue\\Ctrl-c to abort"
raw_input()

infile = open(from_file)
indata = infile.read()

outfile = open(to_file, 'w')
outfile.write(indata)

print "Done"
infile.close()
outfile.close()

outfile = open(to_file)
content = outfile.read()
print "The content of outfile is %s." % content