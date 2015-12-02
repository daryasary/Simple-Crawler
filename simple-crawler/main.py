from crawl import Crawl 
from lists import sites, target
import os
from datetime import date


# data = []
data = {}

# Make a seperate dir everyday
now = date.today()
A = 'files/{}-{}-{}'.format(now.strftime('%Y'), now.strftime('%m'), now.strftime('%d'))
if not os.path.exists(A):
	os.makedirs(A)

# Crawl sites:
for site in sites:
	# data.append(Crawl(site))
	data[site] = Crawl(site)

# Show count of crawled site character
for k in data:
	print k, 'is ', len(data[k])
