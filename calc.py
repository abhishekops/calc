from operator import add, sub, mul, truediv
from functools import reduce
import argparse

op_map = {'+': add,
		  '-': sub,
		  '*': mul,
		  '/': truediv}

parser = argparse.ArgumentParser(description='Calculator for few operations.')
parser.add_argument('numbers', nargs='*', type=int)
parser.add_argument('--operation', choices=["+", "-", "*", "/"], required=True)
args = parser.parse_args()

def calculator():
	# Reduce function iterates over the list by taking values as tuples of two,
	# performs the lambda expression, takes the result as the first value of the next tuple.
	try:
		res = reduce((lambda x, y: op_map[args.operation](x, y)), args.numbers)
		print('Result for {} on {} is'.format(args.operation, args.numbers), res)
	except ZeroDivisionError:
		print('Doesnt allow division with 0, please choose non zero numbers')

calculator()