"""
Example on how to use the 'calc_cops' function to get the
COPs of an exemplary ground-source heat pump (GSHP).

We use the soil temperature as low temperature heat reservoir.
"""

import oemof.thermal.compression_heatpumps_and_chillers as cmpr_hp_chiller
import pandas as pd
import os

# set path
path_data= r'C:\Users\Stefanie.nguyen\git\COP_calculation\oemof-thermal\examples\compression_heatpump_and_chiller'
# Precalculation of COPs
cops_GSHP = cmpr_hp_chiller.calc_cops(
    temp_high=[37.43],
    temp_low=[10],
    quality_grade=0.53,
    mode='heat_pump')

GSHP_dict={'ground_temperature':[10],
           'temperature_sink':[37.43],
           'COP':cops_GSHP}

data=pd.DataFrame(GSHP_dict)
#data.to_csv(os.path.join(os.path.dirname(__file__) , 'data/results/2021-03-16_GSHP_COP.csv'))
