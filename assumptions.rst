Scope Definition
=================

* Spatial Scope is Germany and its sixteen federal states
* COP calculation for Air-source heat pump (ASHP) and
Ground-source heat pump (GSHP) as both of them are mostly represented in Germany [1]_.


Temperature of the heat source
##############################

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

   "Brandenburg", "BB", "1234"
   "Berlin", "BE", "1234"

As a simplifying assumption the source temperature for the GSHP is
at constant 10°C of the ground temperature from depths of approximately
15 meters throughout the year [2]_.


Temperature of the heat sink
#############################

The sink temperature used for the COP calculation of each federal state combines
hot water, floor heating, and radiator heating.

Field measurements of thirty one ASHP resulted in an average value of 46.9 °C
for domestic hot water heating. Furthermore, an average of 32.7°C was measured
for sink temperatures in heating circuits [3]_. Another simplification is to apply
these two measured temperature levels to the three areas of heating and form
the mean value. To avoid large COP values, the temperature sink is set to 46.9°C
when outdoor temperatures are high in summer.

Quality Grade
##############

Quality Grade: section heat_pumps_and_chillers:

`heat_pumps_and_chillers.csv <https://pvcompare.readthedocs.io/en/latest/parameters.html#heat-pumps-and-chillers-csv>`_.





.. [1] TODO: Quelle für die ASHP un GSHP
.. [2] H. Brandl: "Energy foundations and other thermo-active ground structures". Journal, 2006, p. 90, https://www.icevirtuallibrary.com/doi/pdf/10.1680/geot.2006.56.2.81
.. [3] D. Günther et al.: "„WP Monitor“ Feldmessung von Wärmepumpenanlagen". Report, 2014, p. 56, https://wp-monitoring.ise.fraunhofer.de/wp-monitor-plus/download/endbericht_wp_monitor_klein.pdf
.. [4] L. Gasser et al.: "High efficiency heat pumps for low temperature lift applications". Report, 2017, p. 2, http://hpc2017.org/wp-content/uploads/2017/05/O.1.4.5-High-efficiency-heat-pumps-for-low-temperature-lift-applications.pdf