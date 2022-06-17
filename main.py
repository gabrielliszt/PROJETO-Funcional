import pandas as pd

# Importando a planilha completa
dataframe = pd.read_excel("C:\\Users\\pbm\\Meu Drive\\Planilhas\\!ATENDIMENTOS - Gabriel.xlsx", dtype=str)

# Localizando apenas os valores que serão verificados
dataframe_funcional = dataframe.loc[dataframe['FUNCIONAL'] == 'VERIFICAR']
print(dataframe_funcional)

