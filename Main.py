import TableSuffixes as ts
import AligneurDynamique as al
import time

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

def mean(numbers) :
    return float(sum(numbers)) / max(len(numbers), 1)


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
    def __init__(self, pathnameText,pathnameReads):
        super(Dynamique, self).__init__()
        self.time = time.time()
        self.text = lectureText(pathnameText)
        self.lesReads = lectureReads(pathnameReads)
        self.ts = ts.TableSuffixes(self.text)
        self.timeAlignement = []
        for read in self.lesReads :
            text = self.ts.getSuffixeAt(self.ts.table[self.ts.recherche_dicho(read)])[0:len(read)-1] + "$"           
            timeAl = time.time()
            aligneur = al.AligneurDynamique(text, read, 3)
            aligneur.createMatrix()
            (i,j) = aligneur.departBackTrack()
            (text,chaine,read) = aligneur.backTrack(i,j)
            timeAl = time.time() - timeAl
            self.timeAlignement.append(timeAl)
            print(text)
            print(chaine)
            print(read)
        self.time = time.time - self.time
        print(self.ts.time, " secondes pour créer la table des suffixes")
        print(mean(self.timeAlignement)," secondes en moyenne pour aligner un read à un sous-texte")
        print(self.time, " secondes au total")


# print(lectureText("text1.fna"))
# print(lectureReads("lesReads1.fastq"))

# main = Exact("text1.fna","lesReads1.fastq")
main = Dynamique("text1.fna","lesReads1.fastq")