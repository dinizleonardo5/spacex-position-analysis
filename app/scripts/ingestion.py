from pandas import DataFrame
import json
import pandas as pd
import mysql.connector

def read_json(path:str) -> list:
    json_file = open(path)
    data = json.load(json_file)
    json_file.close()
    return data

def select_columns_and_remove_duplicates(data:list, cols:list) -> DataFrame:
    df = pd.DataFrame(pd.json_normalize(data, sep='_'), columns=cols).dropna(how='any',axis=0)
    return df

def filter_only_last_position(df:DataFrame, key_column:str, date_column:str) -> DataFrame:
    df_max = df.groupby(key_column)[date_column].max()
    df_last_position = pd.merge(df, df_max, on=[key_column, date_column], how='inner')
    df_last_position = df_last_position.drop_duplicates()
    return df_last_position

def insert_mysql(df:DataFrame, host:str, db:str, table:str, user:str, pw:str):
    mydb = mysql.connector.connect(host=host, user=user, passwd=pw, database=db)
    cursor = mydb.cursor()
    cols = ",".join([str(i) for i in df.columns.tolist()])
    count = 0
    for i,row in df.iterrows():
        sql = f'INSERT INTO {table} ({cols}) VALUES {tuple(row)};'
        try:
            cursor.execute(sql)
        except Exception as e:
            raise ValueError(e)
        count += 1
    mydb.commit()
    mydb.close()
    print(f'{count} rows inserted into table {table}!')

def execute_script():
    data_spacex = read_json('app/source/starlink_historical_data.json')
    df_spacex_hst = select_columns_and_remove_duplicates(data_spacex, ['id', 'latitude', 'longitude', 'spaceTrack_CREATION_DATE'])
    df_spacex_hst.rename(columns={"spaceTrack_CREATION_DATE": "creation_date"}, inplace=True)
    #df_spacex_last_pos = filter_only_last_position(df_spacex_hst, 'id', 'creation_date')
    insert_mysql(df_spacex_hst, 'mysql-container', 'db_spacex', 'starlink_hst', 'root', '123')
    #insert_mysql(df_spacex_last_pos, 'mysql-container', 'db_spacex', 'starlink_last_position', 'root', '123')

execute_script()