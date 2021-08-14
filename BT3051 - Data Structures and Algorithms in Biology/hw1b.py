#BT3051 Assignment 1b
#Roll number: ME17B179
#Time: 4:15
import sys
import doctest

def read_FASTA(fname):
    """ (str) -> (list of tuples)
    # function body with documentation
    """
    sequence=""
    sequences=[]
    sequence_name=""
    file=open(fname,'r')
    for line in file:
        if line[0]=='>':
            sequences.append((sequence_name,sequence))
            sequence_name=line[1:-1]
            sequence=""
        else:
            sequence=sequence+line[:-1]
    else:
        sequences.append((sequence_name,sequence))
    sequences.pop(0)
    return sequences # a list of (sequence_name , sequence) tuples

def identify_orfs(dnaStrand):
    """ (str) -> (list of strings)
    # function body with documentation
    """
    reverse_compliment=""
    compliment=''
    for i in dnaStrand:
        if i=='A':
            compliment+="T"
        elif i=='G':
            compliment+="C"
        elif i=='T':
            compliment+="A"
        elif i=='C':
            compliment+="G"
    reverse_compliment = compliment[::-1]            
    frames=[]
    raw=[]
    for m in ([dnaStrand,reverse_compliment]):
        length=len(m)
        x=length%3
        raw.append(m[0:length-x-1])
        x=(length-1)%3
        raw.append(m[1:length-x-1-1])
        x=(length-2)%3
        raw.append(m[2:length-x-1-1-1])
    start="ATG"
    stop=["TAA","TAG","TGA"]
    for i in raw:
        start_index=-1
        stop_index=0
        for j in range(0,len(i)-2,3):
            codon=i[j+0]+i[j+1]+i[j+2]
            if codon==start:
                start_index=j
            elif codon==stop[0] or codon==stop[1] or codon==stop[2]: 
                stop_index=j+2
        if stop_index!=0 and start_index!=-1:
            frames.append(i[start_index:stop_index+1])
    return frames # a list of orf strings

def translate_DNA(dnaStrand, translation_table = 'DNA_TABLE.txt'):
    """
    # function body including documentation and test cases
    >>> translate_DNA('AUGUAUGAUGCGACCGCGAGCACCCGCUGCACCCGCGAAAGCUGA')
    MYDATASTRCTRES
    """
    protein=""
    k=dnaStrand
    codons=[k[j:j+3] for j in range(0, len(k), 3)]
    for i in codons:
        fopen=open(translation_table,'r')
        for line in fopen:
            if line[0]+line[1]+line[2]==i:
                protein+=line[4]
            elif line[11]+line[12]+line[13]==i:
                protein+=line[15]
            elif line[22]+line[23]+line[24]==i:
                protein+=line[26]
            elif line[33]+line[34]+line[35]==i:
                protein+=line[37]
    protein=protein[:-1]
    return protein # the protein string

def compute_protein_mass(protein_string):
    """
    #function body including documentation and test cases
    >>> compute_protein_mass('SKADYEK')
    821.392
    """
    mass=0
    for i in protein_string:
        massfile=open("PROT_MASS.txt",'r')
        for line in massfile:
            print(line)
            if i==line[0]:
                print(float(line[4:]))
                mass+=float(line[4:])
                
    return mass # the mass of the protein string as a float
if __name__ == '__main__':
    #DO NOT CHANGE THE FOLLOWING STATEMENTS
    for seq_name , seq in read_FASTA("hw1b_dataset.faa"):
        print (seq_name+":")
        for orf in identify_orfs(seq):
            protein=translate_DNA(orf)
            print (protein,compute_protein_mass(protein))
