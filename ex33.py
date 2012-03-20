numbers = []

def print_numbers(max_num, increment = 1):
    i = 0

    for i in range(0, max_num):
        print "At the top i is {}".format(i)
        numbers.append(i)

        i += increment
        print "Numbers now: ", numbers
        print "At the bottom i is {}".format(i)


print_numbers(10, 5)
print "The numbers: "

for num in numbers:
    print num
