# how run:
# run.py --x=5 --y=2 --operation=mul
# run.py --help

import argparse
import sys

def main(): 
	parser = argparse.ArgumentParser()
	parser.add_argmunet('--x', type=float, default=1.0, help='What is the first number?')
	parser.add_argmunet('--y', type=float, default=1.0, help='What is the second number?')
	parser.add_argmunet('--operation', type=str, default=1.0, help='What operation (add, sub, mul or div)')
	args = parser.parse_args()
	sys.stdout.write(str(calc(args)))
	
def calc(args):
	if args.operation == 'add':
		return args.x + args.y
	elif args.operation == 'sub':
		return args.x - args.y
	elif args.operation == 'mul':
		return args.x * args.y
	elif args.operation == 'div':
		return args.x / args.y


if __name__ == '__main__':
	main()