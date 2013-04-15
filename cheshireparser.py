import BeautifulSoup as bs
import re
from nltk.corpus import stopwords
import string
import inflect

PATH = '/Users/shoheinarron/Sites/github/cheshirequeries/transformedQueries.xml'
soup = bs.BeautifulSoup(open(PATH, 'rt').read())

tags = ['num', 'title', 'desc', 'narr']

def isPlural(word):
	if len(word) > 3 and word[-1] == 's' and word[-2:] != 'ss':
		if word[-3:] == 'ies' or word[-2:] == "is":
			pass
		else:
			word = word[:-1]
	else:
		pass
	return word

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
	query_num = [w.translate(string.maketrans("","").lower(), string.punctuation) for w in query_num[1:-1]]# if not w in stopwords.words('english')]
	query_title = [w.translate(string.maketrans("","").lower(), string.punctuation) for w in query_title[1:-1]]# if not w in stopwords.words('english')]
	query_desc = [w.translate(string.maketrans("","").lower(), string.punctuation) for w in query_desc[2:-1]]# if not w in stopwords.words('english')]
	query_narr = [w.translate(string.maketrans("","").lower(), string.punctuation)  for w in query_narr[2:-1]]# if not w in stopwords.words('english')]
	query_num[0], query_title[0], query_desc[0] = query_num[0].lower(), query_title[0].lower(), query_desc[0].lower()
	
	#BEGIN AND
	and_list = []
	i = 0
	while i < len(query_desc)-2:
		#print query_desc[i]
		if (query_desc[i] in query_narr) and (query_desc[i+1] in query_narr) and (query_desc[i] not in stopwords.words('english')) and (query_desc[i+1] not in stopwords.words('english')):
			if (query_desc[i+2] in query_narr) and (query_desc[i+2] not in stopwords.words('english')):
				and_list.append(query_desc[i])
				and_list.append(query_desc[i+1])
				and_list.append(query_desc[i+2])
				#print str(query_desc[i:i+3])
			else:
				if query_desc[i-1] not in query_narr:
					and_list.append(query_desc[i])
					and_list.append(query_desc[i+1])
					#print str(query_desc[i:i+2])
				else:
					pass
		else:
			pass
		i += 1
	if (query_desc[-3] in query_narr) and (query_desc[-2] in query_narr):#(query_desc[-2] not in stopwords.words('english')) and (query_desc[-1] not in stopwords.words('english')):
		if query_desc[-1] in query_narr:
			and_list.append(query_desc[-1])
			and_list.append(query_desc[-2])
			and_list.append(query_desc[-3])
		else:
			and_list.append(query_desc[-2])
			and_list.append(query_desc[-3])
	# END AND
	#print and_list

	#BEGIN OR
	for q in query_desc:
		q = isPlural(q)
		#print q
		if (q not in stopwords.words('english')) and (q not in and_list):
			if (q in query_narr) and (q in query_title):
				query = query + ' and ' + q 
				#print "both"
			elif (q in query_narr):
				query = query + ' and ' + q
				#print "narr"
			elif (q in query_title):
				query = query + ' or ' + q
				#print "title"
			else: # should never happen
				pass
		else:
			pass
	#END OR

	for i in and_list:
		query = ' and ' + i + query
	
	#TRIM QUERY END
	if query[:4] == ' or ':
		query = query[4:]
	elif query[:5] == ' and ':
		query = query[5:]
	return query

query_abstract = find_top_tag(soup, tags)
#print query_list
cleaner_abstract = query_cleanup(query_abstract)
#print cleaner_list
looped_tag = tag_loop(cleaner_abstract)
#print looped_tag
pre_query_dict = group_query(looped_tag)
#print pre_query_dict

final_query = []
i = 0
final_queries = {}
while i < len(pre_query_dict):
	print str(401+i) + ": " + make_query(pre_query_dict, i) + ';'
	i += 1

#query_list = make_query(pre_query_dict)
#print query_list