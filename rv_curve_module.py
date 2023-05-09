import numpy as np
import matplotlib.pylab as plt

class rv_curve_class:
    
    """
    We know the orbital parameters of the planet and the Doppler 
    semi-amplitude that the planet imprints in the star.
    Time of periastron passage, t0
    Orbital Period, p
    Orbital Eccentricity, e
    Angle of periastron passage, w
    Doppler semi-amplitude, k
    We can also indicate two times t_init, t_end, in which our star will be observed,
    and the number of points npts to use to create our data.
    """
    
    def __init__(self, t0, p, e, w, k, t_init=0, t_end=25,npts=1000):
        # Asking all the input variables as attributes of the class
        self.t0 = t0
        self.p = p
        self.e = e
        self.w = w
        self.k = k
        self.t_init = t_init
        self.t_end = t_end
        self.npts = npts
        # We can create a new attribute using previous attributes
        self.t_vector = np.linspace(self.t_init, self.t_end, npts)    # get time vector

    
    # method to compute the true anomaly from the mean anomaly
    def true_anomaly(self):
        mean = 2. * np.pi * (self.t_vector - self.t0) / self.p   # mean anomaly
        true = mean + self.e * np.sin(mean)          # initial guess for true anomaly
        f = true - self.e * np.sin(true) - mean      # first value of function f
        for i in range(len(self.t_vector)):                     # iterate for all the values
            while np.abs(f[i]) > 1e-6:              # Newton-Raphson condition
                f[i] = true[i] - self.e * np.sin(true[i]) - mean[i]  # calculate f
                df = 1. - self.e * np.cos(true[i])  # calculate df
                true[i] = true[i] - f[i]/df         # update the eccentric anomaly
        eimag = np.sqrt(1. - self.e*self.e) * np.sin(true)    # calculate imaginary part of eccentric anomaly
        ereal = np.cos(true) - self.e                         # calculate real part of eccentric anomaly
        true = np.arctan2(eimag, ereal)                       # get true anomaly from eccentric anomaly
        return true
    

    # function to compute the radial velocity curve
    def rv_curve(self):
        # Note how when we call the true_anomaly method, we do not need to give any input parameter
        # All the parameters are attributes of the instance, so they are used in the method computationscre
        nu = self.true_anomaly()                         # get true anomaly from true_anomaly function
        # Note how we can add the rv attribute to the instance
        self.rv = self.k * np.cos(nu + self.w) + self.e * np.cos(self.w)  # compute RV curve

    # Let's create a new method to plot the light curve
    def plot(self):  
        #Let us compute the curve
        self.rv_curve()
        # plot the RV curve
        plt.plot(self.t_vector, self.rv)
        plt.xlabel("Time [d]")
        plt.ylabel("RV [m/s]")
        plt.show()

