from sys import argv

script, filename = argv

print "We're going to erase {!r}.".format(filename)
print "If you don't want that, hit CTRL-C (^C)."
print "If you do want that, hit RETURN."

raw_input("?")

print "Opening the file..."
target = open(filename, 'w')

print "Truncating the file. Goodbye!"
target.truncate()

print "Now I'm going to ask you for three lines."

line1 = raw_input("line 1: ")
line2 = raw_input("line 2: ")
line3 = raw_input("line 3: ")

print "I'm going to write these to the file."

file_output = line1 + "{0}" + line2 + "{0}" + line3 + "{0}"
file_output = file_output.format("\n")
target.write(file_output)
"""target.write(line1)
target.write("\n")
target.write(line2)
target.write("\n")
target.write(line3)
target.write("\n")"""

print "And finally we close it."
target.close()
