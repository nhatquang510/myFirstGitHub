import matplotlib.pyplot as plt
import numpy as np

center_of_circle = (1, 1)

figure, axes = plt.subplots()
Drawing_uncolored_circle = plt.Circle( center_of_circle, 1, fill = False )
axes.set_aspect(1)
plt.xlim(-2, 13)
plt.ylim(-2, 13)
axes.add_artist( Drawing_uncolored_circle )
#axes.add_artist( Drawing_O )

theta = np.linspace(0, 2*np.pi, 13)
x = np.cos(theta) + center_of_circle[0]
y = np.sin(theta) + center_of_circle[1]

S = (sum(x) - x[0], sum(y) - y[0])

for i in range(12):
    plt.plot([0, x[i]], [0, y[i]], 'b', marker = 'o')

plt.plot([0, S[0]], [0, S[1]], 'r', marker = 'o')

#i = 0
#axes.add_artist(plt.Circle( (x[i], y[i]), 0.03) )


plt.title( 'Circle' )
plt.show()
print("second commit")
#change in code