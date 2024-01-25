from glob import glob
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd


files = ['/Users/rahularora/Desktop/Project/Papers PhD/EVo/Output/arc.csv']

if(len(files) != 0):
    for j in range(len(files)):
        data = pd.read_csv(files[j])
        mgas = np.array(data['Gas_wt'])[-1]/100
        mu = np.array(data['mol_mass'])[-1]
        ngas = mgas/mu
        wt = np.array(data['rho_melt'])[-1]*1e9*3
        print(np.array([np.array(data['mCO2'])[-1],np.array(data['mH2O'])[-1],np.array(data['mSO2'])[-1],np.array(data['mN2'])[-1]])*ngas*wt)
        print(np.array([np.array(data['mCO2'])[-1],np.array(data['mH2O'])[-1],np.array(data['mSO2'])[-1],np.array(data['mN2'])[-1]])*2/np.array(data['mCO2'])[-1])
        