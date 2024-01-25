import numpy as np
import time
import os

fo2 = np.arange(-4,6,1)
T = np.arange(1073,1973,50)
pressure = 1
wh20 = np.logspace(-2,-1,4) 
wco2 = np.logspace(-5,-2,10)
ws = np.logspace(-4,np.log10(3.33e-3),4)
wn = np.logspace(-7,-5,3)
float_formatter = "{:.8f}".format
'''
T=[1200]
wh20 =[0.01]
wco2=[0.001]
ws =[0.0001]
wn=[0.00001]
'''
Env = open('./env.dat','r+')
env_data = Env.readlines()
Env.close()
for i in range(len(fo2)):
    for j in range(len(T)):
        for k in range(len(wh20)):
            for l in range(len(wco2)):
                for m in range(len(ws)):
                    for n in range(len(wn)):
                        tot_m = 1
                        env_data[59] = f'FO2_buffer_START: {fo2[i]}\n'
                        env_data[19] = f'T_START: {T[j]}\n'
                        env_data[95] = f'WTH2O_START: {float_formatter(wh20[k]/tot_m)}\n'
                        env_data[98] = f'WTCO2_START: {float_formatter(wco2[l]/tot_m)}\n'
                        env_data[101] = f'SULFUR_START: {float_formatter(ws[m]/tot_m)}\n'
                        env_data[104] = f'NITROGEN_START: {float_formatter(wn[n]/tot_m)}\n'
                        env_data[5] = f'FILE_NAME: \'{fo2[i]}_{T[j]}K_{pressure}bar_{np.log10(wh20[k])}_{np.log10(wco2[l])}_{np.log10(ws[m])}_{np.log10(wn[n])}\'\n'
                        env_yaml = open('./env.yaml','w+')
                        for p in range(len(env_data)):
                            env_yaml.writelines(env_data[p])

                        env_yaml.close()

                        
                        print(i,j,k,l,m,n)
                        os.system('python3 dgs.py chem.yaml env.yaml --output output.yaml')

