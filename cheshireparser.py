import BeautifulSoup as bs
import re

PATH = '/Users/shoheinarron/Sites/github/cheshirequeries/transformedQueries.xml'
soup = bs.BeautifulSoup(open(PATH, 'rt').read())

tags = ['num', 'title', 'desc', 'narr']

def top_dict(soup, tags):
	initial_list = {}
	counter = 0
	for root in soup.findAll('top'):
		initial_list[counter] = root.contents
		counter += 1
	return initial_list
#print initial_list
#print len(initial_list)

	#counter = 0
	#while counter < len(initial_list):
	#	print initial_list[counter]
	#	counter += 1

def query_cleanup(query_dict):
	counter = 0
	cleaner_list = []
	str_list = []
	while counter < len(query_dict):
		for i in query_dict[counter]:
			str_list.append([item.strip() for item in filter(None, str(i).split('\n'))])
			#print [item.strip() for item in filter(None, str(i).split('\n'))]
		counter += 1
	for i in str_list:
		if i == []:
			pass
		else:
			cleaner_list.append(i)
	return cleaner_list
#print [w for w in text if re.search('^[A-Z][a-z]+$', w)]

def tag_loop(cleaner_list, tag):
	for i in cleaner_list:
		if tag == 'num':
			print i[0].split()[1:-1]
		elif tag == 'title':
			print i[0].split()[1:-1]
		elif tag == 'desc':
			print i[0].split()[1:-1]
		elif tag == 'narr':
			print i[0].split()[1:-1]
		else:
			pass

def make_query():
	pass
query_list = top_dict(soup, tags)
cleaner_list = query_cleanup(query_list)
tag_loop(cleaner_list, 'title')