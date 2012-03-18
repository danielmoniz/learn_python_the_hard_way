tabby_cat = "\tI'm tabbed in."
persion_cat = "I'm split\non a line."
backslash_cat = "I'm \\ a \\ cat."

fat_cat = '''
I'll do a list:
\t* Cat food
\t* Fishies
\t* Catnip\n\t* Grass
'''

print tabby_cat
print persion_cat
print backslash_cat
print fat_cat

speech = "I have a dream!{}I have a dream that one day..."

print speech.format(' ')
print "   ...   "
print speech.format('\n')

speech2 = "But today is not this day! I, {!r}, am the man."

print speech2.format("Ara'agorn")
print speech2.format(r'Aragorn')
print speech2.format("""Aragorn""")
