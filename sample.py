#samples
import csv
f=open('samples.csv','w+',newline='')
wo=csv.writer(f)
ro=csv.reader(f)
h=('filename','fileaddress','variables')
x=('health check up',r'C:\Users\Admin\Desktop\quickdocx\health check up.docx',{1:'Name '})
y=('FORM 24',r'C:\Users\Admibn\Desktop\quickdocx\FORM 24.docx',{1:'File number ',2:'Year ',3:'Name',4:'Date of birth',5:'Number of years',6:'Number of months',7:'Number of days',8:'Last date of service',9:'First day of service '})
z=('exam intimation',r'C:\Users\Admin\Desktop\quickdocx\exam intimation.docx',{1:'Diary number',2:'Date',3:'Name',4:'Branch where working',5:'UPSC/SSC',6:'Name of board',7:'Advertisement number',8:'advertisement date'})
wo.writerow(h)
wo.writerow(x)
wo.writerow(y)
wo.writerow(z)

f.close()


#documentation

f=open('documentation.dat','wb')
st=''' '''
