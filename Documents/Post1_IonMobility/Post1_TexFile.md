###  Introduction IMS Theory

This is an introduction to the basics of ion mobility spectrometry (IMS). The purpose of this page is to introduce you to the concept of IMS and how ions behave in neutral gasses. The structure and content of this page is based upon lecture slides written by Dr. Bill Siems.
	
####  Variables in IMS

Here we introduce the commonly referenced variables which will be discussed in further detail. These variables are grouped into three categories: instrument-state, mass, and measured quantities.

\subsubsection{Instrument-State Variables: $(L, V, E)$ and $(N, T, P)$}
$L$ is the length of the drift space and $V$ is the voltage drop across the drift space. The electric field for a traditional linear drift tube is constant and equivalent to $E=\frac{V}{L}$. $N$ is the number density of the drift gas. If the drift gas is considered ideal then $N=N_0\cdot \dfrac{P\cdot T_0}{P_0\cdot T}$, where $T_0=273.15$K, $P_0= 760\;$torr, and  $N_0=2.687\cdot10^{19} \text{cm}^3$ (the number density of an ideal gas at STP).
	\subsubsection{Mass Parameters: $(m, M,q=Ze)$}
		$m$ and $M$ correspond to the ion and drift gas masses respectively and $q$ corresponds to the charge of the ion.
	
	\subsubsection{Measured Quantities: $(t_d, v_d)$}

	
	$t_d$ is the drift time required for an ion swarm to traverse the length of the drift space $L$. This terminal velocity is called the drift velocity $(v_d)$. The drift velocity of a given ion population is equivalent to $v_d=\dfrac{L}{t_d}$ where the length is often predetermined and the drift time is measured.
	
	###  Ion Mobility Spectrometry

	The mobility $(K)$ of an ion swarm is important and related to the drift velocity of an ion.
	\begin{equation}
		K=\frac{v_d}{E}
	\end{equation}
	The central observation is that if an electric field $(E)$ is applied to ions dispersed in gas, the ions move with a characteristic average terminal velocity $(v_d)$ in the direction of the field. The mobility $K$ is defined as the ratio of the velocity to the field strength and is traditionally reported in units of cm$^2$V$^{-1}$sec$^{-1}$.
	
	
	####  Five Underlying Assumptions of IMS

	

1.  $n << N$: Ions have a much lower number density then neutrals (additionally, mutual coulombic repulsion of ions is unimportant, ion-ion collisions unimpportant, and each neutral encounters 0 or 1 ion during a mobility experiment).
1.  Collisions are instantaneous.
1.  Three-body collisions are rare.
1.   Ions reach a terminal velocity defined by $v_d=KE$.:  Vacuum and  ''low'' pressures excluded from consideration
1.  Ion-neutral reactions and clustering may be ignored (in real experiments clustering is common).

	
	####  Key IMS Scaling Factor ($E/N$- Reduced Field Strength)

	
	$E/N$ is known as the reduced field strength. Experimentally, $K$ is understood to be constant at low reduced field strengths. We shall now see why this parameter is useful by observing from this simulation the effect of varying the reduced field strength $(E/N)$.
	
	####  No Electric Field

	First, we can consider the effect when ions are confined in a box in the presence of neutrals without the presence of an electric field.
	
	%<video width="480" height="320" controls="controls">)
	%<source src="/animations/IMS_Theory/NoEfield.mp4" type="video/mp4">)
	%</video>
	
	%The ions behave similarily to that of the neutral gasses.
	
%	Now we demonstrate the effect when the electric field is constant and where voltage is decreasing in the direction from left to right.
	%<video width="480" height="320" controls="controls">)
	%<source src="/animations/IMS_Theory/Efield1xN1x.mp4" type="video/mp4">)
	%</video>
	
	%When the number density is doubled without changing the electric field setting from previous, the ions travel slower
	%<video width="480" height="320" controls="controls">)
	%<source src="/animations/IMS_Theory/Efield1xN2x.mp4" type="video/mp4">)
%	</video>
	
%	The electric field setting is now doubled.
%	<video width="480" height="320" controls="controls">)
%	<source src="/animations/IMS_Theory/Efield2xN2x.mp4" type="video/mp4">)
%	</video>