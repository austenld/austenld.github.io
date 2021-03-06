---
layout: post
title: Electric field and number density
---

The first part of this post demonstrates why the drift velocity of an ion population
depends on the applied electric field and number density in context
of IMS. The second part examines the key scaling factor known as field
strength and its relation to drift velocity.

<video width="750" height="375" controls="controls">)
	<source src="/animations/IMS_Theory/E1N1.mp4" type="video/mp4">)
</video>

Electric Field $$(E)$$ and Number Density $$(N)$$
=============================================

The drift velocity of an ion population $$(v_d)$$ is dependent on the
applied electric field $$(E)$$ and number density $$(N)$$. The electric
field $$(E)$$ for a traditional linear drift tube is constant and the
number density $$(N)$$ of the drift gas is determined (under ideal
conditions) by the ideal gas law ($$PV=nRT=Nk_bT$$).

The animations below is split into four quadrants where positively
charged ions (red diamonds) and neutrals (blue circles) are confined in
the box where only elastic collisions are hereby considered. The ions
are initially placed in the center x-axis with a starting initial
velocity of zero. The neutrals are dispersed in the confined box with
random starting initial velocities and positions.

<video width="750" height="375" controls="controls">)
	<source src="/animations/IMS_Theory/HighQuality_EN1.mp4" type="video/mp4">)
</video>


In the animation above, the first and second column corresponds to a
simulation in the presence of no applied electric field and applied constant
electric field (the direction of the field is from left to right )
respectively. Similarly, the first row corresponds to where the number
density is effectively reduced to zero (mimicking high vacuum
conditions) and the second row includes the presence of neutrals and
thereby increase the number density of gas molecules.

(top-left) no electric field and reduced number density
-------------------------------------------------------

First, we can consider the simple example when ions are confined in the
box without an applied electric field and reduced number density
highlighted in the upper left quadrant. Without any force acting on the
ions, the ions position is stationary throughout the duration of the
simulation.

(top-right) constant electric field and reduced number density
--------------------------------------------------------------

When ions are confined in the box with an applied electric field
highlighted in the upper right quadrant, ions accelerate in the
direction of the electric field. The potential energy $$(E_{p})$$ of the
positively charged ions in a constant electric field is equivalent to
$$E_{p}=qU$$ where $$q$$ is the charge of the ion and $$U$$ is the voltage
difference or electric potential difference. The ions accelerate to the
right side wall where the potential energy is converted to kinetic
energy ($$E_k=\frac{1}{2}m{v_d}^2$$) where $$v_d$$ is the velocity of the
ion and $$m$$ is the mass of the ion. In this example, $$v_d$$ for each ion
is increasing until the ions collide on the right side wall of the box.
This simulation is analogous to time-of-flight mass spectrometry where
the arrival time of ions is dependent upon the mass, and charge, and
applied electric field; the collisions with neutrals in high vacuum
conditions are rare and often ignored.

(bottom-left) no electric field and higher number density
---------------------------------------------------------

The kinetic energy of the neutral buffer gas is transferred to the ions
where conservation of momentum is maintained. The motion of the ions can
be described as Brownian motion.

(bottom-right) constant electric field and higher number density
----------------------------------------------------------------

The simulation on the bottom-right best models that of the IMS
experiment. Ions are accelerated by the electric field but the motion is
retarded by the presence of neutrals. Although the instantaneous drift
velocity of individual ion is continually changing , the ions are
considered to reach an average terminal velocity $$(v_d)$$ that is
dependent on the interactions between the ions and buffer gas in
addition to the influence of the electric field and ion. The drift
velocity of an ion population ($$v_d$$) is related to the mobility of the
same ion population $$(K)$$ under a constant electric field $$(E)$$ from the
equation $$v_d=KE$$.

The Key IMS Scaling Factor $$(E/N)$$
==================================

A key IMS scaling factor is reduced field strength $$(E/N)$$ and is an
important consideration when reporting mobility measurements. $$E/N$$ is
commonly reported in literature as Townsends (Td), where
$$1 \;\text{Td} = 10^{-17}\;\text{V}\; \text{cm}^2$$. When $$E$$ and $$N$$ are
both multiplied by some constant $$(\delta)$$, the drift velocity of the
ion population $$(v_d)$$ is unaffected (ignoring three-body collisions).
Under low-field conditions, the mobility of an ion population ($$K$$) is
*nearly* invariant to $$E/N$$.

The bottom-right quadrant of the animation shown previously is now
located in the top-left corner of the animation provided below. The left
and right columns correspond to multiplying $$E$$ by a constant $$\delta=1$$
and $$\delta=2$$ respectively where the ion acceleration is multiplied by
the equivalent factor $$\delta$$. The top and bottom rows in the animation
below correspond to multiplying $$N$$ by the constant $$\delta=1$$ and
$$\delta=2$$ respectively where multiplying the number density ($$N$$) by
the constant $$\delta$$ reduces the distance to the next collision by the
same factor $$\delta$$.


<video width="750" height="375" controls="controls">)
	<source src="/animations/IMS_Theory/HighQuality_EN2.mp4" type="video/mp4">)
</video>

The animation shown above demonstrate the similar arrival time
distributions for the top-left and bottom-right quadrant where
multiplying both $$E$$ and $$N$$ by the constant $$\delta$$ keeps $$E/N$$ and
$$v_d$$ constant.



