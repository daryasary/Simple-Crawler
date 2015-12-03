# sites = [
# 	# Write your prefered site(s) here
# 	'http://digiato.com',
# 	# 'http://Cnet.com',
# 	# 'http://stackoverflow.com',
# 	'http://1pezeshk.com',
# 	# 'http://ramezanpour.me',
# ]

sites = open('sites.txt', 'r')
sites = sites.read()
sites = sites.split('\n')



# Write youe Keyword(s) in targets.txt file
# Each keyword in seperate line
targets = open('targets.txt', 'r')
targets = targets.read()
targets = targets.split('\n')
# word = [word.append(target.readline) for line in len(target)]


