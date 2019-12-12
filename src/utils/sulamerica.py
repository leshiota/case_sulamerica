import pandas as pd
import numpy as np



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


def rename_data(df):
    months = {'jul19': '2019-07','jun19': '2019-06','dez17': '2017-12','mar18': '2018-03','abr19': '2019-04',
              'abr18': '2018-04','mai18': '2018-05','jul18': '2018-07','ago18': '2018-08','set18': '2018-09',
              'nov18': '2018-11','dez18': '2018-12','jan19': '2019-01','fev19': '2019-02'}
    regiao = {'Região Norte': 'NORTE_TOTAL', '.. Roraima': 'NORTE', 'Região Nordeste': 'NORDESTE_TOTAL',
              '.. Rondônia': 'NORTE','.. Acre': 'NORTE','.. Amazonas': 'NORTE', '.. Espírito Santo': 'SUDESTE',
              '.. Pará': 'NORTE','.. Amapá': 'NORTE','.. Tocantins': 'NORTE', '.. Rio Grande do Norte': 'NORDESTE',
              '.. Maranhão': 'NORDESTE','.. Piauí': 'NORDESTE','.. Ceará': 'NORDESTE',
              '.. Paraíba': 'NORDESTE','.. Pernambuco': 'NORDESTE','.. Alagoas': 'NORDESTE','.. Sergipe': 'NORDESTE',
              '.. Bahia': 'NORDESTE','Região Sudeste': 'SUDESTE_TOTAL','.. Minas Gerais': 'SUDESTE','.. Espírito Santo': 'SUDESTE',
              '.. Rio de Janeiro': 'SUDESTE','.. São Paulo': 'SUDESTE','Região Sul': 'SUL_TOTAL','.. Paraná': 'SUL',
              '.. Santa Catarina': 'SUL','.. Rio Grande do Sul': 'SUL','Região Centro-Oeste': 'CENTRO-OESTE_TOTAL',
              '.. Mato Grosso do Sul': 'CENTRO-OESTE','.. Mato Grosso': 'CENTRO-OESTE','.. Goiás': 'CENTRO-OESTE',
              '.. Distrito Federal': 'CENTRO-OESTE', 'Total': 'TOTAL'}

    nomes = {'.. Paraíba': 'Paraíba','.. Rondônia': 'Rondônia','.. Piauí': 'Piauí','.. Distrito Federal': 'Distrito Federal',
             '.. Pará': 'Pará', '.. Rio Grande do Norte': 'Rio Grande do Norte', 'Região Nordeste': 'Região Nordeste', 
             'Região Centro-Oeste': 'Região Centro-Oeste', '.. Pernambuco': 'Pernambuco','.. Amazonas': 'Amazonas',
             '.. Mato Grosso do Sul': 'Mato Grosso do Sul', 'Região Sul': 'Região Sul','.. Ceará': 'Ceará',
             '.. Alagoas': 'Alagoas', '.. São Paulo': 'São Paulo', '.. Bahia': 'Bahia', '.. Rio Grande do Sul': 'Rio Grande do Sul', 
             '.. Maranhão': 'Maranhão','.. Tocantins': 'Tocantins','Região Norte': 'Região Norte','.. Mato Grosso': 'Mato Grosso',
             'Total': 'Total', '.. Amapá': 'Amapá', 'Região Sudeste': 'Região Sudeste', '.. Sergipe': 'Sergipe',
             '.. Goiás': 'Goiás', '.. Rio de Janeiro': 'Rio de Janeiro', '.. Santa Catarina': 'Santa Catarina', '.. Roraima': 'Roraima',
             '.. Minas Gerais': 'Minas Gerais','.. Paraná': 'Paraná','.. Espírito Santo': 'Espírito Santo','.. Acre': 'Acre'}

    df['period'] = df['sheet_name'].map(months)
    df['Regiao'] = df['Região/Unidade da Federação'].map(regiao)
    df['Região/Unidade da Federação'] = df['Região/Unidade da Federação']\
        .map(nomes)

    return df


def add_period_data(df):
    period_list = ['2017-12', '2018-01', '2018-02', '2018-03', '2018-04', '2018-05',
                   '2018-06', '2018-07', '2018-08', '2018-09', '2018-10', '2018-11',
                   '2018-12', '2019-01', '2019-02', '2019-03', '2019-04', '2019-05',
                   '2019-06', '2019-07'] 

    names_list = ['Região Norte', 'Rondônia', 'Acre', 'Amazonas', 'Roraima', 'Pará',
                  'Amapá', 'Tocantins', 'Região Nordeste', 'Maranhão', 'Piauí',
                  'Ceará', 'Rio Grande do Norte', 'Paraíba', 'Pernambuco', 'Alagoas',
                  'Sergipe', 'Bahia', 'Região Sudeste', 'Minas Gerais',
                  'Espírito Santo', 'Rio de Janeiro', 'São Paulo', 'Região Sul',
                  'Paraná', 'Santa Catarina', 'Rio Grande do Sul',
                  'Região Centro-Oeste', 'Mato Grosso do Sul', 'Mato Grosso',
                  'Goiás', 'Distrito Federal', 'Total']
    comb = []
    for period in period_list:
        for name in names_list:
            comb.append([period, name])

    temp_df = pd.DataFrame(comb, columns=['period','Região/Unidade da Federação'])

    df = pd.merge(temp_df, df, how="left")

    return df


def _break_data(df):
    df = df[~df['Regiao'].str.contains("TOTAL", na=False)]\
        .sort_values(by=['period'])
    regiao_list = df['Região/Unidade da Federação'].unique()

    df_list = list()
    for regiao in regiao_list:
        df_list = df[df['Região/Unidade da Federação'] == regiao]

    return df_list


def _impute_data(df, method='linear'):
    pass


def reconstruct_data(df, method='linear'):

    df_list = _break_data(df=df)
    
    for dfs in df_list:
        imputed_df = _impute_data(df=dfs, method=method)

    df = _impute_data(df=df, method=method)







