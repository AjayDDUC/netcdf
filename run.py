# from netCDF4 import Dataset  # use scipy instead
# from scipy.io import netcdf #### <--- This is the library to import.
from netCDF4 import Dataset
import xarray as xr
import pandas as pd

# Open file in a netCDF reader
path = r"C:\Users\curaj1\Downloads\outfile.nc"
# nc = netcdf.netcdf_file(wrf_file_name, 'r')
data = Dataset(path, mode='r')
temp = data.variables["mcape"][:]
tem = data.variables["mcape"].dimensions

print(temp.size)
# print(tem)

# for var in data.variables.values():
#     print(var)


# ds = xr.open_dataset(path)
# df = ds.to_dataframe()
# data = df.to_csv("csv_file_out.csv")
