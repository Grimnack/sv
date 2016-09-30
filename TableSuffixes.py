

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
        self.text = text
        self.my_alphabet = ['\n','A','C','G','T']
        self.table = []
        for i in range(len(text)) :
            self.table.append(i)
        self.table.sort(key=self.custom_key)


ts = TableSuffixes("ATTAC\n")
print(ts.table)

        