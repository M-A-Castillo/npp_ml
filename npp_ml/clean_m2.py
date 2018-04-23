### This script intends to clean the individual docket csv's

import pandas as pd
import numpy as np

ALL = [
    010,133,155,206,213,220,237,244,245,247,249,250,251,254,255,259,260,
    263,266,267,269,270,271,272,275,277,278,280,281,285,286,287,289,293,
    295,296,298,301,302,304,305,306,309,311,312,313,315,316,317,318,320,
    321,322,323,324,325,327,328,331,334,335,336,338,341,344,346,348,353,
    354,361,362,364,366,368,369,370,373,374,382,387,389,390,391,395,397,
    400,409,410,412,413,414,265,423,424,425,440,443,445,446,454,455,456,
    457,458,461,482,483,498,499,528,529,530,219,261,282,333,339,352,388,
    416]

for i in ALL:
    df = pd.read_csv('m2_dockets_csv/%s_m2_results.csv'%i)

### Rename RPT_PERIOD of DF
    df.rename(columns = {'RPT_PERIOD':'RPT_PERIOD_M2','Unnamed: 0':'TRUE_INDEX'}, inplace = True)
    df = df.drop(['DOCKET','Unnamed: 14','Unnamed: 15','Unnamed: 16','Unnamed: 17',
                'Unnamed: 18','Unnamed: 19','Unnamed: 20','Unnamed: 21','Unnamed: 22',
                'Unnamed: 23','Unnamed: 24','Unnamed: 25','Unnamed: 26','Unnamed: 27',
                'Unnamed: 28','Unnamed: 29','Unnamed: 30','Unnamed: 31','Unnamed: 32',
                'Unnamed: 33','Unnamed: 34','Unnamed: 35','Unnamed: 36','Unnamed: 37',
                'Unnamed: 38'],axis =1) ### Note ### When removing columns, rename the dataframe because it doesnt save it.
    df['OUTG_DATE'] = pd.to_datetime(df['OUTG_DATE']) ### Changed OUTG_DATE int64 -> datetime64
    df['DESCRIP'] = df['DESCRIP'].astype(str)
    print i
    df.to_csv('clean_csv/%s_m2_cleaned.csv'%i)
