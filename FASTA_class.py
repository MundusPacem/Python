
class FASTA:
    def __init__(self, name, desc, seq, Len, gc, stype):
        self.name   = name
        self.desc   = desc
        self.seq    = seq
        self.Len    = Len
        self.gc     = gc
        self.stype  = stype



    def setName(self):
        self.name = name
        

    def getName(self):
        return self.name

    def setDesc(self):
        self.desc = desc

    def getDesc(self):
        return self.desc

    def setSeq(self):
        self.seq = seq

    def getSeq(self):
        return self.seq
    
    def setLength(self):
        self.Len = Len

    def getLength(self):
        return self.Len

    
    def calcGC(self):

        i       = 0
        tot_GC  = 0.0

        for i in range (len(seq)):
            if seq[i] == "G" or seq[i] == "C":
                tot_GC += 1.0

        gc = (tot_GC/(len(seq)))

    

    def getGC(self):
        return self.gc
    

    def getRevSeq(self):
        
        gene = seq

        reversed = ''.join(reversed(gene))

        x = reversed.upper()
        
        x = revseq
        list(revseq)

        i = 0
        for i in range(len(seq)):
            if seq == "A":
                revseq.write("T")
                
            if revseq[i] == "T":
                revseq.append("A")

            if revseq[i] == "G":
                revseq.append("C")

            if revseq[i] == "C":
                revseq.append("G")

            else:
                revseq.append(revseq[i])
                
        "".join(revseq)

        return revseq
    
    
    def getCompSeq(self):

        


    def getSubSeq(self):

