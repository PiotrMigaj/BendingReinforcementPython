fh = open("ZbrZgBaza//tablica.txt.", "r")
Tablica=fh.readlines()

count = len(Tablica)

#for i in range(count):
#   print(Tablica[i])

#print(Tablica[0].split(' ')[7])

count2=len(Tablica[0].split(' '))

n = 3
m = 4
Tablica2 = []
for i in range(count):
    Tablica2.append([0] * count2)

for i in range(count):
    for j in range(count2):
        Tablica2[i][j]=float(Tablica[i].split(' ')[j])

def InterpolacjaLin(x,x0,x1,y0,y1):
    h=x1-x0
    L=y0+(y1-y0)/h*(x-x0)
    return L

def znajdz(ni):
    tab=[0]*(count2-1)
    for i in range(count):
        if ni==Tablica2[i][0]:
            x=i
            for k in range(count2-1):
                tab[k]=Tablica2[x][k+1]

        elif ni>Tablica2[i][0]and ni<Tablica2[i+1][0]:
            x = i
            omega=InterpolacjaLin(ni,Tablica2[x][0],Tablica2[x+1][0],Tablica2[x][1],Tablica2[x+1][1])
            ksi=InterpolacjaLin(ni,Tablica2[x][0],Tablica2[x+1][0],Tablica2[x][2],Tablica2[x+1][2])
            dzeta = InterpolacjaLin(ni, Tablica2[x][0], Tablica2[x + 1][0], Tablica2[x][3], Tablica2[x + 1][3])
            ec2 = InterpolacjaLin(ni, Tablica2[x][0], Tablica2[x + 1][0], Tablica2[x][4], Tablica2[x + 1][4])
            es1 = InterpolacjaLin(ni, Tablica2[x][0], Tablica2[x + 1][0], Tablica2[x][5], Tablica2[x + 1][5])
            ss1 = InterpolacjaLin(ni, Tablica2[x][0], Tablica2[x + 1][0], Tablica2[x][6], Tablica2[x + 1][6])
            ss2 = InterpolacjaLin(ni, Tablica2[x][0], Tablica2[x + 1][0], Tablica2[x][7], Tablica2[x + 1][7])

            tab[0]=omega
            tab[1] = ksi
            tab[2] = dzeta
            tab[3] = ec2
            tab[4] = es1
            tab[5] = ss1
            tab[6] = ss2


    return tab







