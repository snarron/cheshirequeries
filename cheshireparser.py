import BeautifulSoup as bs
import re
from nltk.corpus import stopwords
import string
import inflect

PATH = '/Users/shoheinarron/Sites/github/cheshirequeries/transformedQueries.xml'
soup = bs.BeautifulSoup(open(PATH, 'rt').read())

tags = ['num', 'title', 'desc', 'narr']

def find_top_tag(soup, tags):
	initial_list = {}
	counter = 0
	for root in soup.findAll('top'):
		initial_list[counter] = root.contents
		counter += 1
	return initial_list

def query_cleanup(top_tag_dict):
	counter = 0
	cleaner_list = []
	str_list = []
	while counter < len(top_tag_dict):
		for i in top_tag_dict[counter]:
			str_list.append([item.strip() for item in filter(None, str(i).split('\n'))])
			#print [item.strip() for item in filter(None, str(i).split('\n'))]
		counter += 1
	for i in str_list:
		if i == []:
			pass
		else:
			cleaner_list.append(i)
	return cleaner_list

def tag_loop(query_line_list_by_tag):
	line_list = []
	for i in query_line_list_by_tag:
		line_list.append(' '.join(i)[:].split())
	return line_list
		#print ' '.join(i)[:].split()
		#if tag == 'num':
		#	print ' '.join(i)[:].split()
		#	pass
		#elif tag == 'title':
		#	print ' '.join(i)[:].split()
		#	pass
		#elif tag == 'desc':
		#	print ' '.join(i)[:].split()
		#	pass
		#elif tag == 'narr':
		#	print ' '.join(i)[:].split()
		#	pass
		#else:
		#	pass

def group_query(line_list):
	query_group = {}
	i = 0
	q = 0
	while i < len(line_list):
		if line_list[i][0] == "<num>":
			query_group[q] = line_list[i:i+4]
		else:
			pass
		#print i
		i += 4
		q += 1
	return query_group



def make_query(pre_query_dict, query_number):
	#query = "dc.title"
	p = inflect.engine()
	query = ""
	query_base = pre_query_dict[query_number]
	#print query_base
	query_num, query_title, query_desc, query_narr = query_base[:4]
	query_num = [w.translate(string.maketrans("","").lower(), string.punctuation) for w in query_num[1:-1] if not w in stopwords.words('english')]
	query_title = [w.translate(string.maketrans("","").lower(), string.punctuation) for w in query_title[1:-1] if not w in stopwords.words('english')]
	query_desc = [w.translate(string.maketrans("","").lower(), string.punctuation) for w in query_desc[2:-1] if not w in stopwords.words('english')]
	query_narr = [w.translate(string.maketrans("","").lower(), string.punctuation)  for w in query_narr[2:-1] if not w in stopwords.words('english')]
	query_num[0], query_title[0], query_desc[0] = query_num[0].lower(), query_title[0].lower(), query_desc[0].lower()
	#print query_base
	#print query_num
	#print query_title
	#print query_desc
	#print query_narr
	#print query_number
	for q in query_desc:
		if q == query_desc[0]:
			if (q in query_narr) and (q in query_title):
				#query = query + ' any ' + q + ' and '
				query = query + q + ' and '
				#print "both"
			elif (q in query_narr):
				#query = query + ' any ' + q + ' or '
				query = query + q + ' or '
				#print "narr"
			elif (q in query_title):
				#query = query + ' any ' + q + ' or '
				query = query + q + ' or '
				#print "title"
			else: # should never happen
				#query = query + ' any '
				pass
		else:
			if (q in query_narr) and (q in query_title):
				query = query + q + ' and '
				#print "both"
			elif (q in query_narr):
				query = query + q + ' or '
				#print "narr"
			elif (q in query_title):
				query = query + q + ' or '
				#print "title"
			else: # should never happen
				pass
	if query[-3:] == 'or ':
		query = query[:-3]
	elif query[-4:] == 'and ':
		query = query[:-4]
	return query

query_abstract = find_top_tag(soup, tags)
#print query_list
cleaner_abstract = query_cleanup(query_abstract)
#print cleaner_list
looped_tag = tag_loop(cleaner_abstract)
#print looped_tag
pre_query_dict = group_query(looped_tag)
#print pre_query_dict

i = 0
final_queries = {}
while i < len(pre_query_dict):
	print str(i) + ": " + make_query(pre_query_dict, i)
	i += 1

#query_list = make_query(pre_query_dict)
#print query_list