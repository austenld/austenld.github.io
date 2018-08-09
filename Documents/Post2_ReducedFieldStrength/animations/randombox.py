"""
Animation of Elastic collisions with Gravity
#https://jakevdp.github.io/blog/2012/08/18/matplotlib-animation-tutorial/
author: Jake Vanderplas
email: vanderplas@astro.washington.edu
website: http://jakevdp.github.com
license: BSD
Please feel free to use and modify this, but keep the above information. Thanks!
"""
import numpy as np
from scipy.spatial.distance import pdist, squareform

import matplotlib.pyplot as plt
import scipy.integrate as integrate
import matplotlib.animation as animation
import matplotlib.mlab as mlab
#import ffmpeg

#ffmpeg.rcParams['animation.ffmpeg_path'] = "C:\\FFmpeg"
#10 seconds for 510 particles and 0.025 velocity (1 ion).
#25 seconds for 750 particles and 0.025 velocity (1 ion).
num_particles=1000       #500/20/0.0125 and 1000/20/0.025
num_ions=20
ion_velocity=0.0250    #0.05

class ParticleBox:
    """Orbits class
    
    init_state is an [N x 4] array, where N is the number of particles:
       [[x1, y1, vx1, vy1],
        [x2, y2, vx2, vy2],
        ...               ]

    bounds is the size of the box: [xmin, xmax, ymin, ymax]
    """
    def __init__(self,
                 init_state = [[1, 0, 0, -1],
                               [-0.5, 0.5, 0.5, 0.5],
                               [-0.5, -0.5, -0.5, 0.5]],
                 bounds = [-2, 2, -2, 2],
                 size = 0.04,
                 M = 0.05,
                 G =0):
        self.init_state = np.asarray(init_state, dtype=float)
        self.M = M * np.ones(self.init_state.shape[0])
        self.size = size
        self.state = self.init_state.copy()
        self.time_elapsed = 0
        self.bounds = bounds
        self.G = G
		

    def step(self, dt):
        """step once by dt seconds"""
        self.time_elapsed += dt
        
        # update positions
        self.state[:, :2] += dt * self.state[:, 2:]

        # find pairs of particles undergoing a collision
        D = squareform(pdist(self.state[:, :2]))
        ind1, ind2 = np.where(D < 2 * self.size)
        unique = (ind1 < ind2)
        ind1 = ind1[unique]
        ind2 = ind2[unique]

        # update velocities of colliding pairs
        for i1, i2 in zip(ind1, ind2):
            # mass
            m1 = self.M[i1]
            m2 = self.M[i2]

            # location vector
            r1 = self.state[i1, :2]
            r2 = self.state[i2, :2]

            # velocity vector
            v1 = self.state[i1, 2:]
            v2 = self.state[i2, 2:]

            # relative location & velocity vectors
            r_rel = r1 - r2
            v_rel = v1 - v2

            # momentum vector of the center of mass
            v_cm = (m1 * v1 + m2 * v2) / (m1 + m2)

            # collisions of spheres reflect v_rel over r_rel
            rr_rel = np.dot(r_rel, r_rel)
            vr_rel = np.dot(v_rel, r_rel)
            v_rel = 2 * r_rel * vr_rel / rr_rel - v_rel

            # assign new velocities
            self.state[i1, 2:] = v_cm + v_rel * m2 / (m1 + m2)
            self.state[i2, 2:] = v_cm - v_rel * m1 / (m1 + m2) 

        # check for crossing boundary
        crossed_x1 = (self.state[:, 0] < self.bounds[0] + self.size)
        crossed_x2 = (self.state[:, 0] > self.bounds[1] - self.size)
        crossed_y1 = (self.state[:, 1] < self.bounds[2] + self.size)
        crossed_y2 = (self.state[:, 1] > self.bounds[3] - self.size)

        self.state[crossed_x1, 0] = self.bounds[0] + self.size
        self.state[crossed_x2, 0] = self.bounds[1] - self.size

        self.state[crossed_y1, 1] = self.bounds[2] + self.size
        self.state[crossed_y2, 1] = self.bounds[3] - self.size

        self.state[crossed_x1 | crossed_x2, 2] *= -1
        self.state[crossed_y1 | crossed_y2, 3] *= -1

        # add gravity
        #self.state[:, 2] -= self.M * self.G * dt
        self.state[0:num_ions, 2] += ion_velocity
		


#------------------------------------------------------------
# set up initial state
np.random.seed(9)
init_state = np.random.random((num_particles, 4)) #change number of particles here.
init_state[:, 0:2] *= 4.0
init_state[:, 0:2] -= 2.0

init_state[:, 2:4] -= 0.50
init_state[0:num_ions,0]=0.0 	#First ion is not moving and centered.
init_state[0:num_ions,2:4]*=0.1 	#First ion is not moving and centered.
#init_state[0:num_ions,1:1]=-1.95 	#First ion is not moving and centered.
#init_state[0:num_ions,1:4]=0.0	#First ion is not moving and centered.

box = ParticleBox(init_state, size=0.04)
dt = 1. / 30 # 30fps


#------------------------------------------------------------
# set up figure and animation
fig = plt.figure(figsize=(5, 5))
grid = plt.GridSpec(5, 5, hspace=0.01, wspace=0.01)
#fig.subplots_adjust(left=0, right=1, bottom=0, top=1)
ax = fig.add_subplot(grid[-4:, :5], autoscale_on=False, xlim=(-2.00, 2.00), ylim=(-2, 2))
                     #xlim=(-3.2, 3.2), ylim=(-2.4, 2.4))
# particles holds the locations of the particles
ax.set_yticklabels([])
ax.set_xticklabels([])
ion_particles, = ax.plot([], [], 'rD', ms=4)
particles, = ax.plot([], [], 'bo', ms=4)
# rect is the box edge
rect = plt.Rectangle(box.bounds[::2],
                     box.bounds[1] - box.bounds[0],
                     box.bounds[3] - box.bounds[2],
                     ec='none', lw=2, fc='none')
ax.add_patch(rect)
#Add subplot
#fig_hist = plt.figure()
hist_ax = fig.add_subplot(grid[:-4, :5], autoscale_on=False,sharex=ax, ylim=(0.0, 20.0))

var_numbins=12
x_binning= np.linspace(-2.0, 2., num=var_numbins)
x_plot_binning=np.linspace(-2., 2., num=var_numbins-1) #Number is 1 less
bin_data,=hist_ax.plot([], [], 'r')

plt.legend([ion_particles, particles], ["Ions", "Neutrals"],loc=1,prop={'size': 9})

if ion_velocity<=0:
    textstr1='Electric Field\n(Off)'
elif ion_velocity<0.02:
    textstr1='Electric Field\n(On) ---> = 1x'
elif ion_velocity>=0.02:
    textstr1='Electric Field\n(On) ---> = 2x'
    
if num_particles<=500:
    textstr2='Number Density\n= 1x'
elif num_particles>500:
    textstr2='Number Density\n= 2x'

    

#ax.annotate("", xy=(0.9, 0.9), xytext=(0, 0), arrowprops=dict(arrowstyle="->"))
props = dict(boxstyle='round', facecolor='wheat', alpha=0.5)
hist_ax.text(0.10, 1.22, textstr1, transform=ax.transAxes, fontsize=7, verticalalignment='top', bbox=props, horizontalalignment='center')
hist_ax.text(0.12, 1.10, textstr2, transform=ax.transAxes, fontsize=7, verticalalignment='top', bbox=props,horizontalalignment='center')

def init():
    #"""initialize animation"""
    global box, rect
    particles.set_data([], [])   
    ion_particles.set_data([], [])
    bin_data.set_data([],[])
    rect.set_edgecolor('none')
    return particles, rect, ion_particles, bin_data

def animate(i):
    """perform animation step"""
    global box, rect, dt, ax, fig
    box.step(dt)

    #ms = int(fig.dpi * 2 * box.size * fig.get_figwidth()
    #         / np.diff(ax.get_xbound())[0])
    ms =4
    rect.set_edgecolor('k')	
    particles.set_data(box.state[num_ions:, 0], box.state[num_ions:, 1])
    ion_particles.set_data(box.state[0:num_ions, 0], box.state[0:num_ions, 1])
    
    list_bin_data=[]
    for j in range(len(x_binning)-1):
        count=0
        for k in range(num_ions):
            if box.state[k, 0]>x_binning[j]:
                if box.state[k, 0]<x_binning[j+1]:
                    count+=1
        list_bin_data.append(count)
    bin_data.set_data(x_plot_binning, list_bin_data)
    
    textstr3='%.2f' % (float((i+1)/30.0))
    textstr3="Time: "+ textstr3+' s'
    for txt in ax.texts:
        txt.set_visible(False)
    props = dict(boxstyle='round', facecolor='wheat', alpha=1)
    textvar=ax.text(0.02, 0.95, textstr3, transform=ax.transAxes, fontsize=7, verticalalignment='top', bbox=props,horizontalalignment='left')

    
    #ax_hist.hist(box.state[0:num_ions, 0])
    #fig_hist.remove()
    #digitized = np.digitize(box.state[0:num_ions, 0], bins)
    #bin_means = [box.state[0:num_ions, 0][digitized == i].mean() for i in range(1, len(bins))]
    #ax_hist.hist(digitized)
    
    #plot.hist(ion_particles.set_data(box.state[0:num_ions, 0],density=1, bins=5) 
   # plot.axis([-2, 2, 0, 20]) 
    #particles.set_markersize(ms)
    #ion_particles.set_markersize(ms)
    return particles, rect, ion_particles


ani = animation.FuncAnimation(fig, animate, frames=360, interval=1, blit=True, init_func=init)
# save the animation as an mp4.  This requires ffmpeg or mencoder to be
# installed.  The extra_args ensure that the x264 codec is used, so that
# the video can be embedded in html5.  You may need to adjust this for
# your system: for more information, see
# http://matplotlib.sourceforge.net/api/animation_api.html
#mywriter = animation.FFMpegWriter()
ani.save('diffusion.mp4', dpi=150,fps=30)
plt.show()
#plt.close(fig)
