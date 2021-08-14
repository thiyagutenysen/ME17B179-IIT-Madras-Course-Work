# Homework header as usual
#
#
#

class Gene:
    
    """
        lass body with documentation
        nitialise the class, and define methods to calculate GC content, add 2 sequences, and find the complement of a strand
	 """
    def __init__(self,geneID,sequence):
        self.sequence=sequence
        self.geneID=geneID
        self.length=len(self.sequence)
    def __GC_content(self):
        k=0
        for i in self.sequence:
            if i=='G' or i=='C':
                k+=1
        per=(k/self.length)*100
        return per
    def dnasequence(self):
        return self.sequence
    def __add__(self,other):
        c=self.sequence+other.dnasequence()
        return Gene("DNA",c)
    def __neg__(self):
        compliment=''
        for i in self.sequence:
            if i=='A':
                compliment+="T"
            elif i=='G':
                compliment+="C"
            elif i=='T':
                compliment+="A"
            elif i=='C':
                compliment+="G"
        return compliment  
def GC_content(self):
    k=0
    for i in self.sequence:
        if i=='G' or i=='C':
            k+=1
    per=(k/self.length)*100
    return per

