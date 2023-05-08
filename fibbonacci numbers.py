def fibbo(n):
    if n==1:
        return n
    elif n==0:
        return n
    else:
        return fibbo(n-1)+fibbo(n-2) 
n=int(input(('enter range n of fibbonacci numbers')))
fibs=[]
for i in range (n):
    h=fibbo(i)
    fibs.append(h)
print (fibs)
A=int(input('enter number A'))
B=int(input('enter number B'))
if A  and B in fibs and abs(B-A)<B and A:
    print('the numbers are  neighbours in fibbonacci series ') 
else:
    print('the numbers are not neighbours in fibbonacci series ')
    
    
