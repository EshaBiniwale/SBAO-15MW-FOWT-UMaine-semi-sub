# SBAO-15MW-FOWT-UMaine-semi-sub

The rise of floating wind technology in the last few years has been unprecedented. The main benefit being that it can be deployed in deep waters, alleviating the visual and noise pollution created by its onshore and fixed offshore counterparts. 

Currently, a major setback for floating wind is the excessive operation and maintenance costs. Reducing the cost of sub-structures would in turn help reduce the over-all costs. This report provides a framework to minimize the material costs of the mooring lines for a floating offshore wind turbine using surrogate models, a data-driven optimization project.

The considered system is the IEA 15-MW reference wind turbine installed on the UMaine VolturnUS-S reference semi-submersible platform. Given the lack of available data, a population data-set was created by varying the geometrical properties of mooring lines. A large database of HAWC2 simulation results was generated. A few key responses, namely tower top acceleration, surge, pitch and tension at the fairlead and anchor, were chosen to be investigated. The simulation outputs were used as inputs for training the surrogate model.

A deep neural network was trained to understand the relationship between the geometrical properties of the mooring system and the motion responses of the structure. These neural networks were used as the surrogate models within the optimization routine, thus, allowing the search space to be more thoroughly searched.

For the applied methodology and conditions, it is shown that the required material cost can be reduced by about 5\%, and, at the same time the performance of the ﬂoating system - expressed by the RMS of the tower-top acceleration, absolute value of maximum surge and pitch and maximum tension at the fairlead and anchor- improved in some respect.
