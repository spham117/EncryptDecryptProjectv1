s = "      Hello World"
a = s.split(' ')[::-1]
k=0

for i in a:
    if i == ' ' and k<=len(a):
        k+=1
if a[k]==a[k+1] and a[k] == '' :
    print (len(a[k+2]))
else: 
    print('0')
h


        




