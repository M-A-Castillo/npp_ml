#### This script takes cleaned_csv files then sends them to individual dictionaries
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import csv

### Dockets CHECK 219 261 282 333 339 352 388 416 ---There are floats in these dockets.
### Python interprets 010 as 8 because of octal.
ALL = [
    010,133,155,206,213,220,237,244,245,247,249,250,251,254,255,259,260,
    263,266,267,269,270,271,272,275,277,278,280,281,285,286,287,289,293,
    295,296,298,301,302,304,305,306,309,311,312,313,315,316,317,318,320,
    321,322,323,324,325,327,328,331,334,335,336,338,341,344,346,348,353,
    354,361,362,364,366,368,369,370,373,374,382,387,389,390,391,395,397,
    400,409,410,412,413,414,265,423,424,425,440,443,445,446,454,455,456,
    457,458,461,482,483,498,499,528,529,530,219,261,282,333,339,352,388,
    416]

class Dictionary_sort:

### Counts all word occurences
    def counting(self,dataframe_string):
        self.non_word = ['IF','THE','TO','OF','A','FOR','END','AT','AND','BE','WAS','AN']
        self.d_ = ','.join(str(v) for v in dataframe_string) ### Creates one string
        self.d_ = self.d_.replace('(','').replace(')','').replace('.','').replace(',','').upper() ### Gets rid of parenthesis
        self.counts = {} ### Creates empty dictionary
        self.words = self.d_.split() ### splits string into array of substrings
        self.words = [word for word in self.words if word not in self.non_word]
        for word in self.words:
            if word in self.counts: ### If word is in dictionary add 1
                self.counts[word] += 1
            else: ### if word not in dictionary assign a value to it
                self.counts[word] = 1
        self.val = sorted(self.counts.values(), reverse = True) ### Occurences in dict
        self.bird = sorted(self.counts.keys(), key = self.counts.__getitem__,reverse = True) ### Words in dict
        return self.counts
if __name__ == '__main__':
    diction = Dictionary_sort()
    for i in ALL:
        print i
        df = pd.read_csv('clean_csv/{}_m2_cleaned.csv'.format(i)) ### Reads dataframe for specific docket
        df = df['DESCRIP']
        z = diction.counting(df)
        w = csv.writer(open('dict_csv/%s_dict.csv'%i,'w'))
        for key, val in z.items():
            w.writerow([key,val]) ### This places all dictionaries from each reactor into their own CSV file.
