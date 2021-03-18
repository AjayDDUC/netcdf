# from mpl_toolkits.basemap import Basemap
# import matplotlib.pyplot as plt
import pandas as pd

#DATA
path = r"C:\Users\curaj1\PycharmProjects\netcdf\csv_file_out.csv"
data = pd.read_csv(path)
print(data.columns)
print(data.size)


#VIZ
# m = Basemap()
# m.drawcoastlines()
# plt.show()