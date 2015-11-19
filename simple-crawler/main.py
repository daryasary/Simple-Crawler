from crawl import Crawl 
from lists import sites, target
import os
from datetime import date


data = []

# Make a seperate dir everyday
now = date.today()
A = 'files/{}-{}-{}'.format(now.strftime('%Y'), now.strftime('%m'), now.strftime('%d'))
if not os.path.exists(A):
	os.makedirs(A)

# Crawl sites:
for site in sites:
	data.append(Crawl(site))

# Show count of crawled site character
for d in data:
	print 'is ', len(d)
