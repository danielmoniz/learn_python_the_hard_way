from sys import argv

script, user_name, education = argv
prompt = '==> '

print "Hi {}, I'm the {} script.".format(user_name, script)
print "I'd like to ask you a few questions."
print "Do you like me {}?".format(user_name)
likes = raw_input(prompt)

print "Where do you live {}?".format(user_name)
lives = raw_input(prompt)

print "What kind of computer do you have?"
computer = raw_input(prompt)

print "How was your education in {}?".format(education)
edu_description = raw_input(prompt)

print """
Alright, so you said {!r} about liking me.
You live in {!r}. Not sure where that is.
Your education in {!r} was {!r}.
And you have a {!r} computer. Nice.
""".format(likes, lives, education, edu_description, computer)
