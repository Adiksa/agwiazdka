import math
def wyswietl(a):
    for i in range(len(a)):
        for j in range(len(a[i])):
            print(a[i][j]+" ",end="")
        print("")
def zawiera(y,x,lista):
    for i in range(len(lista)):
        if(lista[i].x==x and lista[i].y==y):
            return 1
    return 0

class punkt:
    def __init__(self,ypoz,xpoz,val,gg):
        self.x = xpoz;
        self.y = ypoz;
        self.end=0;
        if(val=='k'):
            self.end=1
        self.g = gg;
        self.h = math.sqrt(math.pow(int(self.x-19),2)+math.pow(int(self.y)-19,2))
        self.f = self.g + self.h
plik = open('grid.txt')
b = plik.read()
tab = b.split("\n")
for i in range(len(tab)):
    tab[i] = tab[i].split(" ")
tab.reverse()
tab[19][19] = "k";
start = punkt(0.0,0.0,tab[0][0],0.0)
open = []
close = []
open.append(start)
while (1):
    obecny = open[0]
    for i in range(len(open)):
        if (open[i].f < obecny.f):
            obecny = open[i]
    close.append(obecny)
    open.remove(obecny)
    if (obecny.end == 1):
        break
    if(obecny.y+1<20):
        if(tab[int(obecny.y+1)][int(obecny.x)] != '5' and zawiera(obecny.y+1,obecny.x,close)==0):
            if(zawiera(obecny.y+1,obecny.x,open)==0):
                temp = punkt(obecny.y+1,obecny.x,tab[int(obecny.y+1)][int(obecny.x)],float(obecny.g)+1.0)
                temp.parent = obecny;
                open.append(temp);
    if (obecny.y - 1 >= 0):
        if (tab[int(obecny.y - 1)][int(obecny.x)] != '5' and zawiera(obecny.y - 1, obecny.x, close) == 0):
            if (zawiera(obecny.y - 1, obecny.x, open) == 0):
                temp = punkt(obecny.y - 1, obecny.x, tab[int(obecny.y - 1)][int(obecny.x)], float(obecny.g)+1.0)
                temp.parent = obecny;
                open.append(temp);
    if (obecny.x + 1 <20):
        if (tab[int(obecny.y)][int(obecny.x+1)] != '5' and zawiera(obecny.y, obecny.x+1, close) == 0):
            if (zawiera(obecny.y, obecny.x+1, open) == 0):
                temp = punkt(obecny.y, obecny.x+1, tab[int(obecny.y)][int(obecny.x+1)], float(obecny.g)+1.0)
                temp.parent = obecny;
                open.append(temp);
    if (obecny.x- 1 >= 0):
        if (tab[int(obecny.y)][int(obecny.x-1)] != '5' and zawiera(obecny.y , obecny.x-1, close) == 0):
            if (zawiera(obecny.y, obecny.x-1, open) == 0):
                temp = punkt(obecny.y, obecny.x-1, tab[int(obecny.y)][int(obecny.x-1)], float(obecny.g)+1.0)
                temp.parent = obecny;
                open.append(temp);
    if(len(open)==0):
        break
if(len(open)==0):
    print("Brak rozwiazania")
else:
    temp = close.pop()
    while (1):
        if (temp.x == 0 and temp.y == 0):
            break;
        xp = temp.x
        yp = temp.y
        temp = temp.parent
        if (temp.x == xp):
            if (temp.y > yp):
                tab[int(temp.y)][int(temp.x)] = 'd'
            else:
                tab[int(temp.y)][int(temp.x)] = 'g'
        else:
            if (temp.x > xp):
                tab[int(temp.y)][int(temp.x)] = 'l'
            else:
                tab[int(temp.y)][int(temp.x)] = 'p'
    tab.reverse()
    wyswietl(tab)
    plik.close()