import numpy as np

class AligneurDynamique(object):
    """docstring for AligneurDynamique"""
    def __init__(self, text, read, maxErreur):
        super(AligneurDynamique, self).__init__()
        self.text = text
        self.tailleText = len(text)
        self.read = read
        self.tailleRead = len(read)
        self.maxErreur = maxErreur
        self.indel = -10
        self.match = 5
        self.mismatch = -4 


    def matching(self,i,j) :
        '''
        Pas très complexe renvoire le score de match si ça match,
        le score de mismatch sinon.
        '''
        if self.text[j-1] == self.read[i-1] :
            return self.match
        else :
            return self.mismatch

    def chooseValue(self,i,j) :
        '''
        Donne le score résulat de la case [i][j]
        '''
        ouest = self.score[i][j-1]
        nord = self.score[i-1][j]
        nordOuest = self.score[i-1][j-1]
        if ouest == None :
            return max(nord+self.indel,nordOuest+self.matching(i,j))
        elif nord == None :
            return max(ouest+self.indel,nordOuest+self.matching(i,j))
        else :
            return max(ouest+self.indel,max(nord+self.indel,nordOuest+self.matching(i,j)))

    def chooseValueBack(self,i,j) :
        ouest = self.score[i][j-1]
        nord = self.score[i-1][j]
        nordOuest = self.score[i-1][j-1]
        if j == 0 :
            return nord
        if i == 0 :
            return ouest
        if ouest == None :
            return max(nord,nordOuest)
        elif nord == None :
            return max(ouest,nordOuest)
        else :
            return max(ouest,max(nord,nordOuest))


    def createMatrix(self) :
        '''
        Cette fonction est un passage obligatoire elle permet de calculer la matrice de prog dynamique pour notre alignement.
        '''
        # initialisation du tableau Score
        self.score = []
        for ligne in range(self.tailleRead+1) :
            self.score.append([None]*(self.tailleText+1))
        for i in range(self.maxErreur+1) :
            self.score[i][0] = -i
            self.score[0][i] = -i
        for i in range(1,self.tailleRead+1) :
            for j in range(1,self.tailleText+1) :
                if self.score[i-1][j-1] == None :
                    continue
                else :
                    self.score[i][j] = self.chooseValue(i,j)


    def departBackTrack(self) :
        '''
        une fois la matrice de score calculée 
        on cherche dans la dernière ligne l'élément
        le plus grand, on renvoie ses coordonnées i j 
        '''
        jSauvegarde = None
        elementSauvegarde = None
        for j in range(1,self.tailleText+1) :
            element = self.score[self.tailleRead][j]
            if element == None :
                continue
            elif jSauvegarde == None :
                jSauvegarde = j
                elementSauvegarde = element
            elif max(element,elementSauvegarde) == element :  
                jSauvegarde = j
                elementSauvegarde = element
        return (self.tailleRead,jSauvegarde)

    def backTrack(self,i,j) :
        '''
        enfin notre fonction de back tracking pour retrouver notre alignement
        à partir d'un point de départ (i,j)
        '''
        iActuel = i
        jActuel = j
        iText = self.tailleText - 1
        iRead = self.tailleRead - 1
        text = ""
        read = ""
        chaine = ""
        for k in range(self.tailleText-j) :
            read = '-' + read
            text = self.text[iText] + text
            iText -= 1
        while not (iActuel==jActuel==0):
            ouest = self.score[iActuel][jActuel-1]
            nord = self.score[iActuel-1][jActuel]
            nordOuest = self.score[iActuel-1][jActuel-1]
            valeur = self.chooseValueBack(iActuel,jActuel)
            if valeur == ouest :
                jActuel = jActuel-1
                read = '-' + read
                text = self.text[iText] + text
                iText -= 1
                chaine = ' ' + chaine
            elif valeur == nord :
                iActuel = iActuel - 1
                text = '-' + text
                read = self.read[iRead] + read
                iRead -= 1
                chaine = ' ' + chaine
            else : #donc on choisis nordouest on regarde si match ou mismatch
                read = self.read[iRead] + read
                text = self.text[iText] + text
                iRead -= 1
                iText -= 1
                if valeur > self.score[iActuel][jActuel] : #mismatch
                    chaine = ' ' + chaine
                else :
                    chaine = '|' + chaine
                iActuel = iActuel - 1
                jActuel = jActuel - 1
        return (text,chaine,read)




    def printScore(self) :
        '''
        oui parce que par defaut c est moins joli voilà pardon...
        '''
        for i in range(self.tailleRead+1) :
            print(str(self.score[i]))

bout_genome = "tgggatggatcaaccctaacagtggtggcacaaactatgcacagaagtttcagggcagggtcaccatgaccagggacacgtccatcagcacagcctacatggagctgagcaggctgagatctgacgacacggccgtgtattactgtgcgagaga"
read_test = "ttgcacgcattgattgggatgatgataaatactacagcacatctctgaagaccaggctcaccatctccaaggacacctccaaaaaccaggtggtccttacaatgaccaacatggaccctgtggacacggccgtgtattactg"



align = AligneurDynamique(bout_genome, read_test, 10)
# align = AligneurDynamique("ATTATCGGG", "TACTATC", 2)

align.createMatrix()
# align.printScore()
(i,j) = align.departBackTrack()
(text,chaine,read) = align.backTrack(i,j)
print(text)
print(chaine)
print(read)