import TableSuffixes as ts


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




class Main(object):
    """docstring for Main"""
    def __init__(self, pathnameText,pathnameReads):
        super(Main, self).__init__()
        self.text = lectureText(pathnameText)
        self.lesReads = lectureReads(pathnameReads)
        self.ts = ts.TableSuffixes(self.text)
        print(self.ts.recherche_dicho("ACACACAAAAAGAAAGAAGAATTTTTAGGATCTTTTGTGTGCGAATAACTATGAGGAAGATTAATAATTTTCCTCTCATTGAAATTTATATCGGAATTTAAATT$"))

    def run(self) :
        pass
        


# print(lectureText("text1.fna"))
# print(lectureReads("lesReads1.fastq"))

main = Main("text1.fna","lesReads1.fastq")
