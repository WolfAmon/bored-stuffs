import logging

logging.basicConfig(filename='factorialLog.txt', level=logging.DEBUG, format=' %(asctime)s - %(levelname)s - %(message)s')

logging.debug('start the program')

def factorial(n):
	logging.debug('start of factorial (%s)' % (n))

	total = 1
	for x in range(1, n + 1):
		total *= x
		logging.debug('x is ' + str(x) + ', total is ' + str(total))

	logging.debug('End of factorial (%s)' % (n))
	return total

print(factorial(5))
logging.debug('End of program')