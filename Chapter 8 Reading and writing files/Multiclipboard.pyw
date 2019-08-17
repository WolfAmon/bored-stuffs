#! python3
# mcb.pyw - Saves and loads pieces of text to the clipboard.
# Usage: py.exe mcb.pyw save <keyword> - Saves clipboard to keyword.
#        py.exe mcb.pyw <keyword> - Loads keyword to clipboard.
#        py.exe mcb.pyw list - Loads all keywords to clipboard.

# the pyw extension means that python won't show a terminal windows so t will be necessary a file bat to execute

import shelve, pyperclip, sys

mcbShelf = shelve.open('mcb')

if len(sys.argv) == 3:
	if sys.argv[1].lower() == 'save':		
		mcbShelf[sys.argv[2]] = pyperclip.paste()
	elif sys.argv[1].lower() == 'delete':		
		if sys.argv[2] in mcbShelf:		
			del mcbShelf[sys.argv[2]]
		else:
			print('does not exists key %s' % (sys.argv[2]))
elif len(sys.argv) == 2:
	if sys.argv[1].lower() == 'list':
		pyperclip.copy(str(list(mcbShelf.keys())))
	elif sys.argv[1].lower() == 'delete':
		mcbShelf.clear()
	elif sys.argv[1] in mcbShelf:
		pyperclip.copy(mcbShelf[sys.argv[1]])

mcbShelf.close()