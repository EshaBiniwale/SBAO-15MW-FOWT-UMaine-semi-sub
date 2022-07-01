import numpy as np
import pandas as pd 

wdepth = 200.0                                  # water depth
R_fairlead = 58.0                               # radius from origin to fairlead (in xy-plane)
mooring_seabed = 10.0

L_value_list = []
R_anchor_value_list = []
z_fairlead_value_list = []

for L in range(800, 901, 10):                       #specify range for unstretched length of mooring line
    for R_anchor in range(800, 901, 10):            #specify range for radius from origin to anchor (in xy-plane)
        for z_fairlead in range(0, 20):             #specify range for z-pos of fairlead
            L_value_list.append(L)
            R_anchor_value_list.append(R_anchor)
            z_fairlead_value_list.append(z_fairlead)


d = {'L_values': L_value_list, 'R_anchor': R_anchor_value_list, 'z_fairlead': z_fairlead_value_list}
df = pd.DataFrame(data=d)

df = df.rename_axis('File_ID')

df["Disrupt Constraint"] = np.where(df['L_values'] >= (mooring_seabed + np.sqrt((df['R_anchor']-mooring_seabed-R_fairlead)**2 + (wdepth - df['z_fairlead'])**2)), 'Pass', 'Fail')

df.groupby(["Disrupt Constraint"])["Disrupt Constraint"].count()
df.to_csv('L_R_z_values.csv')

df_clean = df.loc[df['Disrupt Constraint'] == 'Pass'].reset_index()

# df_clean.to_csv('L_R_z_values_pass.csv', index=False)