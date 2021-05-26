What you can find here and general information
==============================================

Going through this documentation you will be able to generate a COP time series with individual
input ambient temperatures as well as individual temperature sinks.

For open_MODEX a COP time series was generated for each federal state in Germany using the
:py:func:`~.calc_cops` functionality from `oemof.thermal <https://oemof-thermal.readthedocs.io/en/latest/>`_
for compression heat pumps.

The :py:func:`~.calc_cops` functionality is a simple calculation for compression heat pumps and chillers
based on temperatures for energy system optimizations with oemof.solph.

To determine the COP of a real machine a scale-down factor (the quality grade \eta)
is applied on the Carnot efficiency:


.. math:: COP = \eta \cdot COP_\mathrm{Carnot}
   :label: COP_calc


with


.. math:: 0 \leq \eta \leq 1


Further information regarding the COP calculation see
`Compression heat pump and chiller <https://oemof-thermal.readthedocs.io/en/latest/compression_heat_pumps_and_chillers.html>`_.