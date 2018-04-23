### Used this file to seperate dockets into own csv files
### alternate between m1 & m2 for both MORP1 and MORP2

import pandas as pd

ALL = [133,155,206,213,219,220,237,244,245,247,249,250,251,254,255,259,260,261,263,265,266,267,269,270,271,272,275,277,278,280,281,282,285,286,
287,289,293,295,296,298,301,302,304,305,306,309,311,312,313,315,316,317,318,320,321,322,323,324,325,327,328,331,333,334,335,336,338,339,341,
344,346,348,352,353,354,361,362,364,366,368,369,370,373,374,382,387,388,389,423,424,425,440,443,445,446,454,455,456,457,458,461,482,483,498,499,528]
df = pd.read_csv('MORP2.csv')
for i in ALL:
    dock = df[df.DOCKET ==i] ## Creates dataframe of info for specified docket
    dock.to_csv('m2_dockets_csv/%s_m2_results.csv'%i)

df = pd.read_csv('MORP1.csv')
for i in ALL:
    dock = df[df.DOCKET ==i] ## Creates dataframe of info for specified docket
    dock.to_csv('m1_dockets_csv/%s_m1_results.csv'%i)
