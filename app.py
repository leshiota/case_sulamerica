#%%
from src.utils import sulamerica as sl

df = sl.read_data('data/cases_internacao_SUS.xls')

months = {'jul19': 201907,
          'jun19': 201906,
          'dez17': 201712,
          'mar18': 201803,
          'abr19': 201904,
          'abr18': 201804,
          'mai18': 201805,
          'jul18': 201807,
          'ago18': 201808,
          'set18': 201809,
          'nov18': 201811,
          'dez18': 201812,
          'jan19': 201901,
          'fev19': 201902}


df['period'] = df['sheet_name'].map(months)


# %%
