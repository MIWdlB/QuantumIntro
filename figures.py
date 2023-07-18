import numpy as np
import matplotlib.pyplot as plt
#Get absolute maxes for axis ranges to center origin
#This is optional
fig = plt.figure(figsize=(6,6))
ax = fig.add_subplot(autoscale_on=False, xlim=(-1,4), ylim=(-1,4))
ax.set_aspect('equal')


ax.arrow(0,0,2.,2., color='blue', linewidth=2)
ax.arrow(0.,0,3,0., color='r', linewidth=2)
# ax.arrow(3,0,-1.5,1.5, color='black', linestyle=':', linewidth=2)

ax.plot(0,0,'ok') #<-- plot a black point at the origin
ax.grid(which='major') #<-- plot grid lines
# plt.gca.set_aspect('equal', adjustable='box')
fig.savefig('images/fig1.png', dpi=90, bbox_inches='tight')

fig = plt.figure(figsize=(6,6))
ax = fig.add_subplot(autoscale_on=False, xlim=(-1,4), ylim=(-1,4))
ax.set_aspect('equal')


ax.arrow(0,0,2.,2., color='blue', linewidth=1)
ax.arrow(0.,0,3,0., color='r', linewidth=1)
ax.arrow(3,0,-1.5,1.5, color='black', linestyle=':', linewidth=2)

ax.plot(0,0,'ok') #<-- plot a black point at the origin
ax.grid(which='major') #<-- plot grid lines
# plt.gca.set_aspect('equal', adjustable='box')
fig.savefig('images/fig2.png', dpi=90, bbox_inches='tight')

fig = plt.figure(figsize=(6,6))
ax = fig.add_subplot(autoscale_on=False, xlim=(-1,4), ylim=(-1,4))
ax.set_aspect('equal')


ax.arrow(0,0,2.,2., color='blue', linewidth=1)
ax.arrow(0.,0,3,0., color='r', linewidth=1)
ax.arrow(3,0,-1.5,1.5, color='black', linestyle=':', linewidth=2)
ax.arrow(0,0,1.5,1.5, color='black', linestyle='-', linewidth=2)

ax.plot(0,0,'ok') #<-- plot a black point at the origin
ax.grid(which='major') #<-- plot grid lines
# plt.gca.set_aspect('equal', adjustable='box')
fig.savefig('images/fig3.png', dpi=90, bbox_inches='tight')