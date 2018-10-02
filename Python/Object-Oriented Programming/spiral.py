
'''Python 3 Code for the align numbers up to n^2 in a spiral challenge.
The output layout can be slighthly changed by setting another character as SPACINGSYMB.
-nighmared'''
NUMBER = int(input('Base: '))
SPACINGSYMB = ' ' #Symbol used to align the output better
print('{}\n'.format(NUMBER))
def makepowlist(n):return(list(range(1,(n**2)+1)))
def makelist(n,rev=False):return((list(range(n))).reverse() if rev else list(range(n)))
class matrix(list):
    def __init__(self,n,makeindex=True):
        self.n = n
        self.numbrl = len(str(self.n**2))
        self.powl = makepowlist(self.n)
        self.matrix = [None]*n
        self.plan = buildplan(self.n)
        for y in self.matrix:self.matrix[self.matrix.index(y)] = [None]*n
        if makeindex:
            for y in self.matrix:
            	for x in range(len(y)):self.matrix[self.matrix.index(y)][x] = [self.matrix.index(y)+1,x+1]
    def __repr__(self):
        retstr = ''
        for row in self.matrix:
            for e in row:retstr+='{} '.format(e)
            if row != self.matrix[-1]:retstr+='\n'
        return(str(retstr))
    def spiral(self,plan):
        for e in plan:
            i = str(self.powl.pop(-1))
            if len(i)!=self.numbrl:
                if (self.numbrl-len(i))%2==0:i = '{0}{1}{0}'.format(int((self.numbrl-len(i))*0.5)*SPACINGSYMB,i)
                else:i= ((self.numbrl-len(i))*SPACINGSYMB)+i
            self.matrix[e[0]][e[1]] = i
def buildplan(n):
    xnull=ynull=x=y=0
    round,L,fL,cn,even=1,len(makepowlist(n)),[],n-1,bool
    if n%2==0:deadx,deady,even = int((n/2)-1),int(n/2),True
    else:deadx,deady,even = int((n-1)/2),int((n-1)/2),False
    while L>0:
        if cn<1 or L<1:break
        x,y=xnull,ynull
        while x<cn: #move cursor right
            fL.append((y,x))
            if (y,x) == (deady,deadx):break
            x,L=x+1,L-1
        while y<cn: #move cursor down
            fL.append((y,x))
            if (y,x) == (deady,deadx):break
            y,L=y+1,L-1
        while x>xnull: #move cursor left
            fL.append((y,x))
            if (y,x) == (deady,deadx):break
            x,L=x-1,L-1
        xnull+=1
        while y>ynull: #move cursor up
            fL.append((y,x))
            if (y,x) == (deady,deadx):break
            y,L=y-1,L-1
        ynull+=1
        cn = cn-1
    if not even:fL.append((deady,deadx))
    return fL
MATRIX = matrix(NUMBER)
MATRIX.spiral(MATRIX.plan)
print(MATRIX)