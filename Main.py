import TableSuffixes as ts
import AligneurDynamique as al


def lectureReads(pathname) :
    print("begin reading reads")
    fichier = open(pathname,'r')
    cpt = 0
    lesReads = []
    for ligne in fichier :
        if cpt % 4 == 1 :
            ligneClean = ligne.replace("\n", "")
            lesReads.append(ligneClean+"$")
        cpt += 1
    fichier.close()
    print("end reading reads")
    return lesReads

def lectureText(pathname) :
    print("begin reading text")
    fichier = open(pathname,'r')
    cpt = 0
    text = ""
    ligne = fichier.readline()
    while ligne != "" :
        ligne = fichier.readline().rstrip()
        text += ligne
    text += "$"
    fichier.close()
    print("end reading text")
    return text




class Exact(object):
    """N'affiche que les reads qui sont exactement dans le texte"""
    def __init__(self, pathnameText,pathnameReads):
        super(Exact, self).__init__()
        self.text = lectureText(pathnameText)
        self.lesReads = lectureReads(pathnameReads)
        self.ts = ts.TableSuffixes(self.text)
        # self.aligneur = al.
        for read in self.lesReads :
            comp = self.ts.getSuffixeAt(self.ts.table[self.ts.recherche_dicho(read)])[0:len(read)-1] + "$"
            if read == comp :
                print("#############################################")
                print(read)
                print(comp)
        # print(self.ts.getSuffixeAt(self.ts.table[self.ts.recherche_dicho("ACACACAAAAAGAAAGAAGAATTTTTAGGATCTTTTGTGTGCGAATAACTATGAGGAAGATTAATAATTTTCCTCTCATTGAAATTTATATCGGAATTTAAATT$")]))
 
class Dynamique(object):
    """Accepte des erreurs avec Kband"""
    def __init__(self, pathnameText,pathnameReads,maxError):
        super(Dynamique, self).__init__()
        self.maxError = maxError
        self.text = lectureText(pathnameText)
        self.lesReads = lectureReads(pathnameReads)
        self.ts = ts.TableSuffixes(self.text)
        for read in self.lesReads :
            text = self.ts.getSuffixeAt(self.ts.table[self.ts.recherche_dicho(read)])[0:len(read)-1] + "$"           
            if len(text) == len(read) :
                aligneur = al.AligneurDynamique(text, read, 3)
                aligneur.createMatrix()
                (i,j) = aligneur.departBackTrack()
                (text,chaine,read,nbError) = aligneur.backTrack(i,j)
                if nbError <= self.maxError :
                    print(text)
                    print(chaine)
                    print(read)



# print(lectureText("text1.fna"))
# print(lectureReads("lesReads1.fastq"))

# main = Exact("text1.fna","lesReads1.fastq")
main = Dynamique("text1.fna","lesReads1.fastq",10)