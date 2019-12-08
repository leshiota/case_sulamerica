#%%
import pandas as pd
import numpy as np

#%%
def read_data(filename):
    xls = pd.ExcelFile(filename)
    sheets = xls.sheet_names
    df = pd.read_excel(filename,
                       sheet_name=sheets[0],
                       nrows=0)
    df['sheet_name'] = np.nan
    for sheet in sheets:
        temp = pd.read_excel(filename,
                             sheet_name=sheet)
        temp['sheet_name'] = sheet
        df = df.append(temp)

    return df


#%%