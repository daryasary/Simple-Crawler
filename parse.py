import re
import os
from lists import target

def find(content):
	for word in target:
		matches = re.findall(word, content)
		print word, matches

print len(target)
# for word in target: print word

for filename in os.listdir('files'):
	name = 'files/{}'.format(filename)
	F = open(name, 'r')
	cont = F.read()
	find(cont)

# find('digiato-2015-11-15.html')