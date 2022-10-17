## Importing packages
import pandas as pd
from dotenv import load_dotenv
from sqlalchemy import create_engine
import os

## Loading environment variables
load_dotenv()

## Defining Login Credentials
mysql_host = os.getenv("HOSTNAME_SQL")
mysql_user = os.getenv("USERNAME_SQL")
mysql_password = os.getenv("PASSWORD_SQL")
mysql_database = os.getenv("DATABASE_SQL")

## Defining Connection String
connection = f'mysql+pymysql://{mysql_user}:{mysql_password}@{mysql_host}/{mysql_database}'
db = create_engine(connection)

## Defining Query
query = 'SELECT * FROM db2.table2;'
query

df = pd.read_sql(query, con=db)

## Creating dataframe
real_df = pd.read_csv('https://raw.githubusercontent.com/hantswilliams/HHA-507-2022/main/descriptive/example1/data/data.csv')
real_df

## Importing dataframe to mySQL
real_df.to_sql('table2', con=db, if_exists='replace', index=False)

## Testing query results
sql_query = """ SELECT * FROM table3 WHERE age = '47' """;
results_47 = pd.read_sql(sql_query, con=db)
results_47

df = pd.read_sql("""
SELECT * FROM db2.table2;""", con=db)