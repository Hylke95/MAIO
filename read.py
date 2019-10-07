import numpy as np
import matplotlib.pyplot as plt

meta = np.loadtxt('iWS_collumns_output.txt',dtype=str,delimiter='\t= ')
for i in meta:
	for j in range(len(i)):
		i[j] = i[j].strip()
meta = meta.T

data = np.loadtxt('grl_aws23_ALL.txt',dtype=str).T[2:].astype(float)
for i in range(len(data)-1):
	i += 1
	dlt = data[i] > -999
	if any(dlt):
		un, cnts = np.unique(data[i][dlt],return_counts=True)
		if np.max(cnts)/np.sum(cnts) < 0.9:	#only show informative columns
			plt.figure()
			plt.plot(np.arange(len(data[i]))[dlt],data[i][dlt],'o')
			plt.xlabel('index')
			par = meta[0][i+1]
			unit = np.array(list(par)) == '['
			if any(unit):
				plt.ylabel(par[np.where(unit)[0][0]:])
			plt.title(meta[1][i+1])
			plt.grid()
plt.show()