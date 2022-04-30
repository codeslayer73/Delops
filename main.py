import sqlite3
import pandas as pd
conn = sqlite3.connect('customer_set')
c = conn.cursor()

# CREATE
c.execute(
    '''CREATE TABLE IF NOT EXISTS customer_set([customer_id] INTEGER PRIMARY KEY, [loc]TEXT NOT NULL, [wgt] INTEGER , [lat] INTEGER ,[long] INTEGER, [val] INTEGER)''')

# INSERT
c.execute(''' INSERT INTO customer_set (customer_id,loc,wgt,lat,long,val) VALUES
 (1,"Depot",35,12,15,600),
 (2,"A",45,15,20,800),
 (3,"B",25,8,19,700),
 (4,"C",34,25,17,450),
 (5,"D",65,13,26,340),
 (6,"E",20,8,30,200)''')

# Commit db
conn.commit()
# DISPLAY
c.execute('''SELECT * FROM customer_set''')
df = pd.DataFrame(c.fetchall(), columns=[
                  'customer_id', 'loc', 'wgt', 'lat', 'long', 'val'])
print(df)
df.to_csv('order.csv')
