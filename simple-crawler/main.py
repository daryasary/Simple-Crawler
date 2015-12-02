from crawl import Crawl 
from lists import sites, target
import os
from datetime import date
from parse import find


# data = []
data = {}

# Make a seperate dir everyday
now = date.today()
directory = 'files/{}-{}-{}'.format(now.strftime('%Y'), now.strftime('%m'), now.strftime('%d'))
if not os.path.exists(directory):
	os.makedirs(directory)

# Crawl sites:
for site in sites:
	# data.append(Crawl(site))
	data[site] = Crawl(site)

print '##'* 4, '\n Fetching done!'

name = 'files/result-{}-{}-{}.txt'.format(now.strftime('%Y'), now.strftime('%m'), now.strftime('%d'))
result = open(name, 'w')
# Parse through files in archive
for filename in os.listdir(directory):
	name = directory + '/{}'.format(filename)
	F = open(name, 'r')
	cont = F.read()
	find(cont, filename, result)
