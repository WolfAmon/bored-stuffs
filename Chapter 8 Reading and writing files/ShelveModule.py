'''
El modulo shelve permite guardas variables en archivos binarios para posteriormente usar como en configuraciones o cosas de ese estilo, puedes restaurar los datos del disco duro
'''

import shelve

# Creando el archivo para guardar los datos

shelveFile =  shelve.open('mydata')
cats = ['Zophie', 'Pooka', 'Simon']
shelveFile['cats'] = cats
shelveFile.close()

# Abriendo el archivo para obtener los datos

shelveFile = shelve.open('mydata')
print(type(shelveFile))
print(shelveFile['cats'])
shelveFile.close()

# Getting data like list, it has a behaviour like dictionaries

shelveFile = shelve.open('mydata')
print('\nthe keys for the file are...')
print( list(shelveFile.keys()) )
print('\nthe values in the file are...')
print( list(shelveFile.values()) )
shelveFile.close()

