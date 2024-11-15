import pandas as pd    

knimeTable = pd.read_csv('Table_finale.csv')

#recherche d'outliers
Q1 = knimeTable['Salaire base mensuel'].quantile(0.25)
Q3 = knimeTable['Salaire base mensuel'].quantile(0.75)
IQR = Q3 - Q1
outliers = knimeTable[(knimeTable['Salaire base mensuel'] < (Q1 - 1.5 * IQR)) | (knimeTable['Salaire base mensuel'] > (Q3 + 1.5 * IQR))]
print(outliers)
