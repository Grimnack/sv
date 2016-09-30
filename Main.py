import TableSuffixes as tf


def lectureReads(pathname) :
    fichier = open(pathname,'r')
    cpt = 0
    lesReads = []
    for ligne in fichier :
        if cpt % 4 == 1 :
            lesReads.append(ligne)
        cpt += 1
    fichier.close()
    return lesReads

def lectureText(pathname) :
    fichier = open(pathname,'r')
    cpt = 0
    text = ""
    ligne = fichier.readline()
    while ligne != "" :
        ligne = fichier.readline().rstrip()
        text += ligne
    fichier.close()
    return text




class Main(object):
    """docstring for Main"""
    def __init__(self, pathnameText,pathnameReads):
        super(Main, self).__init__()
        self.text = lectureText(pathnameText)
        self.lesReads = lectureReads(pathnameReads)
        self.ts = ts.TableSuffixes(self.text)

    def run(self) :     
        


# print(lectureText("text1.fna"))
print(lectureReads("lesReads1.fastq"))