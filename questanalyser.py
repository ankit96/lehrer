import cPickle
f=open('cprogramming.txt','r')
train_text=f.readlines()
cpparas=cPickle.load(open('cprogramming.p', 'rb'))
def statistics(x):
	
	   dic={}
	   y=[]
	   for b in x:
		   y=y+b.split()
	   for i in y:
	       if not i in  dic:        #Python 2.7: if not dic.has_key(x):
		  dic[i] = train_text.count(i)
	   return dic
def searchinparas(string,y):
	#print '---------------------------------------------'
	b=string.split()
	#print "b  --> "+str(b)
	#print "x  --> "+str(y)
	for a in y:
		#print "a ->"+str(a)
		if a in b:
			#print "Hello"
			return 1
		
	return 0
def search(sample_text,tokens,parsed_tree,x):
	i=0
	for a in cpparas:
		ct=0
		y=[]
		a1=a.split()
		for b in x:
			y=y+b.split()
		for b in y:
			if b in a1 or b[:-1] in a1:
				
				ct=ct+1
				i=i+1
			
		
		if ct>=1 :
			
			print "-----------------------------------------------------------------------"
			
			
			smallparas=[]
			small=''
			a1=a.split('\n\n')
			
			#print str(a1)
			for line in a1:
				
				
				if searchinparas(line,y):
					smallparas.append(line)
				
				
			
			print str(smallparas)
		
			print "-----------------------------------------------------------------------"
			ct=0
			
			
		
		
		#print a
		
			

					
	
def questiswhat(sample_text,tokens,parsed_tree,x):
	print "modifier : "+str(tokens[0])
	print sample_text
	print parsed_tree
     	print str(x[0])
	
     	stats = statistics(x)
     	print str(stats) 
     	search(sample_text,tokens,parsed_tree,x)
     	

     	
