import numpy as np
import matplotlib.pyplot as plt
import os.path
import pandas as pd


fo2 = np.arange(-4 ,6,1)
T = np.arange(1073,1973,50)
pressure = 1
wh20 = np.logspace(-5,-1,13) 
wco2 = np.logspace(-5,-2,10)
ws = np.logspace(-4,np.log10(3.33e-3),4)
wn = np.logspace(-6,-5,3)

fo2 = np.arange(0 ,6,1)
T = np.arange(1073,1973,50)
pressure = 1
wh20 = 10**(np.array([-2.3333333333333335,-2]))
wco2 = np.logspace(-4,-2.3333333333333335,6)[2:]
ws = np.logspace(-4,np.log10(3.33e-3),4)[2:]
wn = np.logspace(-6,-5,3)

print(wh20,wco2,ws,wn)

molecules = ['H2O','H2','O2','CO2','CO','CH4','SO2','H2S','S2','N2']
'''
data = np.ndarray(shape = (len(molecules),len(fo2),len(T),len(wh20),len(wco2),len(ws),len(wn)))

filemis = open('./missing.txt','w+')


for i in range(len(fo2)):
    for j in range(len(T)):
        for k in range(len(wh20)):
            for l in range(len(wco2)):
                for m in range(len(ws)):
                    for n in range(len(wn)):
                        if os.path.isfile(f'./Output/{fo2[i]}_{T[j]}K_{pressure}bar_{np.log10(wh20[k])}_{np.log10(wco2[l])}_{np.log10(ws[m])}_{np.log10(wn[n])}.csv'):
                            file = pd.read_csv(f'./Output/{fo2[i]}_{T[j]}K_{pressure}bar_{np.log10(wh20[k])}_{np.log10(wco2[l])}_{np.log10(ws[m])}_{np.log10(wn[n])}.csv')
                            mgas = np.array(file['Gas_wt'])[-1]/100
                            mu = np.array(file['mol_mass'])[-1]
                            ngas = mgas*6.022e23/mu
                            for p in range(len(molecules)):
                                data[p,i,j,k,l,m,n] = ((np.array(file[f'm{molecules[p]}'])[-1])*ngas*9e13/(3.154e+7*(4*np.pi*6.378e8**2)))
                        else:
                            data[:,i,j,k,l,m,n] = 0
                            filemis.writelines(f'{i}  {j}  {k}  {l}  {m}  {n}\n')

filemis.close()

np.save('./emission.npy',data)

'''

data = np.load('./emission.npy')

fig, axs = plt.subplots(2, 1,figsize= (20,13))

for j in range(1):
    data1 = [np.ndarray.flatten(data[i,:,:,j,1,1,1]) for i in range(len(molecules))]

    print(np.shape(data1))
    for i in range(len(data1)):
        data1[i] = data1[i][data1[i]!=0]
    print(data1)    
    if(len(data1[0])!=0):
        axs[0].violinplot(data1,vert =True)
        axs[0].set_yscale('log')
        axs[0].set_xticks(np.arange(1, len(molecules) + 1))
        axs[0].set_xticklabels(molecules)
        axs[0].title.set_text(f'{np.log10(wh20[j])}')
        axs[0].set(ylabel ='Emission flux (molecule/cm^2)')
        axs[0].set_ylim(1e-12,1e12)

for j in range(1):
    data1 = [np.ndarray.flatten(data[i,:,:,1+j,1,1,1]) for i in range(len(molecules))]

    print(np.shape(data1))
    for i in range(len(data1)):
        data1[i] = data1[i][data1[i]!=0]
    if(len(data1[0])!=0):
        axs[1].violinplot(data1,vert =True)
        axs[1].set_yscale('log')
        axs[1].set_xticks(np.arange(1, len(molecules) + 1))
        axs[1].set_xticklabels(molecules)
        axs[1].title.set_text(f'{np.log10(wh20[1+j])}')
        axs[1].set(ylabel ='Emission flux (molecule/cm^2)')
        axs[1].set_ylim(1e-12,1e12)
#plt.xticks(ticks=np.arange(1, len(molecules) + 1),labels=molecules)
plt.savefig('./Plots/violin_h2o.png')
plt.clf()

fig, axs = plt.subplots(2, 2,figsize= (20,20))

for j in range(2):
    data1 = [np.ndarray.flatten(data[i,:,:,1,j,1,1]) for i in range(len(molecules))]

    print(np.shape(data1))
    for i in range(len(data1)):
        data1[i] = data1[i][data1[i]!=0]
    if(len(data1[0])!=0):
        axs[j,0].violinplot(data1,vert =True)
        axs[j,0].set_yscale('log')
        axs[j,0].set_xticks(np.arange(1, len(molecules) + 1))
        axs[j,0].set_xticklabels(molecules)
        axs[j,0].title.set_text(f'{np.log10(wco2[j])}')
        axs[j,0].set_ylim(1e-12,1e12)

for j in range(2):
    data1 = [np.ndarray.flatten(data[i,:,:,1,2+j,1,1]) for i in range(len(molecules))]

    print(np.shape(data1))
    for i in range(len(data1)):
        data1[i] = data1[i][data1[i]!=0]
    if(len(data1[0])!=0):
        axs[j,1].violinplot(data1,vert =True)
        axs[j,1].set_yscale('log')
        axs[j,1].set_xticks(np.arange(1, len(molecules) + 1))
        axs[j,1].set_xticklabels(molecules)
        axs[j,1].title.set_text(f'{np.log10(wco2[2+j])}')
        axs[j,1].set_ylim(1e-12,1e12)
#plt.xticks(ticks=np.arange(1, len(molecules) + 1),labels=molecules)
plt.savefig('./Plots/violin_co2.png')
plt.clf()

fig, axs = plt.subplots(2, 1,figsize= (20,20))

for j in range(2):
    data1 = [np.ndarray.flatten(data[i,:,:,1,2,j,1]) for i in range(len(molecules))]

    print(np.shape(data1))
    for i in range(len(data1)):
        data1[i] = data1[i][data1[i]!=0]
    if(len(data1[0])!=0):
        axs[j].violinplot(data1,vert =True)
        axs[j].set_yscale('log')
        axs[j].set_xticks(np.arange(1, len(molecules) + 1))
        axs[j].set_xticklabels(molecules)
        axs[j].title.set_text(f'{np.log10(ws[j])}')
        axs[j].set_ylim(1e-12,1e12)

plt.savefig('./Plots/violin_s.png')
plt.clf()

fig, axs = plt.subplots(3, 1,figsize= (20,13))

for j in range(3):
    data1 = [np.ndarray.flatten(data[i,:,:,1,2,1,j]) for i in range(len(molecules))]

    print(np.shape(data1))
    for i in range(len(data1)):
        data1[i] = data1[i][data1[i]!=0]
    if(len(data1[0])!=0):
        axs[j].violinplot(data1,vert =True)
        axs[j].set_yscale('log')
        axs[j].set_xticks(np.arange(1, len(molecules) + 1))
        axs[j].set_xticklabels(molecules)
        axs[j].title.set_text(f'{np.log10(wn[j])}')
        axs[j].set_ylim(1e-12,1e12)

plt.savefig('./Plots/violin_n.png')
plt.clf()

'''
for j in range(3):
    data1 = [np.ndarray.flatten(data[i,:,:,5,6+j,2,2]) for i in range(len(molecules))]

    print(np.shape(data1))
    for i in range(len(data1)):
        data1[i] = data1[i][data1[i]!=0]
    if(len(data1[0])!=0):
        axs[j,2].violinplot(data1,vert =True)
        axs[j,2].set_yscale('log')
        axs[j,2].set_xticks(np.arange(1, len(molecules) + 1))
        axs[j,2].set_xticklabels(molecules)
        axs[j,2].title.set_text(f'{np.log10(wco2[6+j])}')
#plt.xticks(ticks=np.arange(1, len(molecules) + 1),labels=molecules)
plt.savefig('./Plots/violin_co2.png')


f,t,h,c,s,n = np.loadtxt('./missing.txt',unpack=True)


total = 11664/len(fo2)
print(f'total = {total}')
for i in range(len(fo2)):
    #print(T[i])
    print(total - len(f[f==i]))

'''