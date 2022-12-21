import pandas as pd
import shutil as sh

version = '1.15'
input_version = 'version_komodo'
all_version = ['version_komodo', 'version_xarelto']

file_loc = r"C:\Users\Prasanna\Desktop\AWS CICD"
file_name = ['dev_PP_JBI_master_ingestion_mapping']

target_file_loc = file_loc + "\\sandbox\\Design\\"+version
file_loc_2 = file_loc + "\\sandbox\\Design\\_master"

for file in file_name:
    file_path = file_loc_2 + "\\" + file + ".csv"
    target_file_path = target_file_loc + "\\" + file + ".csv"
    sh.copyfile(file_path, target_file_path)


for name in file_name:

    file_path = file_loc + "\\sandbox\\Design\\"+"\\"+"1.15"+"\\"+name+".csv"
    #print(file_path)
    df = pd.read_csv(file_path,sep=',')
    index_name = df[~df[input_version].isin(['Y'])].index
    df.drop(index_name, inplace=True)

    for v in all_version:
        del df[v]

    target_file_path = file_loc + "\\sandbox\\Output\\" + version + "\\" + name + ".csv"
    target_file_path = target_file_path.replace('JBI_master', 'JBI_'+version)
    print(target_file_path)
    df.to_csv(target_file_path, sep=',', encoding='utf-8', index=False)
