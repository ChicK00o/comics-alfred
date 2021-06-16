from pprint import pprint


def enabled():
	return True

def title():
	return "Calvin and Hobbes"

def subtitle():
	return "View Calvin's adventures with good old Hobbes"

def run():
	import feedparser
	# import re
	import os
	# import pprint
	d = feedparser.parse('https://www.comicsrss.com/rss/calvinandhobbes.rss')
	# pp = pprint.PrettyPrinter(indent=4)
	# pp.pprint(d['entries'][0]['summary_detail']['value'].split())
	# print("done")
	strip = [i[5:-1] for i in d['entries'][0]['summary_detail']['value'].split() if i.find('assets.') > 0][0]
	# strip = re.match(r'<img[^>]*\ssrc="(.*?)"' , d['entries'][0]['summary_detail']['value'], re.IGNORECASE).groups(0)[0]
	# tweak, must be done by tumblr I suppose
	# strip = strip.replace("_500.gif", "_1280.gif")
	os.system('curl -s ' + strip + ' -o strip.png')
	# os.system('qlmanage -p strip.png')
