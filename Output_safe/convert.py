import numpy as np
import matplotlib.pyplot as plt
import pandas as pd


data = pd.read_csv('/Users/rahularora/Desktop/study_material/Papers PhD/EVo/Output/dgs_output_basalt_COHS_closed_1473K.csv')

mol = ['H2','O2','H2O','CO2','CO','CH4','SO2','H2S','S2']
mass = [18,2,32,44,28,16,64,36,63,28]
mu_g = np.array(data['mol_mass'])[-1]*1000
alpha = np.array(data['Gas_wt'])[-1]*10/mu_g

mu_melt=64.52
alpha_melt = ((1-(np.array(data['Gas_wt'])[-1]/100))*1000)/mu_melt
#alpha = alpha /(alpha+alpha_melt)
q = np.zeros(len(mol))
for i in range(len(mol)):
    name= 'm'+mol[i]
    q[i] = np.array(data[name])[-1]*alpha

#print(q*1e-3*np.array(data['rho_melt'])[-1]*25e9*3.154e+7*6.022e23/(4*np.pi*(6.378e+8**2)))

q = np.zeros(len(mol))
#print((alpha/(mu_melt*(1-alpha))))
for i in range(len(mol)):
    name= 'm'+mol[i]
    q[i] = np.array(data[name])[-1]*3.4e6*6.022e23/(4*np.pi*(6.378e+8**2))

print(q*1)

tableau20 = [(31, 119, 180),(255, 127, 14),(44, 160, 44),(214, 39, 40),(148, 103, 189),(140, 86, 75), (227, 119, 194),(127, 127, 127),(188, 189, 34),(23, 190, 207),\
(174, 199, 232),(255, 187, 120),(152, 223, 138),(255, 152, 150),(197, 176, 213),(196, 156, 148),(247, 182, 210),(199, 199, 199),(219, 219, 141),(158, 218, 229)] 
# 


# Scale the RGB values to the [0, 1] range, which is the format matplotlib accepts.    
for i in range(len(tableau20)):    
    r, g, b = tableau20[i]    
    tableau20[i] = (r / 255., g / 255., b / 255.)


fig, ax = plt.subplots(nrows=2, ncols=1, sharex=True, figsize=(8, 9),gridspec_kw={'height_ratios': [2,1]})


plot_mol = ['H2','H2O','CO2','CO','SO2','H2S','S2']
lab_mol = [r'H$_2$',r'H$_2$O',r'CO$_2$',r'CO',r'SO$_2$',r'H$_2$S',r'S$_2$']


for i in range(len(plot_mol)):
    name= 'm'+plot_mol[i]
    ax[0].plot(np.array(data['P']),np.array(data[name]),color = tableau20[i],label = f'{lab_mol[i]}',linewidth =2.5)

ax[1].plot(np.array(data['P']),np.array(data['Exsol_vol%']),color = 'black',linewidth =2.5)

ax[0].axvline(x=1,color = 'black')
ax[1].axvline(x=1,color = 'black')

ax[1].set_xlabel('Pressure (bar)',fontsize=28)
ax[0].set_ylabel('Degassed mole fraction',fontsize=25)
ax[1].set_ylabel('Exsolve %',fontsize=28)

plt.gca().invert_yaxis()    
ax[0].set_xscale('log')
ax[0].set_yscale('log')
ax[0].set_ylim(1e-5,3)
ax[0].set_xlim(2000,0.1)
ax[1].set_ylim(0,100)
for a in ax.flatten():
    a.tick_params(axis='both', which='major', labelsize=25)
    a.tick_params(axis='both', which='minor', labelsize=22)

plt.rc('legend',fontsize=20)
ax[0].legend(loc='lower right',ncol =2 )
#ax[1].legend(loc='lower right')

plt.savefig('/Users/rahularora/Desktop/study_material/Papers PhD/EVo/Output/spec_evo.pdf', bbox_inches='tight')

print(6.93769688e+09+3.13633287e+08)