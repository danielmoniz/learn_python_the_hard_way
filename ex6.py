x = "There are {0} types of people.".format(10)
binary = "binary"
do_not = "don't"
y = "Those who know {} and those who {}.".format(binary, do_not)

print x
print y

print "I said: {!r}.".format(x)
print "I also said: '{}'.".format(y)

hilarious = False
joke_evaluation = "Isn't that joke so funny?! {!r}"
print joke_evaluation.format(hilarious)

w = "This is the left side of..."
e = "a string with a right side."

print w + e
