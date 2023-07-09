# -*- coding: utf-8 -*-
"""
Created on Sat Jul  8 20:59:51 2023

@author: MIKAEL
"""

import pandas as pd
from sqlalchemy import create_engine

def db_load_pasardki():
    # Step 2: Create SQLAlchemy engine
    engine = create_engine("mysql+mysqlconnector://{user}:{pw}@{host}/{db}"
                           .format(user="xxx",
                                   pw="xxx",
                                   host="xxx",
                                   db="pasardkidb"))

    # Step 3: Establish database connection
    with engine.connect() as connection:
        query = """
            SELECT ml.MarketName, cl.Commodity, al.Date, al.Price
            FROM marketlist AS ml
            JOIN allpasar AS al ON al.MarketID = ml.MarketID
            JOIN commoditylist AS cl ON al.CommodityID = cl.CommodityID
        """

        # Step 4: Execute the query and fetch the result into a pandas DataFrame
        df = pd.read_sql_query(query, connection)

    return df

