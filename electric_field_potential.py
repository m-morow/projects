#Calculate and plot electric potential and field of two charges (-q, +q) 0.05m apart

def electric_potential(q, x1, y1, x2, y2):
  return q/(4*np.pi*(8.854e-12)*(np.sqrt((x1-x2)**2 + (y1-y2)**2)))

dy = []
dx = []
p1_x = -0.05 #charge 1 x-coordinate
p2_x = 0.05 #charge 2 x-coordinate
p1_y = 0 #charge 1 y-coordinate
p2_y = 0 #charge 2 y-coordinate
y, x = np.mgrid[0.5:-0.5:100j, 0.5:-0.5:100j]
dy, dx = np.gradient(electric_potential(1, x, y, p1_x, p1_y)
                    + electric_potential(-1, x, y, p2_x, p2_y)) #gradient using axis as partials

fig, ax = plt.subplots()
#Set up plot 1 (quiver plot)
ax.quiver(x, y, dx, dy, electric_potential(1, x, y, p1_x, p1_y)
                        + electric_potential(-1, x, y, p2_x, p2_y))
plt.title("Quiver Plot of electric field for two charges")
plt.xlabel("X [m]")
plt.ylabel("Y [m]")
plt.show()

#Set up plot 2 (stream plot)
plt.streamplot(x, y, dx, dy, density=2)
plt.title("Electric field for two charges")
plt.xlabel("X [m]")
plt.ylabel("Y [m]")
plt.show()
