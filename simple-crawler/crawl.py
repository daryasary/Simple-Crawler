import urllib
import timeit
from datetime import date
from urlparse import urlparse

def save_output(text, name):
	now = date.today()
	name = 'files/{}-{}-{}/{}-{}-{}-{}.html'.format(now.strftime('%Y'), now.strftime('%m'), now.strftime('%d'), name, now.strftime('%Y'), now.strftime('%m'), now.strftime('%d'))
	out = open(name, 'w') 
	out.write(text)

def site_name(site):
	S = urlparse(site)
	name = S.netloc.split('.')[0]
	return name

def Crawl(site):
	start = timeit.default_timer()
	content = urllib.urlopen(site).read()
	stop = timeit.default_timer()
	print '%s done in %d seconds' % (site, (stop - start))
	name = site_name(site)
	save_output(content, name)
	return content

