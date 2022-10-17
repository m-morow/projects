#Create diffraction figures {plot; simulated diffraction pattern on screen}
#Integration method (Gaussian quadrature) using Mark Newman's code

######################################################################
#
# Functions to calculate integration points and weights for Gaussian
# quadrature
#
# x,w = gaussxw(N) returns integration points x and integration
#           weights w such that sum_i w[i]*f(x[i]) is the Nth-order
#           Gaussian approximation to the integral int_{-1}^1 f(x) dx
# x,w = gaussxwab(N,a,b) returns integration points and weights
#           mapped to the interval [a,b], so that sum_i w[i]*f(x[i])
#           is the Nth-order Gaussian approximation to the integral
#           int_a^b f(x) dx
#
# This code finds the zeros of the nth Legendre polynomial using
# Newton's method, starting from the approximation given in Abramowitz
# and Stegun 22.16.6.  The Legendre polynomial itself is evaluated
# using the recurrence relation given in Abramowitz and Stegun
# 22.7.10.  The function has been checked against other sources for
# values of N up to 1000.  It is compatible with version 2 and version
# 3 of Python.
#
# Written by Mark Newman <mejn@umich.edu>, June 4, 2011
# You may use, share, or modify this file freely
#
######################################################################

from numpy import ones,copy,cos,tan,pi,linspace

def gaussxw(N):

    # Initial approximation to roots of the Legendre polynomial
    a = linspace(3,4*N-1,N)/(4*N+2)
    x = cos(pi*a+1/(8*N*N*tan(a)))

    # Find roots using Newton's method
    epsilon = 1e-15
    delta = 1.0
    while delta>epsilon:
        p0 = ones(N,float)
        p1 = copy(x)
        for k in range(1,N):
            p0,p1 = p1,((2*k+1)*x*p1-k*p0)/(k+1)
        dp = (N+1)*(p0-x*p1)/(1-x*x)
        dx = p1/dp
        x -= dx
        delta = max(abs(dx))

    # Calculate the weights
    w = 2*(N+1)*(N+1)/(N*N*(1-x*x)*dp*dp)

    return x,w

def gaussxwab(N,a,b):
    x,w = gaussxw(N)
    return 0.5*(b-a)*x+0.5*(b+a),0.5*(b-a)*w

def gauss_quad(func, N, a, b, q_func, x_in):
  xs, weights = gaussxwab(N, a, b)
  s = 0

  for i in range(N):
    s += weights[i]*func(xs[i], q_func, x_in)

  return s
######################################################################

def q(u): #transmission function
  if u < -50e-6:
    return 0
  elif -50e-6 < u < -30e-6:
    return 1
  elif -30e-6 < u < 30e-6:
    return 0
  elif 30e-6 < u < 40e-6:
    return 1
  else:
    return 0

def I_integrand(u, q_func, xs): #integrand of intensity function
  return cmath.exp((1j*2*np.pi*x*u)/(500e-9*1))*np.sqrt(q_func(u))

def I(x, q_func): #intensity function
  sep = 20e-6
  w = 10*sep
  integrand = gauss_quad(I_integrand, 100, -w/2, w/2, q_func, x)
  return np.abs(integrand)**2

#Set up plot 1 (plot)
width = 10e-2
xs = np.linspace(-width/2, width/2, 200)
vals = []

for x in xs:
  vals = np.append(vals, I(x, q))

plt.title("Intensity of diffraction pattern")
plt.xlabel("Distance from central axis [m]")
plt.ylabel("Intensity [W/m^2]")
plt.plot(xs, vals)
plt.show()

#Set up plot 2 (simulated diffraction pattern on screen)
Z = np.zeros((10, 200)) #essentially set size of plot

for i in range(10): #how "tall" stripes will be
  Z[i, :] = vals

fig, ax = plt.subplots()
plt.title("Simulated diffraction pattern on screen")
plt.xlabel("Distance from central axis [m]")
ax.set_xticks([0, 50, 100, 150, 200])
ax.set_xticklabels(["-0.05", "-0.025", "0", "0.025", "0.05"])
plt.yticks([])
plt.pcolormesh(Z)
plt.show()
