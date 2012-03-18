# import the 'argv' command so we can get parameters from cmd line
from sys import argv

# define the first two arguments to be the script and file name
script, filename = argv

# open the file stored at filename and set it to be the var 'txt'
txt = open(filename)

# print out the filename
print "Here's your file {!r}".format(filename)
# print out the full text read from the file 'txt'
print txt.readline()

txt.close()
