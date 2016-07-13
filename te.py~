from nltk.corpus import stopwords
from nltk.corpus import state_union
from nltk.tokenize import PunktSentenceTokenizer
import nltk
from nltk.tokenize import sent_tokenize, word_tokenize
import pprint
from stat_parser import Parser
import questanalyser
parser = Parser()



f=open('questions.txt','r')
cont=f.readlines()

f=open('cprogramming.txt','r')
train_text=f.readlines()
for sample_text in cont :
	if len(sample_text)<3:
		break
	

	parsed_tree =  parser.parse(sample_text)
	
	print ""
	np = [" ".join(i.leaves()) for i in parsed_tree.subtrees() if i.label() == 'NP']
	
	np_mwe_nocomma = [j for j in [" ".join(i.leaves()) for i in parsed_tree.subtrees() if i.label() == 'NP'] if j.count(' ') > 0 and j.count(',') == 0]
	x = []
	for i in sorted(np_mwe_nocomma, key=len):
	   	for j in x:
             		if j in i:
                     		continue
     		
     		x.append(i)
     	tokens = nltk.word_tokenize(sample_text)
	
     	if len(x)==1:#only one NP
     		
     		if tokens[0].strip()=="what" or tokens[0].strip()=="What":
     			questanalyser.questiswhat(sample_text,tokens,parsed_tree,x)
     		
	     		
	print("----------------------------------------------------------------------------")
	


