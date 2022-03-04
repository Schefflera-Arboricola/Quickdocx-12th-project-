#samples
import csv
f=open('samples.csv','w',newline='')  #file will contain all samples' names,locations and variables in them
wo=csv.writer(f)  #Writer object
ro=csv.reader(f)     #Reader object
h=('filename','filelocation','variables')
x=('health check up authorisation letter',r'C:\Users\Admin\Desktop\quickdocx\sample\health check up authorisation letter.docx',{1:'Name '})
y=('FORM 24',r'C:\Users\Admin\Desktop\quickdocx\sample\FORM 24.docx',{1:'File number ',2:'Year ',3:'Name',4:'Date of birth',5:'Number of years',6:'Number of months',7:'Number of days',8:'Last date of service',9:'First day of service '})
z=('exam intimation',r'C:\Users\Admin\Desktop\quickdocx\sample\exam intimation.docx',{1:'Diary number',2:'Date',3:'Name',4:'Branch where working',5:'UPSC/SSC',6:'Name of board',7:'Advertisement number',8:'advertisement date'})
wo.writerow(h)  #adding rows in csv file
wo.writerow(x)
wo.writerow(y)
wo.writerow(z)

f.close()


#user manual
import pickle
f=open('help.dat','wb')   #file of user manual
st='''Help

Required packages : docx , os , pickle , csv

Before using : Run the samples.py program in python IDLE to install in built samples and user manual. Don’t delete or open the files created, in the folder, after executing the program. 

How to use the program : 

1.  Put files quickdocs.py and samples.py and folder sample   in a folder on desktop and run samples.py .

2.	Make a sample docfile by writing  {n{  in place of variable characters . 
Here n is a number , assigned to the variable characters. For first variable character(s), n would be 1,
For second variable character(s), n would be 2,
For third variable character(s), n would be 3 ,...and so on.

These numbers would be used for further occurrences, in the document also , in the above syntax only. You can refer to the in built samples for more clarity. Skip , if want to use in built samples only.

3.	Run the program quickdocs in python IDLE . A menu would be displayed. By entering : 

a.	0 : the program will end.
b.	1 : a series of menus would appear to help you create your document from the sample. It would iterate until the necessary character(s) to stop the process is/are not entered.   
c.	2 : a series of menus would appear to help you create your own ,new sample.
d.	3 : the names of all the existing samples with there location would be shown . 
e.	4 : a series of menus would appear to help you delete an already existing sample’
f.	Otherwise , this ‘help’ section would appear.

4.	The docfile, once created would be in the folder in point no. 1 and can be removed from the folder.

5.	If you change the position of a user created sample, then to change the address , the sample would have to be deleted and created again with the different address. It would  appear in the list of names of samples but would give an error when you would try to create a file.
 '''
pickle.dump(st,f) #adding st in file
f.close()
