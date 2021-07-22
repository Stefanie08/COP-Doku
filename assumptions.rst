Scope Definition
=================
The spatial scope of the calculation is Germany and its sixteen federal states.
COP calculation for Air-source heat pump (ASHP) and
Ground-source heat pump (GSHP) as both of them are mostly represented in Germany [1]_.


Temperature of the heat source
##############################
As a simplifying assumption the source temperature for the GSHP
is measured from depths of approximately 15 meters throughout
the year [2]_.

The temperature source for the GSHP is set to **10°C**.

In case of the  (ASHP), the ambient temperature
represents the source temperature for the calculation of the COP.
The temperature time series used for the ASHP is retrieved from the
`Deutscher Wetterdienst (DWD) <https://www.dwd.de/DE/leistungen/cdc/cdc_ueberblick-klimadaten.html?nn=16102&lsbId=344084>`_.
The DWD provides various types of time series with
over 400 operating weather stations.

Among the weather stations, those were selected that are located
the closest to the geographic center of each respective state.
The weather stations are calculated with the :py:func:`~.see_CH` functionality.

.. csv-table::
   :header: "Federal State", "Abbreviation","Weather Station id"
   :widths: 15, 10, 15

   "Baden-Württenmberg", "BW", "2074"
   "Bayern", "BY", "2691"
   "Berlin", "BE", "399"
   "Brandenburg", "BB", "5825"
   "Bremen", "HB", "691"
   "Hamburg", "HH", "6254"
   "Hessen", "HE", "7410"
   "Mecklenburg-Vorpommern", "MV", "5009"
   "Niedersachsen", "NI", "3612"
   "Nordrhein-Westfalen", "NW", "13696"
   "Rheinland-Pfalz", "RP", "5871"
   "Saarland", "SL", "5029"
   "Sachsen", "SN", "6314"
   "Sachsen-Anhalt", "ST", "3126"
   "Schleswig-Holstein", "SH", "6105"
   "Thüringen", "TH", "1270"


Temperature of the heat sink
#############################

The sink temperature used for the COP calculation of each federal state combines
hot water, floor heating, and radiator heating.

A field measurement study conducted by the Fraunhofer-Institute ISE monitored
the efficiency of different heat pump models.

The monitoring for the heat sink temperature of thirty one ASHP
resulted in an average value of 46.9 °C for domestic hot water heating.
Furthermore, an average of 32.7°C was measured for sink temperatures in heating circuits [3]_.
Another simplification is to apply these two measured temperature levels to the
three areas of heating and form the mean value equals to 37.43°C. To avoid large COP values,
the temperature sink is set to 46.9°C when outdoor temperatures are high in summer.

.. csv-table::
   :header: "Heat Pump Type", "Temperature of heat sink"," "
   :widths: 15, 10, 15

   "Air-source", "37.43°C", "Combines hot water, floor heating, and radiator heating."
   "Air-source", "46.9°C", "Sink temperature for hot water heating."
   "Ground-source", "37.43°C", "Combines hot water, floor heating, and radiator heating."


Quality Grade
##############
The COP of a real heat pump is calculated with the Carnot efficiency :math:`COP_\mathrm{Carnot}`
and the quality grade :math:`{\eta}`.
The quality grades used in this calculation are based on the nominal temperatures
and nominal conditions of different manufacturers' heat pump models.
Afterwards the mean value was calculated. Specifications to the heat pump models can be found
in the pvcompare documentation in section `heat_pumps_and_chillers.csv <https://pvcompare.readthedocs.io/en/latest/parameters.html#heat-pumps-and-chillers-csv>`_.
Therefore, the quality grades are:

.. csv-table::
   :header: "Heat Pump Type", "Quality Grade"
   :widths: 10, 10

    "Air-source", "0.4030"
    "Ground-source", "0.53"



Temperature Lift
#################


[4]_


.. [1] TODO: Quelle für die ASHP un GSHP
.. [2] H. Brandl: "Energy foundations and other thermo-active ground structures". Journal, 2006, p. 90, https://www.icevirtuallibrary.com/doi/pdf/10.1680/geot.2006.56.2.81
.. [3] D. Günther et al.: "„WP Monitor“ Feldmessung von Wärmepumpenanlagen". Report, 2014, p. 56, https://wp-monitoring.ise.fraunhofer.de/wp-monitor-plus/download/endbericht_wp_monitor_klein.pdf
.. [4] L. Gasser et al.: "High efficiency heat pumps for low temperature lift applications". Report, 2017, p. 2, http://hpc2017.org/wp-content/uploads/2017/05/O.1.4.5-High-efficiency-heat-pumps-for-low-temperature-lift-applications.pdf