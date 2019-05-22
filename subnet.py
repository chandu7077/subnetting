import math
nos=int(input("enter no of networks::"))
noh=int(input("enter no of hosts per each network::"))
def choose(nos,noh):
    tp1,tp2,tp3=-1,-1,-1
    nosb=math.ceil(float(math.log(nos,2)))
    print("subnet bits:",nosb)
    if nosb<=24 and noh<=2**(24-nosb):
        tp1=(nos*noh)/2**(24-nosb)
    if nosb<=16 and noh<=2**(16-nosb):
        tp2=(nos*noh)/2**(16-nosb)
    if nosb<=8  and noh<=2**(8-nosb):
        tp3=(nos*noh)/2**(8-nosb)
    tp=[tp1,tp2,tp3]
    mx=0
    for i in range(1,len(tp)):
        if tp[i]>mx:
            mx=i
    return mx+1,tp[mx]
cls,tph=choose(nos,noh)
print("class {0} gives high throughput of {1} ".format(cls,tph))
ips=["61.0.0.0","172.30.0.0","212.110.1.0"]
ids=[24,16,8]
ip=ips[cls-1]
lip=ip.split(".")
binip=[]
for i in range(0,4):
    lip[i]=int(lip[i])
    binip.append(bin(lip[i])[2:].zfill(8))
bits=[]
def forma(binsip):
    binip="".join(binsip)
    ip=""
    j=0
    for i in range(0,4):
        ip+=str(int(binip[j:j+8],2))+"."
        j=j+8
    return ip[:-1]
nosb=math.ceil(float(math.log(nos,2)))
for i in range(0,nos):
    bits.append(bin(i)[2:].zfill(nosb))
for i in range(nos):
    print("SUBNETWORK {0}:".format(i+1))
    print("-"*120)
    binsip="".join(binip)
    binsip=list(binsip)
    for j in range(cls*8,cls*8+nosb):
        binsip[j]=bits[i][j-cls*8]
    print("SUBNET ADDRESS:",forma(binsip))
    binsip=list(binsip)
    binsip[-1]="1"
    print("FIRST ADDRESS:",forma(binsip))
    for j in range(cls*8+nosb,32):
        binsip[j]="1"
    binsip[-1]="0"
    print("LAST ADDRESS:",forma(binsip))
    binsip=list(binsip)
    for j in range(cls*8+nosb,32):
        binsip[j]="1"
    print("BROADCAST ADDRESS:",forma(binsip))
    binsip=list(binsip)
    for j in range(0,cls*8+nosb):
        binsip[j]="1"
    for j in range(cls*8+nosb,32):
        binsip[j]="0"
    print("SUBNET MASK:",forma(binsip))
    print("NO OF HOSTS PER SUBNET:",2**(ids[cls-1]-nosb))
    print("-"*120)
