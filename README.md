# solar-panel-output-prediction

a small script for predicting solar output based on  predicted clouds cover from various  weather API's  

OpenWeather,Climacel,Weather-API, Weatherbit, VisualCrossing, and Aeris.  it fairly accurate depending on the accuracy of the weather API


you will need to install pysolar , lynx and bc

pysolar  canc be isnstall vis pip install pysolar
and lynx and bc  through your basic apt install method.

it configured to work with collectd-mqtt that sends it to influxdb to generate graphs or graphs viable in collectd interface . it also generales a CSV  so you can import it in other databases 

you need to configure  which ever API with your local corordinates  and your weather API key/s .  the lat/lon  has two functions it configures pysolar with your local postion to calculate probable clear sky solar radation.  and  get the weather api  cloud cover estimate to genatate a probably masking effects..

the second file to configure is the panelconf  this helps calculates the power production it supports  up to 3 orientations. in there you enter your panel orientation , panel grouping  wattage size, inverter effieciency  and albedo effect ( ie: reflected light that still generates power output - to calculater your general albedo  at midday  measure you maxium out put for a panel . then point the panel away from the sun and see  what your power output is. then divide the  maxium  from the  reflective to get a percentage  ( whole number  ie 0.05 =  5%) 

it also has a simple tool called graph  using gnuplot  to generate a simple graph   usage is : graph W_API.csv to see predicted power production from the weather api csv

