import pandas as pd
from scipy.spatial import distance_matrix

dfs = pd.read_csv('del_order.csv', index_col=0)
df1 = dfs[dfs['Possible_in_delbox'] == 1]
print("Following is the delivery list after bin optimizing:")
print(df1)
x = df1['lat'].tolist()
y = df1['long'].tolist()
data = list(zip(x, y))
print("2D Matrix of (Latitude,Longitude):")
print(data)
#data = [[0, 0], [5, 7], [7, 3], [8, 1], [6, 4]]
#ctys = ['Depot', 'A', 'B', 'C', 'D']
ctys = df1['loc']
df = pd.DataFrame(data, columns=['xcord', 'ycord'], index=ctys)
dist_mat = pd.DataFrame(distance_matrix(
    df.values, df.values), index=df.index, columns=df.index)
print(df)
print("Succesfully created the distance matrix for routing!!!!")
print(dist_mat)
print("Storing distance matrix......")
dist_mat.to_csv('dist_mat.csv')
print("completed!!!")
