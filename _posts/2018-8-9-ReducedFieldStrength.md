---
layout: post
title: 'Reduced Field Strength'
---

The first part of this post highlights why the drift velocity of an ion
population depends on the applied electric field and number density for
IMS measurements. The second part examines the key scaling factor known
as field strength.

<video width="750" height="375" controls="controls">)
	<source src="/animations/IMS_Theory/E1N1.mp4" type="video/mp4">)
</video>


Electric Field $$(E)$$ and Number Density $$(N)$$
=============================================

The drift velocity of an ion population $$(v_d)$$ is dependent on the
applied electric field $$(E)$$ and number density $$(N)$$. The electric
field $$(E)$$ for a traditional linear drift tube is constant and the
number density $$(N)$$ of the drift gas is determined (under ideal
conditions) by the ideal gas law ($$PV=nRT=Nk_bT$$). A key IMS scaling
factor is known as reduced field strength $$(E/N)$$ and is an important
consideration when reporting mobility measurements.

The animations below is split into four quadrants where positively
charged ions (red diamonds) and neutrals (blue circles) are confined in
a box where only elastic collisions are considered. The ions are
initially placed in the center x-axis without any starting initial
velocity. The neutrals are dispersed in the confined box with random
starting initial velocities and positions.

<video width="750" height="375" controls="controls">)
	<source src="/animations/IMS_Theory/HighQuality_EN1.mp4" type="video/mp4">)
</video>

In the animation above, the first and second column corresponds to a
simulation in the presence of no electric field and applied constant
electric field (the direction of the field is from left to right )
respectively. Similarly, the first and second rows correspond to where
the number density is effectively reduced to zero (mimicking high vacuum
conditions) and increased number density respectively.

(top-left) no electric field and reduced number density
-------------------------------------------------------

First, we can consider the simple example when ions are confined in a
box without an applied electric field and reduced number density
highlighted in the upper left quadrant. Without any force acting on the
ions, the ions position is stationary throughout the duration of the
simulation.

(top-right) constant electric field and reduced number density
--------------------------------------------------------------

When ions are confined in a box with an applied electric field and
reduced number density highlighted in the upper right quadrant, ions
accelerate in the direction of the electric field. The potential energy
$$(E_{p})$$ of the positively charged ions in a constant electric field is
equivalent to $$E_{p}=qU$$ where $$q$$ is the charge of the ions and $$U$$ is
the voltage drop or electric potential difference. The ions accelerate
to the right side wall where the potential energy is converted to
kinetic energy ($$E_k=\frac{1}{2}m{v_d}^2$$) where $$v_d$$ is the velocity
of the ion and $$m$$ is the mass of the ion. This simulation is analogous
to time-of-flight mass spectrometry.

(bottom-left) no electric field and higher number density
---------------------------------------------------------

The kinetic energy of the neutral buffer gas is transferred to the ions
where conservation of momentum is maintained. The motion of the ions is
described by Brownian motion.

(bottom-right) constant electric field and higher number density
----------------------------------------------------------------

The simulation on the bottom-right best models that of the IMS
experiment. Ions are accelerated by the electric field but the motion is
retarded by the presence of neutrals. Although the instantaneous drift
velocity of individual ion is continually changing , the ions are
considered to reach a terminal velocity that is dependent on the
mobility of the ion population $$(K)$$.

The Key IMS Scaling Factor $$(E/N)$$
==================================

<video width="750" height="375" controls="controls">)
	<source src="/animations/IMS_Theory/HighQuality_EN2.mp4" type="video/mp4">)
</video>


Double Electric Field
---------------------

The ions travel with a higher terminal velocity $$(v_d)$$ when the
electric field is doubled proportional to the defined mobility $$(K)$$ of
the ion population.

Double Electric Field and Number Density
----------------------------------------

The reduced field strength remains constant when the number density and
electric field are doubled. The animation on the right highlights that
the terminal velocity $$(v_d)$$ of the ion population is similar to the
animation in the left.





