from sys import argv
from os.path import exists

script, from_file, to_file = argv

print "Copying from {} to {}".format(from_file, to_file)

# we could do these two on one line, how?

input = open(from_file)
indata = input.read()

# print "The input file is {} bytes long".format(len(indata))

# print "Does the output file exist? {!r}".format(exists(to_file))
# print "Ready, hit RETURN to continue, CTRL-C to abort."
# raw_input()

output = open(to_file, 'w')
output.write(indata)

print "All done!"

output.close()
input.close()
