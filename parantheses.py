def is_valid(s):
    n = -1
    while (len(s) > n):
        n = len(s)
        s = s.replace('()','')
    if len(s) == 0:
        return True
    else:
        return False

def isValid(string):
    n=len(string)
    i=0
    bal=0
    while(i<n):
        if string[i]==')':
            if bal<1:
                return False
            bal-=1
        elif string[i]=='(':
            bal+=1
        i+=1  
    return bal==0

s = "()())("
print(is_valid(s))
print(isValid(s))
