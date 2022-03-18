m, b = np.polyfit(np.log(test),np.log(test2),1)
log_y_fit = m*np.log(test) + b
y_fit = np.exp(log_y_fit)
print(m) #slope
print(b)
