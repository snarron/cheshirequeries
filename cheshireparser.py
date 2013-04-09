import BeautifulSoup as bs
import re

PATH = '/Users/shoheinarron/Desktop/transformedQueries.xml'
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
	while counter < len(query_dict):
		for i in query_dict[counter]:
			str_list = [item.strip() for item in filter(None, str(i).split('\n'))]
			print str_list

		counter += 1
#print [w for w in text if re.search('^[A-Z][a-z]+$', w)]

query_list = top_dict(soup, tags)
#print query_list
query_cleanup(query_list)