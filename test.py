def func(first, something, something2, test1, test2):
    print first
    print something, something2
    print test1, test2

firstvar = 'daniel'
l = [1, 2]
l2 = {'test1':'test1', 'test2':'test2'}
#print type(l2)
func(firstvar, *l, **l2)
