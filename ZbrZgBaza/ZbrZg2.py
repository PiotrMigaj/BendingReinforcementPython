fh = open("ZbrZgBaza//tablica2.txt.", "r")
#fh = open("tablica2.txt.", "r")
Tablica=fh.readlines()

count = len(Tablica)

#for i in range(count):
#   print(Tablica[i])


#print(Tablica[0].split(' ')[2])

count2=len(Tablica[0].split(' '))-1
#print(count2)

#n = 3
#m = 4
Tablica2 = []
for i in range(count):
    Tablica2.append([0] * count2)

for i in range(count):
    for j in range(count2):
        Tablica2[i][j]=float(Tablica[i].split(' ')[j])


#print(Tablica2[count-1][count2-1])






TabDD0=[0.05,0.10, 0.15, 0.20]
countTabDD0=len(TabDD0)

#print(countTabDD)

TabNIS=[0]*count

for i in range(count):
    TabNIS[i]=Tablica2[i][0]

TabDD005 = []
for i in range(count):
    TabDD005.append([0] * 2)

TabDD010 = []
for i in range(count):
    TabDD010.append([0] * 2)

TabDD015 = []
for i in range(count):
    TabDD015.append([0] * 2)

TabDD020 = []
for i in range(count):
    TabDD020.append([0] * 2)


for i in range(count):
    TabDD005[i][0]=Tablica2[i][1]
    TabDD005[i][1] = Tablica2[i][2]

for i in range(count):
    TabDD010[i][0]=Tablica2[i][3]
    TabDD010[i][1] = Tablica2[i][4]

for i in range(count):
    TabDD015[i][0]=Tablica2[i][5]
    TabDD015[i][1] = Tablica2[i][6]

for i in range(count):
    TabDD020[i][0]=Tablica2[i][7]
    TabDD020[i][1] = Tablica2[i][8]


#print(TabDD020)


TableDD=[0]*4
TableDD[0]=TabDD005
TableDD[1]=TabDD010
TableDD[2]=TabDD015
TableDD[3]=TabDD020


def ZnajdzDD(d2d):

    for i in range(len(TabDD0)):
        if d2d == TabDD0[i]:
            x=i
            x2=0
        elif d2d > TabDD0[i] and d2d < TabDD0[i+1]:
            x=i
            x2=1

    return [x,x2]

#IteratorDD = ZnajdzDD(0.05)
#print(IteratorDD[1])



def ZnajdzNI(ni):

    for i in range(len(TabNIS)):
        if ni == TabNIS[i]:
            x=i
            x2=0
        elif ni > TabNIS[i] and ni < TabNIS[i+1]:
            x=i
            x2=1

    return [x,x2]


def InterpolacjaLin(x,x0,x1,y0,y1):
    h=x1-x0
    L=y0+(y1-y0)/h*(x-x0)
    return L



def Wartosci(ni,d2d):
    IteratorDD = ZnajdzDD(d2d)
    IteratorNI = ZnajdzNI(ni)



    if IteratorDD[1] == 0:
        if IteratorNI[1] == 0:
            w1=TableDD[IteratorDD[0]][IteratorNI[0]][0]
            w2 = TableDD[IteratorDD[0]][IteratorNI[0]][1]
        else:
            w1=InterpolacjaLin(ni,TabNIS[IteratorNI[0]],TabNIS[IteratorNI[0]+1],TableDD[IteratorDD[0]][IteratorNI[0]][0],TableDD[IteratorDD[0]][IteratorNI[0]+1][0])
            w2 = InterpolacjaLin(ni, TabNIS[IteratorNI[0]], TabNIS[IteratorNI[0] + 1],
                                 TableDD[IteratorDD[0]][IteratorNI[0]][1], TableDD[IteratorDD[0]][IteratorNI[0] + 1][1])

    else:
        if IteratorNI[1] == 0:
            w1_0=TableDD[IteratorDD[0]][IteratorNI[0]][0]
            w1_1 = TableDD[IteratorDD[0]+1][IteratorNI[0]][0]
            w2_0 = TableDD[IteratorDD[0]][IteratorNI[0]][1]
            w2_1 = TableDD[IteratorDD[0]+1][IteratorNI[0]][1]
            w1=InterpolacjaLin(d2d,TabDD0[IteratorDD[0]],TabDD0[IteratorDD[0]+1],w1_0,w1_1)
            w2 = InterpolacjaLin(d2d, TabDD0[IteratorDD[0]], TabDD0[IteratorDD[0] + 1], w2_0, w2_1)
        else:
            w1_0 = TableDD[IteratorDD[0]][IteratorNI[0]][0]
            w1_1 = TableDD[IteratorDD[0] + 1][IteratorNI[0]][0]
            w2_0 = TableDD[IteratorDD[0]][IteratorNI[0]][1]
            w2_1 = TableDD[IteratorDD[0] + 1][IteratorNI[0]][1]
            w11 = InterpolacjaLin(d2d, TabDD0[IteratorDD[0]], TabDD0[IteratorDD[0] + 1], w1_0, w1_1)
            w21 = InterpolacjaLin(d2d, TabDD0[IteratorDD[0]], TabDD0[IteratorDD[0] + 1], w2_0, w2_1)

            w1_0 = TableDD[IteratorDD[0]][IteratorNI[0]+1][0]
            w1_1 = TableDD[IteratorDD[0] + 1][IteratorNI[0]+1][0]
            w2_0 = TableDD[IteratorDD[0]][IteratorNI[0]+1][1]
            w2_1 = TableDD[IteratorDD[0] + 1][IteratorNI[0]+1][1]
            w12 = InterpolacjaLin(d2d, TabDD0[IteratorDD[0]], TabDD0[IteratorDD[0] + 1], w1_0, w1_1)
            w22 = InterpolacjaLin(d2d, TabDD0[IteratorDD[0]], TabDD0[IteratorDD[0] + 1], w2_0, w2_1)

            w1 = InterpolacjaLin(ni, TabNIS[IteratorNI[0]], TabNIS[IteratorNI[0]+1], w11, w12)
            w2 = InterpolacjaLin(ni,TabNIS[IteratorNI[0]],TabNIS[IteratorNI[0]+1], w21, w22)






    return [w1,w2]


#print(Wartosci(0.405,0.075))
