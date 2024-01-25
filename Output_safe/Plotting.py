import numpy as np
import matplotlib.pyplot as plt
import pandas as pd


fo2 = np.array([-4,-2,-1,0,2,3,4,5])

f =[]
f2=[]
emm =[]
emm2 =[ ]
for i in range(len(fo2)):
    try:
        data = pd.read_csv(f'/Users/rahularora/Desktop/study_material/Papers PhD/EVo/Output/{fo2[i]}_1200K_500bar_-2.0_-3.0_-4.0_-5.0.csv')
        f.append(fo2[i])
        emm.append((np.array(data['mSO2'])[-1]+np.array(data['mH2S'])[-1]))
        #plt.plot(fo2[i],(np.array(data['fSO2'])[-1]+np.array(data['fH2S'])[-1])*3.4e6*6.022e23/(4*np.pi*(6.378e+8**2)))
        #print((np.array(data['fSO2'])[-1]+np.array(data['fH2S'])[-1])*3.4e6*6.022e23/(4*np.pi*(6.378e+8**2)))
    except:
        continue

for i in range(len(fo2)):
    try:
        data = pd.read_csv(f'/Users/rahularora/Desktop/study_material/Papers PhD/EVo/Output/{fo2[i]}_1200K_1bar_-2.0_-3.0_-4.0_-5.0.csv')
        f2.append(fo2[i])
        emm2.append((np.array(data['mSO2'])[-1]+np.array(data['mH2S'])[-1]))
        #plt.plot(fo2[i],(np.array(data['fSO2'])[-1]+np.array(data['fH2S'])[-1])*3.4e6*6.022e23/(4*np.pi*(6.378e+8**2)))
        #print((np.array(data['fSO2'])[-1]+np.array(data['fH2S'])[-1])*3.4e6*6.022e23/(4*np.pi*(6.378e+8**2)))
    except:
        continue

plt.plot(f2,emm2,'.-',label = '1 bar')
plt.plot(f,emm,'.-',label = '500 bar')
plt.legend()
plt.show()    