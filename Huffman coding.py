'''
HUFFMAN CODING
'''
import copy as c
import math as m
a=list(map(float,input("Enter the probabilities in spaces sepreated\t").split()))
#a=[0.4,0.2, 0.2, 0.1, 0.1]
#a=[0.8,0.5,0.5,0.2, 0.2, 0.1, 0.1]
a=sorted(a,reverse=True)
a=[[t,tt] for t,tt in enumerate(a)]
l=[c.deepcopy(a)]
for i in range(len(a)):
    p=a[-1][1]+a[-2][1];_p=a[-1][0]+a[-2][0]
    for y in range(len(a)):
        if(p>=a[y][1]):
            a.insert(y,[_p,p])
            break
    del a[-2:]
    l.append(c.deepcopy(a))
    if len(a)==1:
        break
pp=c.deepcopy(l)
for j in l:
    if j[0][1]==1.0:
        break
    j[-2:]=[[j[-2][0],j[-2][1],0],[j[-1][0],j[-1][1],1]]
def display():
    _=[0]
    le=len(l)+1
    print('\n')
    for g in range(len(l)):
        l[g].extend((le-len(l[g]))*_)
        pp[g].extend((le-len(pp[g]))*_)
    for _i in range(len(l)+1):
        for _j in range(len(l)):
        	print(l[_j][_i],end='   ')
        print('\n')

ff=pp[0]
code=[]
for f in ff: #for probability with index 
    c=[]
    n=1
    s=1
    for i in l:# for the over all elements in l
        co=''
        for j in i: 
            if(len(j)==3 and (f[0]==j[0])):
                co+=str(j[2])
                if(len(j)==3 and j[2]==1):
                    s=[j[0]+i[i.index(j)-n][0],j[1]+i[i.index(j)-n][1]]
                elif(len(j)==3):
                    s=[j[0]+i[i.index(j)+n][0],j[1]+i[i.index(j)+n][1]]
                while 1:
                    if(len(i)==1):
                        break
                    for i in l:
                        for j in i:
                            if(s==j[:2] and len(j)==3):
                                co+=str(j[2])
                                if(len(j)==3 and j[2]==1):
                                    s=[j[0]+i[i.index(j)-n][0],j[1]+i[i.index(j)-n][1]]
                                elif(len(j)==3):
                                    s=[j[0]+i[i.index(j)+n][0],j[1]+i[i.index(j)+n][1]]
                    c.append(co)
    if(len(c)>1):
        code.append([c[0]])
    else:
        code.append(c)
cl=[]
for y in code:
    cl.append(len(y[0]))
al=sum([round(float(pp[0][x][1]*cl[x]),1) for x in range(len(pp[0]))])
h=sum([round(float(pp[0][x][1])*m.log(1/pp[0][x][1],2),5) for x in range(len(pp[0]))])
ef=int((h/al)*100)
display()
print("code word ",*code)
print("code length ",*cl)
print("Efficiency ",ef)
