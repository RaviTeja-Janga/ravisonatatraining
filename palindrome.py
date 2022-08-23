def ispalindrome(string):
    start,end=0,len(string)-1
    while(start<=end):
        if(string[start]!=string[end]):
            return False
        start+=1
        end-=1
    return True
print(ispalindrome('ntr'))
print(ispalindrome('rever'))