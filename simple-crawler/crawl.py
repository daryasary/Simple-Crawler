import urllib
import timeit
from datetime import date
from urlparse import urlparse

def save_output(text, name):
	now = date.today()
	name = 'files/{}-{}-{}/({})-{}-{}-{}.html'.format(now.strftime('%Y'), now.strftime('%m'), now.strftime('%d'), name, now.strftime('%Y'), now.strftime('%m'), now.strftime('%d'))
	out = open(name, 'w') 
	out.write(text)

def site_name(site):
	S = urlparse(site)
	name = S.netloc
	return name

def Crawl(site):
	start = timeit.default_timer()
	try:
		content = urllib.urlopen(site).read()
		stop = timeit.default_timer()
		print '{} done in {} seconds and is {}'.format(site, int(stop - start), len(content))
		name = site_name(site)
		save_output(content, name)
		return content
	except:
		return None

