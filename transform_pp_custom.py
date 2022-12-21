import pandas as pd
import os
import sys

version = sys.argv[1]           #'1.15'
input_version = sys.argv[2]     #'version_komodo'
all_version = ['version_komodo', 'version_xarelto']

workspace = str(os.environ['WORKSPACE'])
file_loc = workspace + "/mapping/master/"
file_names = ['dev_PP_JBI_master_ingestion_mapping']


for name in file_names:

    file_path = file_loc + name + ".csv"
    print(file_path)

    df = pd.read_csv(file_path, sep=',')
    index_name = df[~df[input_version].isin(['Y'])].index
    df.drop(index_name, inplace=True)
    
    for v in all_version:
        del df[v]

    target_file_path = workspace + "/config/mapping/" + name + ".csv"
    target_file_path = target_file_path.replace('JBI_master', 'JBI_' + version)
    print(target_file_path)
    df.to_csv(target_file_path, sep=',', encoding='utf-8', index=False)
