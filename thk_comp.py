import netCDF4 as nc4
import matplotlib.pyplot as plt
from mpl_toolkits.basemap import Basemap
import numpy as np
from matplotlib import colors
from mpl_toolkits.axes_grid1 import ImageGrid
import sys

#Import nc file
ifile = nc4.Dataset('mod_v_obs.nc')
#Import ice thickness
var = ifile.variables['thk']
#Import grounding lines & ice extent
new_gl = ifile.variables['mask']
old_gl = ifile.variables['ctrl_mask']

lon = np.squeeze(ifile.variables['lon'])
lat = np.squeeze(ifile.variables['lat'])
thk = np.squeeze(ifile.variables['thk'])

x = ifile.variables['x'] [:]
y = ifile.variables['y'] [:]
width = x.max() - x.min()
height = y.max() - y.min()

#Set mapping conditions
m = Basemap(resolution='l',projection='spstere',lat_ts=ifile.variables['mapping'].standard_parallel,boundinglat=-64,lon_0=0)
#Mask null values
var2=np.ma.masked_values(var,0.0)
#Convert to lat lon
xx,yy = m(lon, lat)

#Plot map
m.pcolormesh(xx,yy,var2,vmin=-1500, vmax=1500)
#Add colour bar
plt.colorbar(ticks=[-1400,-1200,-1000,-800,-600,-400,-200,0,200,400,600,800,1000,1200,1400], format="%d",label='Change in ice thickness (m)')
#Set colours
plt.set_cmap('bwr_r')

#Add grounding line and ice extent as contour
plt.contour(xx,yy,old_gl[0],3,colors=('k','k','k',(1,1,1)),linewidths=(1.5,1.5,1.5))

plt.contour(xx,yy,new_gl[0],3,colors=('0.55','0.55','0.55',(1,1,1)),linewidths=(1.5,1.5,1.5))

#Add lat lon lines & labels
#m.drawparallels(np.arange(-80.,81.,10.), labels = [0, 0, 0, 0], dashes=[6,1],linewidth=0,xoffset=0.1,yoffset=0.1)
#m.drawmeridians(np.arange(-180.,181.,45.), labels = [1, 0, 0, 0], dashes=[6,1],linewidth=0,xoffset=0.1,yoffset=0.1)

#Flip image (can be done using NCO)
plt.gca().invert_yaxis()
plt.gca().invert_xaxis()

#plt.title("Ice Thickness (m)")
plt.show()

