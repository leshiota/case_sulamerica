# -*- coding: utf-8 -*-

import pandas as pd
import numpy as np
import math
import matplotlib.pyplot as plt
import statsmodels.formula.api as smf            # statistics and econometrics
import statsmodels.tsa.api as smt
import statsmodels.api as sm
import scipy.stats as scsfit
from statsmodels.tsa.holtwinters import ExponentialSmoothing

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
        
        recon_df['Regiao'] = recon_df['Região/Unidade da Federação'].\
            map(reg_dict)

        return recon_df

    def ts_train_test_split(self, data, n_test):

        return data[:(data.shape[0]-n_test)], data[(data.shape[0]-n_test):]

    def tsplot(self, y, lags=None, figsize=(12, 7), style='bmh'):
        """
            Plot time series, its ACF and PACF, calculate Dickey–Fuller test

            y - timeseries
            lags - how many lags to include in ACF, PACF calculation
        """
        if not isinstance(y, pd.Series):
            y = pd.Series(y)

        with plt.style.context(style):    
            fig = plt.figure(figsize=figsize)
            layout = (2, 2)
            ts_ax = plt.subplot2grid(layout, (0, 0), colspan=2)
            acf_ax = plt.subplot2grid(layout, (1, 0))
            pacf_ax = plt.subplot2grid(layout, (1, 1))

            y.plot(ax=ts_ax)
            p_value = sm.tsa.stattools.adfuller(y)[1]
            ts_ax.set_title('Time Series Analysis Plots\n Dickey-Fuller: p={0:.5f}'.format(p_value))
            smt.graphics.plot_acf(y, lags=lags, ax=acf_ax)
            smt.graphics.plot_pacf(y, lags=lags, ax=pacf_ax)
            plt.tight_layout()

    def mape_error(self, y_true, y_pred): 
        return np.mean(np.abs((y_true - y_pred) / y_true)) * 100
    
    def grid_seacrh_ets(self, y_train, y_test):
        trend = [None, "add", "mul"]
        seasonal = [None, "add", "mul"]
        seasonal_periods = [None, 3, 6, 9, 12]
        bc_transform = [True, False]
        remove_bias = [True, False]

        best_mape = None
        best_model = None
        errors = []

        for t in trend:
            for s in seasonal:
                for sp in seasonal_periods:
                    for bc in bc_transform:
                        for rb in remove_bias:
                            try:
                                model = ExponentialSmoothing(y_train, trend=t, seasonal=s, seasonal_periods=sp)
                                model_fit = model.fit(optimized=True, use_boxcox=bc, remove_bias=rb)
                                y_pred = model_fit.forecast(y_test.shape[0])
                                model_mape = self.mape_error(y_test, y_pred)
                                if math.isnan(model_mape):
                                    pass
                                elif best_mape is None:
                                    best_model = model_fit
                                    best_mape = model_mape
                                    best_config = [t, s, sp, bc, rb]
                                elif model_mape < best_mape:
                                    best_model = model
                                    best_mape = model_mape
                                    best_config = [t, s, sp, bc, rb]
                            except ValueError:
                                model_error = ["not able to fit model ", 
                                               str(t),
                                               str(s),
                                               str(sp),
                                               str(bc),
                                               str(rb)]
                                msg = " ".join(model_error)
                                errors.append(msg)

        return best_model, best_mape, errors, best_config

