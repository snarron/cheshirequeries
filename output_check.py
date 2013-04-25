import BeautifulSoup as bs
from collections import Counter

PATH = "/Users/shoheinarron/Sites/github/cheshirequeries/Group1_C3/"
FILE = ["C3_Group_output.txt", "MINI_TREC_QRELS.txt"]

for i in FILE:
	soup = bs.BeautifulSoup(open(PATH+i, 'rt').read())

	ft_loc = []
	for line in str(soup).split('\n'):
		ft_loc.append(line.strip()[6:11])

	ft_counter = Counter(ft_loc)
	print i
	for q in ft_counter:
		print q, ":", ft_counter[q]