import netCDF4 as nc4
import matplotlib.pyplot as plt
from mpl_toolkits.basemap import Basemap
import numpy as np
from matplotlib import colors
from mpl_toolkits.axes_grid1 import ImageGrid
import sys


ifile = nc4.Dataset('s0_uni_end.nc')
var = ifile.variables['usurf']
var2 = ifile.variables['gl_mask']
var3 = ifile.variables['ctrl_mask']
var4=np.ma.masked_values(var,0.0)

lon = np.squeeze(ifile.variables['lon'])
lat = np.squeeze(ifile.variables['lat'])
thk = np.squeeze(ifile.variables['thk'])

x = ifile.variables['x'] [:]
y = ifile.variables['y'] [:]

m = Basemap(resolution='l',projection='spstere',lat_ts=ifile.variables['mapping'].standard_parallel,boundinglat=-60,lon_0=0)

xx,yy = m(lon, lat)

m.pcolormesh(xx,yy,var4[0],vmin=0, vmax=4000)
plt.colorbar(extend='both', ticks=[100,500, 1000, 1500, 2000, 2500,3000, 3500,4000], format="%d", label='Ice surface elevation (m.a.s.l)')
plt.set_cmap('Blues_r')

plt.contour(xx,yy,var[0],colors='#D0D1D3',linewidths=0.5)
plt.contour(xx,yy,var3[0],colors='#D0D1D3',linewidths=0.6)
plt.contour(xx,yy,var2[0],colors='k',linewidths=0.25)

parallels = np.arange(-80.,81.,10.)
m.drawparallels(parallels, labels = [0, 0, 0, 0],color='#A5A5A5')
m.drawmeridians(np.arange(-180.,181.,45.), labels = [1, 1, 0, 0],color='#A5A5A5')

plt.gca().invert_yaxis()
plt.gca().invert_xaxis()

#plt.title("Ice Thickness (m)")
plt.show()

