---
layout: post
title: Introduction IMS Theory
---

[comment]: <> (http://www.gastonsanchez.com/visually-enforced/opinion/2014/02/16/Mathjax-with-jekyll/)
[comment]: <> (http://dasonk.com/blog/2012/10/09/Using-Jekyll-and-Mathjax)
This is an introduction to the basics of ion mobility spectrometry (IMS).
The purpose of this page is to introduce you to the concept of IMS and how ions behave in neutral gasses.
The structure and content of this page is based upon lecture slides written by Dr. Bill Siems.

### Parameters of IMS
First, we need to establish the variables which will be discussed in further detail.
#### Instrument-State Variables: $$(L, V, E)$$ and $$(N, T, P)$$:

$$L$$ is the length of the drift space and $$V$$ is the voltage drop across the drift space.
The electric field is such that $$E=\dfrac{V}{L}$$.
$$N$$ is the number density of the drift gas and if the drift gas is ideal then $$N=N_0\cdot \dfrac{P\cdot T_0}{P_0\cdot T}$$.
Where $$T_0=273.15K, P_0= 760\;\text{torr, and}  N_0=2.687\cdot10^{19} \text{cm}^3$$ (the number density of an ideal gas at STP.

#### Mass Parameters: $$(m, M,q=Ze)$$:

$$m$$ and $$M$$ correspond to the ion and drift gas masses respectively and $q$ corresponds to the charge of the ion.

#### Measured Quantity: $$(t_d, v_d)$$:

$$t_d$$ is the drift time required for an ion swarm to traverse $$L$$.
The drift velocity ($$v_d$$) of an ion swarm is therefore $$v_d=\dfrac{L}{t_d}$$

### Ion Mobility
There is a very important variable to understand and that is the mobility $$(K)$$ of an ion swarm.
The central observation is that if an electric field $$(E)$$ is applied to ions dispersed in gas, the ions move with a characteristic average terminal velocity in the direction of the field.
This terminal velocity is called the drift velocity $$(v_d)$$.
The mobility $$K$$ is defined as the ratio of the velocity to the field strength and is traditionally reported in units of cm$$^2$$V$$^{-1}$$sec$$^{-1}$$.

$$K=\dfrac{v_d}{E}$$

### Five Underlying Assumptions
1. $$n << N$$: Ions have a much lower number density then neutrals.
    1. Mutual coulombic repulsion of ions unimportant
	2. Ion-ion collisions unimpportant
	3. Each neutral encounters 0 ions or 1 ion during a mobility experiment.
2. Collisions are instantaneous
3. Three-body collisions are rare.
    1. Dense fluids are excluded from consideration
4. Ions reach a terminal $$v_d=KE$$.
    1. Vacuum and  “low” pressures excluded from consideration.
5. Ion-neutral reactions and clustering may be ignored



<video width="480" height="320" controls="controls">)
  <source src="/animations/IMS_Theory/diffusion.mp4" type="video/mp4">)
</video>)