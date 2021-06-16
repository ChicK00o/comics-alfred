def enabled():
	return True

def title():
	return "Dilbert"

def subtitle():
	return "View Dilbert's daily strip"

def run():
	import feedparser
	import os
	import pprint
	d = feedparser.parse('http://dilbert.com/fast')
	# pp = pprint.PrettyPrinter(indent=4)
	# pp.pprint([i[5:-1] for i in d['feed']['summary'].split() if i.find('assets.') > 0][0])
	print('done')
	strip = [i[5:-1] for i in d['feed']['summary'].split() if i.find('assets.') > 0][0]
	os.system('curl -s ' + strip + ' -o strip.png')
	# os.system('qlmanage -p strip.png')
