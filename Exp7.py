while True:
    A = int(input('Enter a non-negative integer less than or equal to 1000:'))
    if A>=0 and A<=1000:
        break
    else:
        print('Invalid entry.')

alist = list()
blist = list()

a=b=flag=0

for b in range (1,A):
    for a in range (1,b):
        if (a**2 + b**2 == A):
            alist.append(a)
            blist.append(b)
            flag = 1

size = len(blist)

for i in range (0,size):
    print(f" [{alist[i]},{blist[i]}]")

if flag == 0:
    print(f"\n No such pair of (a,b) satisfy pythagoras' theorem upto {A}")
