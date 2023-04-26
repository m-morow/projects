# Error propagation code for RBS data
# mmtan@umich.edu 2023
# Adapted from JC IBA_error_propagation.m

import numpy as np
import pandas as pd
np.set_printoptions(precision=3)
pd.set_option("display.precision", 3)

# REFERENCE SAMPLE (this is 2019 TBCL)--------------------
N_a0 = 411
N_r0 = 26517
err_a0 = np.sqrt(N_a0)
err_r0 = np.sqrt(N_r0)
X0 = N_a0/N_r0
err_X0 = X0 * np.sqrt((err_a0/N_a0)**2 + (err_r0/N_r0)**2)

# SAMPLES--------------------
  # if there are multiple samples, separate values by a comma
N_aligned = np.array([486, 1396, 783])
N_random = np.array([22232, 22047, 21495])

# INITIALIZE MATRIX
sh_a = np.shape(N_aligned)
sh_r = np.shape(N_random)
sh_NdN = np.zeros(sh_a, )
sh_Xmin = np.zeros(sh_a, )
sh_NdN_err = np.zeros(sh_a, )
sh_err_align = np.zeros(sh_a, )
sh_err_rand = np.zeros(sh_a, )

matrix = (np.matrix([N_aligned, N_random, sh_Xmin, sh_err_align, sh_err_rand, 
                     sh_NdN, sh_NdN_err])).T

# CALCULATIONS--------------------
for r in range(sh_a[0]):
  err_align = np.sqrt(matrix[r,0])
  matrix[r,3] = err_align

  err_rand = np.sqrt(matrix[r,1])
  matrix[r,4] = err_rand
  
  Xmin = matrix[r,0]/matrix[r,1]
  matrix[r,2] = Xmin

  err_Xmin = Xmin * np.sqrt((err_align/matrix[r,0])**2 +
                            (err_rand/(matrix[r,1]))**2)
  Xdif = Xmin - X0
  err_Xdif = np.sqrt((err_Xmin)**2 + (err_X0)**2)

  NdN = (Xmin-X0)/(1-X0)
  matrix[r,5] = NdN

  err_NdN = NdN * np.sqrt((err_Xdif/Xdif)**2 + (err_X0/(1-X0))**2)
  matrix[r,6] = err_NdN

# PRINT MATRIX--------------------
df = pd.DataFrame(matrix, columns=['Aligned counts', 'Random counts', 'Xmin', 
                                   'Aligned error', 'Random error', 'Nd/N', 
                                   'Nd/N error'])
df