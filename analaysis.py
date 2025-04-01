import pandas as pd



file_path = '/Users/yairbecher/dad_projects/teunut.csv'
df = pd.read_csv(file_path)
columns = ['SHNAT_TEUNA', 'HODESH_TEUNA', 'SHAA', 'HODESH_TEUNA', 'SUG_YOM', 'YOM_LAYLA', 'YOM_BASHAVUA', 'HUMRAT_TEUNA', 'SUG_TEUNA']

df_s = df[columns]

df_s = df_s.copy()


# df_s.to_csv("/Users/yairbecher/dad_projects/df_teunut.csv", index=False)

