import cPickle
f=open('cprogramming.txt','r')
train_text=f.readlines()
cpparas=cPickle.load(open('cprogramming.p', 'rb'))
def search(sample_text,tokens,parsed_tree,x):
	
	for a in cpparas:
		ct=0
		y=[]
		for b in x:
			y=y+b.split()
		for b in y:
			
			if b in a or b[:-1]:
				ct=ct+1
		if ct>1:
			print str(a)
			print ""
		break
			
				
	
def questiswhat(sample_text,tokens,parsed_tree,x):
	
	print "modifier : "+str(tokens[0])
	print sample_text
	print parsed_tree
     	print str(x[0])
     	
     	search(sample_text,tokens,parsed_tree,x)
     	

     	