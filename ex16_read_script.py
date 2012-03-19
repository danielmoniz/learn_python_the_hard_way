from sys import argv

filename = argv[1]

target = open(filename, 'r')
print target.read()
