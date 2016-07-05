from pdfminer.pdfinterp import PDFResourceManager, PDFPageInterpreter#process_pdf
from pdfminer.pdfpage import PDFPage
from pdfminer.converter import TextConverter
from pdfminer.layout import LAParams

from PyPDF2 import PdfFileWriter, PdfFileReader
import subprocess

paras=[]
para=''

def extracttext():
	with open('pdftotext.txt') as f:
	    content = f.readlines()
	para=''
	
	for a in content:
		a=a.strip()
		a=a.lower()
		para=para+'\n'+a
		if len(str(a))>1:
			if a[-1]=='.':
				
				paras.append(para)
				para=''
			
def consult_pdftotext(filename):
    '''
    Runs pdftotext to extract text of pages 1..3.
    Returns the count of characters received.

    `filename`: Name of PDF file to be analyzed.
    '''
    
    # don't forget that final hyphen to say, write to stdout!!
    i=1
    while i<=1:
	    cmd_args = [ "pdftotext", "-f",str(i), "-l", "3", filename, "pdftotext.txt" ]
	    pdf_pipe = subprocess.Popen(cmd_args, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
	    extracttext()
	    i=i+1
	   
def calculate(para):
	paralist=para.splitlines()
	
	avg=0
	ct=0
	for line in paralist:
		if len(line)>50:
			avg=avg+len(line)
		else:
			ct=ct+1
	avg=avg/float(len(paralist)-ct)
	return avg

def average(paras):
	ave=0
	for a in paras:
		if ave==0:
			ave=calculate(a)
		else:
			ave=(int(ave)+int(calculate(a)))/2.0
	return ave

consult_pdftotext("data.pdf")

avg=average(paras)

i=0


while i<len(paras)-1:
	paralist=paras[i].splitlines()
	x=paralist[-1]
	

	
	if len(x)>avg:
		paras[i:i+2] = [''.join(map(str,paras[i:i+2]))]
		i=i-1
	
	i=i+1


query=['python']
maxct=0
index=0
ct=0
for a in paras:
	print a
	ct=0
	
	for x in query:
		if x in a:
			print str(a)+'\n'+x
			ct=ct+a.count(x)
	if ct>maxct:
		maxct=ct
		index=a
	
	
		
print index 
print maxct


