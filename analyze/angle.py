import numpy as np
import matplotlib.pyplot as plt

# This scripts analyze the angle between two chromophores assuming they
# lead to two well isolated diagonal peaks and corresponding cross peaks
# Equation 5.31 of Hamm and Zanni is used:
# Szzzz/3Szzxx=(4P2+5)/(10-P2)=R
# P2=(3cos2Theta-1)/2 (Eq. 5.29)
# R*(10-P2)=4P2+5
# 10*R-5=(4+R)*P2
# P2=(10*R-5)/(4+R)
# cos(Theta)=sqrt((2*P2+1)/3)

print("\nDetermining the angle between transition dipoles.")
print("Using method of Chem. Phys., 266, 273–284 (2001).")
print("\n")
delta=4

# Load data
# Read parallel data
Data = np.loadtxt('2D.par.dat')
w1Dim=int(np.sqrt(len(Data[:,0])))
w3Dim=w1Dim
Par = np.reshape(Data[:,3],(w1Dim,w3Dim))

# Read perpendicular data
Data = np.loadtxt('2D.per.dat')
w1Dim=int(np.sqrt(len(Data[:,0])))
w3Dim=w1Dim
Per = np.reshape(Data[:,3],(w1Dim,w3Dim))

w1 = np.reshape(Data[:,0],(w1Dim,w3Dim))
w3 = np.reshape(Data[:,1],(w1Dim,w3Dim))

# Identify main peaks
# Extract diagonal
diagonal=np.diag(Par)
grad=np.zeros(w1Dim-2)
# Find gradient
for i in range(w1Dim-2):
  grad[i]=diagonal[i+2]-diagonal[i]
# Identify peaks
peak=[]
for i in range(w1Dim-3):
  # Find maxima/minima
  if grad[i]*grad[i+1]<-1:
    # Select for bleach
    if diagonal[i+2]<0:
      peak.append(i+2)

# Analyse cross peaks if there is more than one peak
peaks=len(peak)
if peaks>1:
  for i in range(peaks):
    for j in range(peaks):
      if not (i==j):
        print("Cross peak at w1=" + str(w1[peak[i],peak[j]]) + " cm-1 and w3=" + str(w3[peak[i],peak[j]]) + " cm-1")
        Szzzz=0
        Szzxx=0
        for k in [-delta,0,delta]:
          for l in [-delta,0,delta]:
            Szzzz=Szzzz+Par[peak[i]+k,peak[j]+l]
            Szzxx=Szzxx+Per[peak[i]+k,peak[j]+l]
 
        R=Szzzz/3/Szzxx
        P2=(10*R-5)/(4+R)
        if P2<-0.5:
          P2=-0.5
        cosT=np.sqrt((2*P2+1)/3)
        Theta=np.arccos(cosT)*180/np.pi

        print("Angle found to be " + str(Theta) + " degrees.")

print("using square boxes with width of " +str(w1[2+delta,0]-w1[0,0])+" cm-1 for analysis.")
print("If this is larger than the anharmonicity or linewidth lower the variable delta.")
print("The recommended value is in the range cloe to the peak FWHM.\n")
