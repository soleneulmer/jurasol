import numpy as np
import matplotlib.pylab as plt

#Create a function that computes the Radial Velocity curve
#We know the orbital parameters of the planet and the Doppler semi-amplitude that the planet imprints in the star.
#Time of periastron passage, t0
#Orbital Period, p
#Orbital Eccentricity, e
#Angle of periastron passage, w
#Doppler semi-amplitude, k
#We also know two times t_init, t_end, in which our star will be observed.
t0 = 0. #days but typically Barycentre Julian Date (BJD) 
p  = 122. #days
e  = 0.75 
w  = np.pi/3
k  = 10 #m/s
t_init = 10 #days
t_end = 205 #days

#Create a function that computes the Radial Velocity curve
#input parameters: t_init(float), t_end(float), t0 (float), 
#    p (float), e(float), w(float), k(float), npts (integer,optional) 
#output: t_vector, rv (array) --> The time and RV of the curve we want to plot 
def rv_curve(t_init,t_end,t0,p,e,w,k,npts=1000):
    t_vector = np.linspace(t_init,t_end,npts)
    rv = k * np.cos(nu + w) + e * np.cos(w)
    return t_vector, rv

time, rv = rv_curve(t_init,t_end,t0,p,e,w,k)
