from functools import reduce # for reducing our code into 1 line

def ArrayNumAdder(numlist):
	return reduce(lambda a,b: a+b, numlist)

if __name__ == '__main__':
        mylist = [1,2,3,4,5]
        print(ArrayNumAdder(mylist))
