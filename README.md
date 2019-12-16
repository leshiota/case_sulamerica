# case_sulamerica
Repository with codes, notebooks and data for Sulamérica interview.

### Project Structure

```
├── app.py
├── data
│   ├── outputs
│   │   ├── fitted.csv
│   │   └── forecast.csv
│   └── raw
│       └── cases_internacao_SUS.xls
├── environment.yml
├── LICENSE
├── notebooks
│   └── analise.ipynb
├── README.md
├── setup.py
├── src
│   ├── __init__.py
│   └── utils
│       ├── __init__.py
│       └── sulamerica.py
```

## Getting Started

This project contains all codes and analysis (jupyter notebooks) for the Sulamérica case. The notebook with all the explanation is on the notebooks folder, the notebook also generates the results of the models.

You can also generate the results by running the app.py file from the root of the project.

All data is in the data folder. Outputs folder contains both fitted and forecast values for the models that were selected.

### Installing

For this project run smooth we reccomend you to install the conda env. 
You can do it by running

```
conda env create --file environment.yml
```

To activate the environment just run

```
conda activate sulamerica
```