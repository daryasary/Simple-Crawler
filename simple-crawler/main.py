from crawl import Crawl 
from lists import sites, targets
import os
from datetime import date
from parse import find


# data = []
data = {}
# To store sites that not resonding on time
lost = []
# Make a seperate dir everyday
now = date.today()
directory = 'files/{}-{}-{}'.format(now.strftime('%Y'), now.strftime('%m'), now.strftime('%d'))
if not os.path.exists(directory):
	os.makedirs(directory)

# Crawl sites:
# for site in sites:
# 	content = Crawl(site)
# 	if content == site:
# 		lost.append(site)
# 	else:
# 		data[site] = content

print '##'* 4, '\n Fetching done!'

name = 'files/result-{}-{}-{}.txt'.format(now.strftime('%Y'), now.strftime('%m'), now.strftime('%d'))
result = open(name, 'w')
# Parse through files in archive
for filename in os.listdir(directory):
	name = directory + '/{}'.format(filename)
	F = open(name, 'r')
	cont = F.read()
	find(cont, filename, result)

print >> result, 'lost sites: {}'.format(lost)
