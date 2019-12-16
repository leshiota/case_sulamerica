from src.utils import sulamerica
import pandas as pd
import numpy as np
import statsmodels.api as sm
from statsmodels.tsa.holtwinters import ExponentialSmoothing
import warnings
warnings.filterwarnings("ignore")


def main():

    
    sl = sulamerica.Sulamerica()

    df = sl.read_data('data/raw/cases_internacao_SUS.xls')
    df = sl.rename_data(df)
    df = df[df['AIH_aprovadas']>0]
    df['Val_serv_hosp_-_compl_federal'] = pd.to_numeric(df['Val_serv_hosp_-_compl_federal'], errors='coerce')
    df['Val_serv_hosp_-_compl_gestor'] = pd.to_numeric(df['Val_serv_hosp_-_compl_gestor'], errors='coerce')

    df['Val_serv_prof_-_compl_federal'] = pd.to_numeric(df['Val_serv_prof_-_compl_federal'], errors='coerce')
    df['Val_serv_prof_-_compl_gestor'] = pd.to_numeric(df['Val_serv_prof_-_compl_gestor'], errors='coerce')
    df = df.fillna(0)
    df['hospitalar_total'] = (df['Valor_serviços_hospitalares'] + df['Val_serv_hosp_-_compl_federal'] + df['Valor_serviços_hospitalares'])
    df['servicos_total'] = (df['Val_serv_prof_-_compl_federal'] + df['Val_serv_prof_-_compl_gestor'] + df['Valor_serviços_profissionais'])
    df['calculado_total'] = df['hospitalar_total'] + df['servicos_total']
    df['percentual_servicos'] = df['servicos_total'] / df['calculado_total']
    df['percentual_hospitalar'] = df['hospitalar_total'] / df['calculado_total']
    df = df[['period', 'Região/Unidade da Federação', 'Internações', 'AIH_aprovadas',
           'Valor_total', 'Valor_médio_AIH', 'Valor_médio_intern',
           'Dias_permanência', 'Média_permanência', 'Óbitos', 'Taxa_mortalidade',
            'Regiao', 'hospitalar_total', 'servicos_total',
           'calculado_total', 'percentual_servicos', 'percentual_hospitalar']]
    df = sl.add_period_data(df)

    temp_df = df[['Região/Unidade da Federação','period', 'Internações', 
                  'AIH_aprovadas','Valor_total', 'Valor_médio_AIH', 
                  'Dias_permanência', 'Óbitos', 'hospitalar_total', 'servicos_total']]
    recon_df = sl.reconstruct_data(temp_df)

    total_df = recon_df.groupby(['period']).sum().reset_index().sort_values(by=['period'])
    total_df['Taxa_mortalidade'] = (total_df['Óbitos']/total_df['Internações'])*100
    total_df['calculado_total'] = total_df['servicos_total']+total_df['hospitalar_total']
    total_df['media_permanencia'] = total_df['Dias_permanência']/total_df['Internações']

    X = total_df[['period','Internações','Óbitos','Valor_médio_AIH']].set_index('period')
    X_train, X_test = sl.ts_train_test_split(X, 2)
    y = X['Internações']

    best_model, best_mape, errors, best_config = sl.grid_seacrh_ets(X_train['Internações'], X_test['Internações'])
    model_ets = ExponentialSmoothing(y, 
                                 trend=best_config[0], 
                                 seasonal=best_config[1], 
                                 seasonal_periods=best_config[2])
    model_ets_fit = model_ets.fit(optimized=True, 
                                  use_boxcox=best_config[3], 
                                  remove_bias=best_config[4])
    model_ets_forecast = model_ets_fit.forecast(6)

    internacoes_HW_fitted = np.array(model_ets_fit.fittedvalues)
    internacoes_HW_forecast = np.array(model_ets_forecast)

    y=X['Óbitos']
    best_model, best_mape, errors, best_config = sl.grid_seacrh_ets(X_train['Óbitos'], X_test['Óbitos'])

    model_ets = ExponentialSmoothing(y, 
                                 trend=best_config[0], 
                                 seasonal=best_config[1], 
                                 seasonal_periods=best_config[2])
    model_ets_fit = model_ets.fit(optimized=True, 
                                  use_boxcox=best_config[3], 
                                  remove_bias=best_config[4])
    model_ets_forecast = model_ets_fit.forecast(6)

    obitos_HW_fitted = np.array(model_ets_fit.fittedvalues)
    obitos_HW_forecast = np.array(model_ets_forecast)

    y=X['Valor_médio_AIH']
    best_model, best_mape, errors, best_config = sl.grid_seacrh_ets(X_train['Valor_médio_AIH'], X_test['Valor_médio_AIH'])

    model_ets = ExponentialSmoothing(y, 
                                 trend=best_config[0], 
                                 seasonal=best_config[1], 
                                 seasonal_periods=best_config[2])
    model_ets_fit = model_ets.fit(optimized=True, 
                                  use_boxcox=best_config[3], 
                                  remove_bias=best_config[4])
    model_ets_forecast = model_ets_fit.forecast(6)

    AIH_HW_fitted = np.array(model_ets_fit.fittedvalues)
    AIH_HW_forecast = np.array(model_ets_forecast)

    forecast = {'internacoes_HW_forecast': internacoes_HW_forecast,
                'obitos_HW_forecast': obitos_HW_forecast,
                'AIH_HW_forecast': AIH_HW_forecast}

    fitted = {'internacoes_HW_fitted': internacoes_HW_fitted,
              'obitos_HW_fitted': obitos_HW_fitted,
              'AIH_HW_fitted': AIH_HW_fitted}

    df_fitted = pd.DataFrame(fitted, index=model_ets_fit.fittedvalues.index)
    df_forecast = pd.DataFrame(forecast, index=model_ets_forecast.index.strftime('%Y-%m'))


    df_fitted.to_csv('data/outputs/fitted.csv')
    df_forecast.to_csv('data/outputs/forecast.csv')



if __name__ == "__main__":
    main()