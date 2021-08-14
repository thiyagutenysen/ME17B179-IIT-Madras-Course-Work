#ME17B179
#Chella Thiyagarajan
class BinaryNumber:
    def __init__(self,list):
        self.list=list
        for i in self.list:
            if i!=0 and i!=1:
                print("...")
    def __str__(self):
        num=""
        for i in range(len(self.list)-1,-1,-1):
            num=num+str(self.list[i])
        return "["+num+"]_2"
    def value(self):
        k=0
        num=0
        for i in self.list:
            num=num+(i*(2**k))
            k=k+1
        return num