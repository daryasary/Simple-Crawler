import re
import os
from lists import target
from datetime import date



def find(content, filename, result):
	for word in target:
		matches = re.findall(word, content)
		# result.write(word, target , matches)
		# print word, matches
		if matches :
			R = '{} includes {}'.format(filename, word)
			print R
			print >>result, R


# print len(target)
# now = date.today()
# PDir = 'files/{}-{}-{}'.format(now.strftime('%Y'), now.strftime('%m'), now.strftime('%d'))



# find('digiato-2015-11-15.html')