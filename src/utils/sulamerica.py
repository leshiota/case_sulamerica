# -*- coding: utf-8 -*-

import pandas as pd
import numpy as np

"""
Hard coded dictionaries and lists
"""
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

period_list = ['2017-12', '2018-01', '2018-02', 
               '2018-03', '2018-04', '2018-05',
               '2018-06', '2018-07', '2018-08', 
               '2018-09', '2018-10', '2018-11',
               '2018-12', '2019-01', '2019-02', 
               '2019-03', '2019-04', '2019-05',
               '2019-06', '2019-07']

names_list = ['Região Norte', 'Rondônia', 'Acre',
              'Amazonas', 'Roraima', 'Pará',
              'Amapá', 'Tocantins', 'Região Nordeste', 'Maranhão', 'Piauí',
              'Ceará', 'Rio Grande do Norte',
              'Paraíba', 'Pernambuco', 'Alagoas',
              'Sergipe', 'Bahia', 'Região Sudeste', 'Minas Gerais',
              'Espírito Santo', 'Rio de Janeiro', 'São Paulo', 'Região Sul',
              'Paraná', 'Santa Catarina', 'Rio Grande do Sul',
              'Região Centro-Oeste', 'Mato Grosso do Sul', 'Mato Grosso',
              'Goiás', 'Distrito Federal', 'Total']

regiao_list = ['Rondônia', 'Acre', 'Amazonas', 'Roraima', 'Pará',
               'Amapá', 'Tocantins',  'Maranhão', 'Piauí',
               'Ceará', 'Rio Grande do Norte', 'Paraíba', 
               'Pernambuco', 'Alagoas',
               'Sergipe', 'Bahia',  'Minas Gerais',
               'Espírito Santo', 'Rio de Janeiro', 'São Paulo',
               'Paraná', 'Santa Catarina', 'Rio Grande do Sul',
               'Mato Grosso do Sul', 'Mato Grosso',
               'Goiás', 'Distrito Federal']

reg_dict = {'Rondônia': 'NORTE', 'Acre': 'NORTE', 'Amazonas': 'NORTE',
            'Roraima': 'NORTE', 'Pará': 'NORTE', 'Amapá': 'NORTE',
            'Tocantins': 'NORTE', 'Maranhão': 'NORDESTE', 'Piauí': 'NORDESTE',
            'Ceará': 'NORDESTE', 'Rio Grande do Norte': 'NORDESTE', 'Paraíba': 'NORDESTE',
            'Pernambuco': 'NORDESTE', 'Alagoas': 'NORDESTE', 'Sergipe': 'NORDESTE',
            'Bahia': 'NORDESTE', 'Minas Gerais': 'SUDESTE', 'Espírito Santo': 'SUDESTE',
            'Rio de Janeiro': 'SUDESTE', 'São Paulo': 'SUDESTE', 'Paraná': 'SUL',
            'Santa Catarina': 'SUL', 'Rio Grande do Sul': 'SUL',
            'Mato Grosso do Sul': 'CENTRO-OESTE',
            'Mato Grosso': 'CENTRO-OESTE', 'Goiás': 'CENTRO-OESTE',
            'Distrito Federal': 'CENTRO-OESTE'}


"""
Class with all functions used in the analysis
"""


class Sulamerica:

    def read_data(self, filename):
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

    def rename_data(self, df):

        df['period'] = df['sheet_name'].map(months)
        df['Regiao'] = df['Região/Unidade da Federação'].map(regiao)
        df['Região/Unidade da Federação'] = df['Região/Unidade da Federação']\
            .map(nomes)

        return df

    def add_period_data(self, df):
        comb = []
        for period in period_list:
            for name in names_list:
                comb.append([period, name])

        temp_df = pd.DataFrame(comb,
                               columns=['period', 'Região/Unidade da Federação'])

        df = pd.merge(temp_df, df, how="left")

        return df

    
    def _break_data(self, df):

        df = df.sort_values(by=['period'])    
        df_list = list()
        for region in regiao_list:
            df_list.append(df[df['Região/Unidade da Federação'] == region])

        return df_list

    
    def _impute_data(self, df,
                     method='linear',
                     feature_list=['Internações', 'AIH_aprovadas',
                                   'Valor_total', 'Valor_médio_AIH',
                                   'Dias_permanência', 'Óbitos',
                                   'hospitalar_total', 'servicos_total']):

        for feature in feature_list:
            df[feature] = df[feature].interpolate(method=method)
    
        return df
    
    def reconstruct_data(self, df, method='linear'):
    
        df_list = self._break_data(df=df)
    
        recon_df = pd.DataFrame(columns=['Região/Unidade da Federação','period', 
                                          'Internações', 'AIH_aprovadas',
                                          'Valor_total', 'Valor_médio_AIH',
                                          'Dias_permanência', 'Óbitos',
                                          'hospitalar_total', 'servicos_total'])
        for dfs in df_list:
            imputed_df = self._impute_data(df=dfs, method=method)
            recon_df = pd.concat([recon_df, imputed_df],
                                 axis=0,
                                 ignore_index=True)
    
        recon_df = recon_df[['Região/Unidade da Federação','period', 
                             'Internações', 'AIH_aprovadas',
                             'Valor_total', 'Valor_médio_AIH',
                             'Dias_permanência', 'Óbitos',
                             'hospitalar_total', 'servicos_total']].\
            sort_values(by=['Região/Unidade da Federação', 'period'])
        
        recon_df['Regiao'] = recon_df['Região/Unidade da Federação']\
            .map(reg_dict)

        return recon_df
