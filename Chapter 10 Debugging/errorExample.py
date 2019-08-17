import traceback

# def spam():
# 	bacon()

# def bacon():
# 	raise Exception('This is the error message.')

# spam()

# ****** Handle errors and send to a logfile *****

try:
	raise Exception('This is the error message')
except Exception as e:
	errorFile = open('errorInfo.txt', 'w')
	errorFile.write(traceback.format_exc())
	errorFile.close()
	print('The traceback info was written to the errorInfo.txt')

