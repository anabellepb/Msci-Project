import math
import numpy as np
import matplotlib.pyplot as plt



E = np.linspace(0.1, 1.5,15,endpoint=True)    #  E for DOS(E)


h = 6.582*10**(-16)               # hbar (eV/s)
v = 5*10**(5)                     # Fermi velocity of Bi2Se3 (m/s)
L = 10**(-7)                    # Dimension of an LxL Bi2Se3 sample (m)
a = 4.1*10**(-10)                 # Lattice spacing for Bi2Se3  (m) 
Gamma = 0.015                  # Lorentzian scale parameter

kx = np.arange((-(math.pi)/a), ((math.pi)/a), (2*(math.pi)/L))     # Values of kx ((2pim_x)/L) in first BZ
ky = np.arange((-(math.pi)/a), ((math.pi)/a), (2*(math.pi)/L))     # Values of ky ((2pim_x)/L) in first BZ
kx2 = np.square(kx)                                          # Squares all kx
ky2 = np.square(kx)                                          # Squares all ky
k2 = [i + j for j in kx2 for i in ky2]                       # Creates the grid of all kx2 + ky2 
k = np.sqrt(k2)                                              # Returns array of positive square roots of kx2

Ek = [i * (h*v) for i in k]  # Calculates Ek for positive half of Dirac-cone
print()


for i in E:
    DOSel = [((10**14)*Gamma)/ ((i - j)**(2) + (Gamma)**(2)) for j in Ek] 
    DOS = np.sum(DOSel) 
    AnDOS = 2*i/ ((math.pi)*(h)**(2)*(v)**(2))
    print('The code has calculated  DOS (',+ round(i, 2),'eV) =', + DOS, 'eV^-1 m^-2')
    print('The analytical value is  DOS (',+ round(i, 2),'eV) =', + AnDOS, 'eV^-1 m^-2')
    print()
                               

     # Multiply by 2 to account for negative half od the Dirac-cone
     

#print('The analtical value is DOS(',+ E,'eV) =', + AnDOS) # per eV per m^2
#print('The code has calculated DOS(',+ E,'eV) =', + DOS) # per eV per m^2
#print (len(kx))              
#print (len(ky))
#print (len(k2))
#print (len(k))
#print (len(Ek))



