import pandas as pd 

df = pd.read_csv('expresion_genica.tsv', sep='\t')

#filtrar gene con expresion mayor a 100 en las 3 condiciones 

genes_altamente_expresados = df [
    (df ['cond1'] > 1000) & 
    (df['cond2'] > 1000) & 
    (df['cond3'] > 1000)]

print (genes_altamente_expresados)

df['promedio'] = df[['cond1', 'cond2', 'cond3']].mean(axis=1)
print(df)

df = df_ordenado.to_csv('genes_ordenados.tsv', sep=',', index=False, header=True)
print (df_ordenado) 