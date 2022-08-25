def myfile():
    try:
        c=open('D:\Raviteja\pythonProject1\ ravi.txt','r')
        print(c.read())
    except(FileNotFoundError):
        return ('not exists')
emp=myfile()
print(emp)