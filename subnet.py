import math
class subnet:
    def __init__(self,ip):
        self.ip=ip
        self.clas=self.findclass(self.ip)
    def findclass(self,ip):
        for i in range(4):
            if ip[i]==".":
                fip=int(ip[0:i])
        if fip<=127:
            return 1
        elif fip<=191:
            return 2
        elif fip<=223:
            return 3
        else:
            return 4
    def conv(self,li):
        s=""
        for i in range(4):
            s=s+str(li[i])+"."
        return s[:-1]
    def submask(self,nosb):
        mask=[255,255,255,255]
        i=256-2**(8-nosb)
        mask[self.clas]=i
        for j in range(self.clas+1,4):
            mask[j]=0
        return self.conv(mask)
    def first_last_ip(self,i,binip,nosb,s='0',broad=False):
        sr=""
        if self.clas == 3:
            if broad==True:
                sr = bin(i)[2:].zfill(nosb) + bin(2 ** (8 - nosb)-1)[2:]
                binip[3]=int(sr,2)
                return self.conv(binip)
            if s == '0':
                sr = bin(i)[2:].zfill(nosb) + bin(1)[2:].zfill(8 - nosb)
            elif s == '1':
                sr = bin(i)[2:].zfill(nosb) + bin(2 ** (8 - nosb) - 2)[2:]
            binip[3] = int(sr, 2)
            return self.conv(binip)
        sr=bin(i)[2:].zfill(nosb)+s*(8-nosb)
        binip[self.clas]=int(sr,2)
        for j in range(self.clas + 1, 3):
            sr = s * 8
            binip[j] = int(sr, 2)
        if broad==True:
            binip[3]=255
            return self.conv(binip)
        if s=='0':
            binip[3]=1
            return self.conv(binip)
        elif s=='1':
            binip[3]=254
            return self.conv(binip)
    def subnet(self,ip,nos=8):
        binip=[]
        subnet={}
        ix=0
        k=self.clas
        nosb=int(math.log(nos,2))
        for i in range(len(ip)):
            if ip[i]==".":
                binip.append(int(ip[ix:i]))
                ix=i+1
        binip.append(int(ip[ix:]))
        for i in range(self.clas,4):
            binip[i]=0
        for i in range(nos):
            subnet[i+1]=[]
            binip[k]=(2**(8-nosb))*i
            subnet[i+1].append({"Sub Network Address":self.conv(binip)})
            subnet[i+1].append({"First Ipv4 Address:":self.first_last_ip(i,binip,nosb,'0')})
            subnet[i + 1].append({"Last Ipv4 Address:": self.first_last_ip(i, binip, nosb, '1')})
            subnet[i + 1].append({"BroadCast Address:": self.first_last_ip(i, binip, nosb, '1',broad=True)})
            subnet[i+1].append({"Subnet Mask":self.submask(nosb)})
            if self.clas!=3:
                binip[3]=0
        for k,v in subnet.items():
            print("SUB NETWORK {0}".format(k))
            for it in v:
                print(it)
ip=""
nos=int(input("Enter no of physical networks"))
noh=int(input("Enter no of host per each network"))
def choose(nos,noh):
    global ip
    nosb=math.log(nos)
    th1=th2=th3=-1
    th='A'
    if 2**(24-nosb)>=noh:
        th1=noh/2**(24-nosb)
        print("class A is feasible with throughput {0}".format(th1))
        ip="61.0.228.11"
    if 2**(16-nosb)>=noh:
        th2 = noh / 2 ** (16 - nosb)
        print("class B is feasible with throughput {0}".format(th2))
        if th2>th1:
            th='B'
            ip="172.30.12.1"
    if 2 ** (8 - nosb) >= noh:
        th3 = noh / 2 ** (8 - nosb)
        print("class C is feasible with throughput {0}".format(th3))
        if th3>th2:
            th='C'
            ip="192.168.43.1"
    li=[th1,th2,th3]
    print("Max throughput is available through class {0}".format(th))
choose(30,2000)
obj=subnet(ip)
#obj=subnet("192.168.10.0")
obj.subnet(obj.ip,nos=nos)