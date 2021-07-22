"""
Example on how to use the 'calc_cops' function to get the
COPs of an exemplary air-source heat pump (ASHP) and use the
pre-calculated COPs in a solph.Transformer.

We use the ambient air as low temperature heat reservoir.
"""

import os
import oemof.thermal.compression_heatpumps_and_chillers as cmpr_hp_chiller
import pandas as pd
import numpy as np
from datetime import datetime

# set path
path_data= r'C:\Users\Stefanie.nguyen\git\COP_calculation\oemof-thermal\examples\compression_heatpump_and_chiller\data'

#read raw data
def read_heat_pump_data(path, id_number):
    data= 'geo_center_station_{}.csv'.format(id_number)
    geo_station_id = pd.read_csv(os.path.join(path, data),delimiter=';')

    return geo_station_id

data = read_heat_pump_data(path=path_data, id_number='1270')

#Convert date to date time format
date_time=[]
for int in data['MESS_DATUM']:
    entry=str(int)
    datetimeobject = datetime.strptime(entry,'%Y%m%d%H')
    newformat = datetimeobject.strftime('%Y-%m-%d %H:%M:%S')
    date_time.append(newformat)

#Set up new dataframe and set index
ambient_temp = data['TT_TU'].tolist()
station_id = data['STATIONS_ID'].tolist()
temp_sink_list = list(np.ones(len(data))*37.43)
dataDict = {'date_time': date_time,
            'station_id': station_id,
            'ambient_temperature': ambient_temp,
            'temperature_sink': temp_sink_list}
data = pd.DataFrame(dataDict).set_index('date_time')

#Filter relevant data
if '2016-01-01 00:00:00' in data.index:
    data_reduct = data.loc['2016-01-01 00:00:00':'2017-01-01 00:00:00'].reset_index()
    #print(data_reduct)
else:
    raise Exception('Date time range does not exist. Please try another data set.')

dataframe = pd.concat([data_reduct['date_time'],
                       data_reduct['ambient_temperature'],
                       data_reduct['temperature_sink']], axis=1).set_index('date_time')

#if ambient temperature is higher than 20°C, set temperature sinks to 46.9°C for warm water use only
dataframe.loc[dataframe.ambient_temperature > 20, 'temperature_sink'] = 46.9

# Precalculation of COPs
cops_ASHP = cmpr_hp_chiller.calc_cops(
    temp_high=dataframe['temperature_sink'],
    temp_low=dataframe['ambient_temperature'],
    quality_grade=0.4030,
    mode='heat_pump')

COP=pd.DataFrame(cops_ASHP, data_reduct['date_time'], columns=['COP'])

#pre processing sink temperature
list_temp_low = dataframe['ambient_temperature'].values.tolist()  # External temperature of evaporator
list_temp_medium = dataframe['temperature_sink'].values.tolist()  # External temperature of condenser

# Calculate temperature difference between condenser and evaporator
temp_diff = [(t_m - t_l) for (t_m, t_l) in zip(list_temp_medium, list_temp_low)]
temp_diff_dataframe = pd.DataFrame(temp_diff, data_reduct['date_time'], columns=['temp_diff'])

#Concatenate final data and save
COP_data=pd.concat([dataframe, COP, temp_diff_dataframe], axis=1)
COP_data.to_csv(os.path.join(os.path.dirname(__file__), 'data/results/2021-05-06_TH_1270.csv'))
