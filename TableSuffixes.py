

class TableSuffixes(object):
    """docstring for TableSuffixes"""
    
    def custom_key(self,indice):
        numbers = []
        word = self.text[indice:]
        for letter in word :
            numbers.append(self.my_alphabet.index(letter))
        return numbers


    def __init__(self,text):
        super(TableSuffixes, self).__init__()
        print("begin suffixe table")
        self.text = text
        self.my_alphabet = ['$','A','C','G','T']
        self.table = []
        for i in range(len(text)) :
            self.table.append(i)
        self.table.sort(key=self.custom_key)
        print("end suffixe table")


    def getSuffixeAt(self,indice) :
        chaine = ""
        for i in range(indice,len(self.text)) :
            chaine += self.text[i]
        return chaine

    
    def compare(self,indice,element) :
        '''
        Dans la recherche dichotomique sert à comparer
        deux chaines en s'arretant dès que possible
        '''
        iElement = 0
        for i in range(indice,len(self.text)) :
            charText = self.text[i]
            charElement = element[iElement]
            if charText == "$" and charElement == "$"  :
                return 0
            if self.my_alphabet.index(charText) > self.my_alphabet.index(charElement) :
                return 1
            elif self.my_alphabet.index(charText) < self.my_alphabet.index(charElement) :
                return -1

    def recherche_dicho(self,element) :
        a = 0
        b = len(self.table) - 1
        m = (a+b)//2
        while a < b :
            print(a,b,m)
            compResult = self.compare(m,element)
            if compResult == 0 :
                return m
            elif compResult == 1 :
                b = m - 1
            else :
                a = m + 1
            m = (a+b) // 2   
        return a

        