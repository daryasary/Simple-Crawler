import re
import os
from lists import target
from datetime import date

def find(content):
	result = open('result.txt', 'w')
	for word in target:
		matches = re.findall(word, content)
		result.write(word, target , matches)
		print word, matches

print len(target)
now = date.today()
PDir = 'files/{}-{}-{}'.format(now.strftime('%Y'), now.strftime('%m'), now.strftime('%d'))

for filename in os.listdir(PDir):
	name = PDir + '/{}'.format( filename)
	F = open(name, 'r')
	cont = F.read()
	find(cont)

# find('digiato-2015-11-15.html')