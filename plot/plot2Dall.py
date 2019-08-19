import numpy as np
import matplotlib.pyplot as plt

# Set the plotting range and step for tick marks
wmin=1400
wmax=1600
step=50
title=True
save=True

# Set plotting range and axis info
plt.rcParams['axes.linewidth'] = 2
plt.rcParams['xtick.major.size']=8
plt.rcParams['ytick.major.size']=8
plt.rcParams['xtick.major.width']=2
plt.rcParams['ytick.major.width']=2
plt.rcParams['xtick.direction']='in'
plt.rcParams['ytick.direction']='in'

# Read parallel data
Data = np.loadtxt('2D.par.dat')

w1Dim=int(np.sqrt(len(Data[:,0])))
w3Dim=w1Dim

Iso=Data[:,3]
Ani=Data[:,3]
mmax=np.max(np.abs(Data[:,3]))
Data[:,3]=Data[:,3]/mmax
Data[1,3]=1
Data[2,3]=-1

w1 = np.reshape(Data[:,0],(w1Dim,w3Dim))
w3 = np.reshape(Data[:,1],(w1Dim,w3Dim))
PlotMap = np.reshape(Data[:,3],(w1Dim,w3Dim))

# Plot parallel data
fig=plt.figure()
plt.contourf(w1,w3,PlotMap,20,cmap=plt.cm.bwr)
plt.xlabel('$\omega_1$ [cm$^{-1}$]',fontsize=16)
plt.ylabel('$\omega_3$ [cm$^{-1}$]',fontsize=16)
plt.gca().set_aspect('equal')
plt.xlim(wmin,wmax)
plt.ylim(wmin,wmax)
if title:
  plt.title('Parallel polarization')
plt.plot([ wmin , wmax],[wmin,wmax],color='black')
plt.xticks(np.arange(wmin,wmax+1,50),fontsize=12,rotation=0)
plt.yticks(np.arange(wmin,wmax+1,50),fontsize=12,rotation=0)
plt.show()
if save:
  fig.savefig("2D.par.eps")

# Read perpendicular data
Data = np.loadtxt('2D.per.dat')

w1Dim=int(np.sqrt(len(Data[:,0])))
w3Dim=w1Dim

Iso=Iso+Data[:,3]*2
Ani=Ani-Data[:,3]
mmax=np.max(np.abs(Data[:,3]))
Data[:,3]=Data[:,3]/mmax
Data[1,3]=1
Data[2,3]=-1

w1 = np.reshape(Data[:,0],(w1Dim,w3Dim))
w3 = np.reshape(Data[:,1],(w1Dim,w3Dim))
PlotMap = np.reshape(Data[:,3],(w1Dim,w3Dim))

# Plot perpendicular data
fig=plt.figure()
plt.contourf(w1,w3,PlotMap,20,cmap=plt.cm.bwr)
plt.xlabel('$\omega_1$ [cm$^{-1}$]',fontsize=16)
plt.ylabel('$\omega_3$ [cm$^{-1}$]',fontsize=16)
plt.gca().set_aspect('equal')
plt.xlim(wmin,wmax)
plt.ylim(wmin,wmax)
if title:
  plt.title('Perpendicular polarization')
plt.plot([ wmin , wmax],[wmin,wmax],color='black')
plt.xticks(np.arange(wmin,wmax+1,50),fontsize=12,rotation=0)
plt.yticks(np.arange(wmin,wmax+1,50),fontsize=12,rotation=0)
plt.show()
if save:
  fig.savefig("2D.per.eps")

Data[:,3]=Iso
mmax=np.max(np.abs(Data[:,3]))
Data[:,3]=Data[:,3]/mmax
Data[1,3]=1
Data[2,3]=-1

w1 = np.reshape(Data[:,0],(w1Dim,w3Dim))
w3 = np.reshape(Data[:,1],(w1Dim,w3Dim))
PlotMap = np.reshape(Data[:,3],(w1Dim,w3Dim))

# Plot isotropic data
fig=plt.figure()
plt.contourf(w1,w3,PlotMap,20,cmap=plt.cm.bwr)
plt.xlabel('$\omega_1$ [cm$^{-1}$]',fontsize=16)
plt.ylabel('$\omega_3$ [cm$^{-1}$]',fontsize=16)
plt.gca().set_aspect('equal')
plt.xlim(wmin,wmax)
plt.ylim(wmin,wmax)
if title:
  plt.title('Isotropic polarization')
plt.plot([ wmin , wmax],[wmin,wmax],color='black')
plt.xticks(np.arange(wmin,wmax+1,50),fontsize=12,rotation=0)
plt.yticks(np.arange(wmin,wmax+1,50),fontsize=12,rotation=0)
plt.show()
if save:
  fig.savefig("2D.iso.eps")

Data[:,3]=Ani
mmax=np.max(np.abs(Data[:,3]))
Data[:,3]=Data[:,3]/mmax
Data[1,3]=1
Data[2,3]=-1

w1 = np.reshape(Data[:,0],(w1Dim,w3Dim))
w3 = np.reshape(Data[:,1],(w1Dim,w3Dim))
PlotMap = np.reshape(Data[:,3],(w1Dim,w3Dim))

# Plot anisotropic data
fig=plt.figure()
plt.contourf(w1,w3,PlotMap,20,cmap=plt.cm.bwr)
plt.xlabel('$\omega_1$ [cm$^{-1}$]',fontsize=16)
plt.ylabel('$\omega_3$ [cm$^{-1}$]',fontsize=16)
plt.gca().set_aspect('equal')
plt.xlim(wmin,wmax)
plt.ylim(wmin,wmax)
if title:
  plt.title('Anisotropic polarization')
plt.plot([ wmin , wmax],[wmin,wmax],color='black')
plt.xticks(np.arange(wmin,wmax+1,50),fontsize=12,rotation=0)
plt.yticks(np.arange(wmin,wmax+1,50),fontsize=12,rotation=0)
plt.show()
if save:
  fig.savefig("2D.ani.eps")

# Load cross polarization data
Data = np.loadtxt('2D.cro.dat')

w1Dim=int(np.sqrt(len(Data[:,0])))
w3Dim=w1Dim

AbsDat=np.sqrt(Data[:,2]**2+Data[:,3]**2)
Data[:,3]=AbsDat

mmax=np.max(np.abs(Data[:,3]))
Data[:,3]=Data[:,3]/mmax
Data[1,3]=1
Data[2,3]=-1

w1 = np.reshape(Data[:,0],(w1Dim,w3Dim))
w3 = np.reshape(Data[:,1],(w1Dim,w3Dim))
PlotMap = np.reshape(Data[:,3],(w1Dim,w3Dim))

# Plot cross polarization data
fig=plt.figure()
plt.contourf(w1,w3,PlotMap,20,cmap=plt.cm.bwr)
plt.xlabel('$\omega_1$ [cm$^{-1}$]',fontsize=16)
plt.ylabel('$\omega_3$ [cm$^{-1}$]',fontsize=16)
plt.gca().set_aspect('equal')
plt.xlim(wmin,wmax)
plt.ylim(wmin,wmax)
if title:
  plt.title('Abs. val. cross polarization')
plt.plot([ wmin , wmax],[wmin,wmax],color='black')
plt.xticks(np.arange(wmin,wmax+1,50),fontsize=12,rotation=0)
plt.yticks(np.arange(wmin,wmax+1,50),fontsize=12,rotation=0)
plt.show()
if save:
  fig.savefig("2D.abscro.eps")
