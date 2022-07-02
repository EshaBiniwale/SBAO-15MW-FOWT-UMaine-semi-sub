# SBAO-15MW-FOWT-UMaine-semi-sub

The rise of floating wind technology in the last few years has been unprecedented. The main benefit being that it can be deployed in deep waters, alleviating the visual and noise pollution created by its onshore and fixed offshore counterparts. 

Currently, a major setback for floating wind is the excessive operation and maintenance costs. Reducing the cost of sub-structures would in turn help reduce the over-all costs. In this thesis, a data driven framework is created to to minimize the material cost of the mooring system, by optimising the geometry of the mooring system, while also meeting the stability requirements of the floating structure.

The considered system is the IEA 15-MW reference wind turbine installed on the UMaine VolturnUS-S reference semi-submersible platform. Given the lack of available data, a population data-set was created by varying the geometrical properties of mooring lines. A large database of HAWC2 simulation results was generated. A few key responses, namely tower top acceleration, surge, pitch and tension at the fairlead and anchor, were chosen to be investigated. The simulation outputs were used as inputs for training the surrogate model.

The high-fidelity simulations performed in HAWC2 are accurate, but have a high computation cost, which makes it difficult to use in design optimization where a large number of simulations are to be performed. This thesis replaces this high-fidelity simulation with a surrogate model to decrease the computation cost, thus aiding in the design optimization. Here, the surrogate model used is neural networks (NNs). A deep neural network was trained to understand the relationship between the geometrical properties of the mooring system and the motion responses of the structure. 


<img width="944" alt="SBAO workflow" src="https://user-images.githubusercontent.com/107720902/176894309-2ba35551-15c7-4dfa-afb4-6e010531236c.png">


The key stages of the surrogate based optimization followed are illustrated in the figure above. In the first step, a number of combination of decision variables (population data-set) was created. Step two consists of running the fully coupled high-fidelity simulation by using the decision variables as input along with a predefined wind input and an irregular wave input. In step three, i.e, the optimization - an ANN was used to build the surrogate model, using the decision variables and the selected responses obtained from the simulation. A gradient-based optimization routine was then implemented to search for a new, better design. 

For the applied methodology and conditions, it is shown that the required material cost can be reduced by about 5\%, and, at the same time the performance of the ﬂoating system - expressed by the RMS of the tower-top acceleration, absolute value of maximum surge and pitch and maximum tension at the fairlead and anchor- improved in some respect.
