# -*- coding: utf-8 -*-
"""
Created on Wed Jul  5 01:40:50 2023

@author: MIKAEL
"""

import pandas as pd
import requests
from urllib.parse import urlparse, parse_qs
from sqlalchemy import create_engine
import datetime

def getjson():
    def ext_market_id(url):
        parsed_url = urlparse(url)
        query_params = parse_qs(parsed_url.query)
        market_value = query_params.get('lid', [None])[0]
        return market_value
    
    def transform_date(row, url):
        date = row['Date'].zfill(2)
        parsed_url = urlparse(url)
        query_params = parse_qs(parsed_url.query)
        month = query_params.get('m', [None])[0].zfill(2)
        year = query_params.get('y', [None])[0]
        transformed_date = year + month + date
        return transformed_date
    
    # Existing dataframe or list of IDs
    # df_list = pd.DataFrame({'idlist': [7,8,36,37,38,39,41,3,4,21,22,23,24,25,26,27,40,9,10,28,29,30,31,32,33,34,35,1,11,12,13,14,15,16,17,18,19,20,47,48,5,6,42,43,44,45,46,49]})
    
    df_list = pd.DataFrame({'idlist': [7,8,36,37,38,39,41,3,4,21,22,23,24,25,26,27,40,9,10,28,29,30,31,32,33,34,35,1,11,12,13,14,15,16,17,18,19,20,47,48,5,6,42,43,44,45,46,49]})
    year = '2023'
    
    
    def process_urls(df_list, year):
        dfs = []  # List to store the separate dataframes
        mnth = datetime.datetime.now().month
        
        for index, row in df_list.iterrows():
            id_param = row['idlist']
            df_long_list = []  # List to store the individual market ID dataframes
            
            
            url = f'https://infopangan.jakarta.go.id/api/price/series_by_location?public=1&type=market&lid={id_param}&m={mnth}&y={year}'
                
            response = requests.get(url)
            json_data = response.json()
                
            data = json_data['data']
                
            if len(data) > 0:
                df_1 = pd.json_normalize(data)
                    
                columns_re = ['name', 'unit', 'id', 'low', 'high', 'average', 'location_name']
                df_2 = df_1.drop(columns=columns_re)
                    
                columns_ren = {
                    'commodity_id': 'CommodityID',
                    'series.1': '1',
                    'series.2': '2',
                    'series.3': '3',
                    'series.4': '4',
                    'series.5': '5',
                    'series.6': '6',
                    'series.7': '7',
                    'series.8': '8',
                    'series.9': '9',
                    'series.10': '10',
                    'series.11': '11',
                    'series.12': '12',
                    'series.13': '13',
                    'series.14': '14',
                    'series.15': '15',
                    'series.16': '16',
                    'series.17': '17',
                    'series.18': '18',
                    'series.19': '19',
                    'series.20': '20',
                    'series.21': '21',
                    'series.22': '22',
                    'series.23': '23',
                    'series.24': '24',
                    'series.25': '25',
                    'series.26': '26',
                    'series.27': '27',
                    'series.28': '28',
                    'series.29': '29',
                    'series.30': '30',
                    'series.31': '31'
                }
                
                df_2 = df_2.rename(columns=columns_ren)
                
                df_2.loc[df_2['CommodityID']=='Ayam Broiler/Ras','CommodityID']='1'
                df_2.loc[df_2['CommodityID']=='Bawang Merah','CommodityID']='2'
                df_2.loc[df_2['CommodityID']=='Bawang Putih','CommodityID']='3'
                df_2.loc[df_2['CommodityID']=='Beras IR 42/Pera','CommodityID']='4'
                df_2.loc[df_2['CommodityID']=='Beras IR. I (IR 64)','CommodityID']='5'
                df_2.loc[df_2['CommodityID']=='Beras IR. II (IR 64) Ramos','CommodityID']='6'
                df_2.loc[df_2['CommodityID']=='Beras IR. III (IR 64)','CommodityID']='7'
                df_2.loc[df_2['CommodityID']=='Beras Muncul .I','CommodityID']='8'
                df_2.loc[df_2['CommodityID']=='Beras Setra I/Premium','CommodityID']='9'
                df_2.loc[df_2['CommodityID']=='Cabe Merah Besar (TW)','CommodityID']='10'
                df_2.loc[df_2['CommodityID']=='Cabe Merah Keriting','CommodityID']='11'
                df_2.loc[df_2['CommodityID']=='Cabe Rawit Hijau','CommodityID']='12'
                df_2.loc[df_2['CommodityID']=='Cabe Rawit Merah','CommodityID']='13'
                df_2.loc[df_2['CommodityID']=='Daging Babi Berlemak','CommodityID']='14'
                df_2.loc[df_2['CommodityID']=='Daging Kambing','CommodityID']='15'
                df_2.loc[df_2['CommodityID']=='Daging Sapi Has (Paha Belakang)','CommodityID']='16'
                df_2.loc[df_2['CommodityID']=='Daging Sapi Murni (Semur)','CommodityID']='17'
                df_2.loc[df_2['CommodityID']=='Garam Dapur','CommodityID']='18'
                df_2.loc[df_2['CommodityID']=='Gas Elpiji 3kg','CommodityID']='19'
                df_2.loc[df_2['CommodityID']=='Gula Pasir','CommodityID']='20'
                df_2.loc[df_2['CommodityID']=='Ikan Bandeng (sedang)','CommodityID']='21'
                df_2.loc[df_2['CommodityID']=='Ikan Lele','CommodityID']='22'
                df_2.loc[df_2['CommodityID']=='Ikan Mas','CommodityID']='23'
                df_2.loc[df_2['CommodityID']=='Jeruk Medan','CommodityID']='24'
                df_2.loc[df_2['CommodityID']=='Kelapa Kupas','CommodityID']='25'
                df_2.loc[df_2['CommodityID']=='Kentang (sedang)','CommodityID']='26'
                df_2.loc[df_2['CommodityID']=='Margarin Blueband Cup','CommodityID']='27'
                df_2.loc[df_2['CommodityID']=='Margarin Blueband Sachet','CommodityID']='28'
                df_2.loc[df_2['CommodityID']=='Minyak Goreng (Kuning/Curah)','CommodityID']='29'
                df_2.loc[df_2['CommodityID']=='Semangka','CommodityID']='30'
                df_2.loc[df_2['CommodityID']=='Susu Bubuk Bendera 400gr','CommodityID']='31'
                df_2.loc[df_2['CommodityID']=='Susu Bubuk Dancow 400gr','CommodityID']='32'
                df_2.loc[df_2['CommodityID']=='Susu Kental Bendera 200gr','CommodityID']='33'
                df_2.loc[df_2['CommodityID']=='Susu Kental Enak 200gr','CommodityID']='34'
                df_2.loc[df_2['CommodityID']=='Telur Ayam Ras','CommodityID']='35'
                df_2.loc[df_2['CommodityID']=='Tepung Terigu','CommodityID']='36'
                df_2.loc[df_2['CommodityID']=='Tomat Buah','CommodityID']='37'
                    
                df_long = pd.melt(df_2, id_vars='CommodityID', var_name='Date', value_name='Price')
                df_long = df_long.sort_values(['CommodityID', 'Date']).reset_index(drop=True)
                    
                market_value = ext_market_id(url)
                df_long['MarketID'] = market_value
                
                df_long['Date'] = df_long.apply(lambda row: transform_date(row, url), axis=1)
                    
                df_long_list.append(df_long)  # Append the dataframe to the list
            
            if len(df_long_list) > 0:
                # Create a separate dataframe for each market ID
                df_combined = pd.concat(df_long_list)
                dfs.append(df_combined)  # Append the dataframe to the list
        
        return dfs
    
    
    # Call the function to process the URLs
    dfs = process_urls(df_list, year)
    
    # Access each dataframe individually
    merged_df = pd.concat(dfs, ignore_index=True)
    merged_df = merged_df[['MarketID', 'CommodityID', 'Date', 'Price']]
    merged_df = merged_df[~merged_df['Date'].str.contains('series', case=False)]
    last_dates = merged_df.groupby('MarketID')['Date'].max().reset_index()
    
    fil_df = merged_df.merge(last_dates, on=['MarketID', 'Date'])
    
    
    """
    MySQL Connection
    """
    
    engine = create_engine("mysql+mysqlconnector://{user}:{pw}@{host}/{db}"
                           .format(user="xxx",
                                   pw="xxx",
                                   host="xxx",
                                   db="xxx"))
    
    """
    Test Connectionz`
    """
    
    connection = engine.connect()
    
    table_name = 'allpasar'  # Replace with the desired table name
    fil_df.to_sql(table_name, con=engine, if_exists='append', index=False)
    
    connection.close()
