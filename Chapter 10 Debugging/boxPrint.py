def boxPrint(symbol, width, height):
	if len(symbol) != 1:
		raise Exception('Symbol must be a singles character string.')
	if width <= 2:
		raise Exception('width must be greater than 2.')
	if height <= 2:
		raise Exception('Height mut be greater than 2.')
	print(symbol * width)
	for x in range(height - 2):
		print(symbol + (' ' * (width - 2)) + symbol)
	print(symbol * width)

for sym,w,h in (('*', 4, 4), ('O', 20, 5), ('x', 1, 3), ('ZZ', 3, 3)):
	try:
		boxPrint(sym, w, h)
	except Exception as error:
		print('An exception happened: ' + str(error))