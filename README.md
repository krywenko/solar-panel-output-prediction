# solar-panel-output-prediction

a small script for predicting solar output based on  predicted clouds cover/ air visablity from various  weather API's  

OpenWeather,Climacel,Weather-API, Weatherbit, VisualCrossing, and Aeris.  it fairly accurate depending on the accuracy of the weather API


you will need to install pysolar , lynx and bc

pysolar  can be install vis pip install pysolar
and lynx and bc  through your basic apt install method.

it configured to work with collectd-mqtt that sends it to influxdb to generate graphs or graphs viable in collectd interface . it also generates a CSV  so you can import it in other databases 

you need to configure  which ever API with your local corordinates  and your weather API key/s .  the lat/lon  has two functions it configures pysolar with your local postion to calculate probable clear sky solar radation.  and  get the weather api  cloud cover estimate to generate a probable masking effects..

the second file, to configure, is the panelconf.  this helps calculates the power production. it supports  up to 3 orientations and predicts solar panel potential production  depending on the sun's position in relations to the panel groupings.. in there you enter your panel orientation , panel grouping  wattage size, inverter effieciency  and albedo effect ( ie: reflected light that still generates power output - to calculater your general albedo  at midday  measure you maxmium out put for a panel   then point the panel away from the sun and see  what your power output is. then divide the  maxmium  from the  reflective to get a percentage  ( whole number  ie 0.05 =  5%) 

it also has a simple tool called graph  using gnuplot  to generate a simple graph   usage is : graph W_API.csv to see predicted power production from the weather api csv

 example below
![graph csv](https://github.com/krywenko/solar-panel-output-prediction/blob/main/predictive2.png)

Graphing in Chronograf - you notice that different  apis gave different  cloudcover prediction as with air visablity hence  why the graph is slightly different than the actual  predicted cloud cover 
![ChronoGraf](https://github.com/krywenko/solar-panel-output-prediction/blob/main/predictive3.png)

for me  weather API   and weatherbit are the  most consistanly accurate. but I live in a fairly remote regions that are not generally covered that well by most weather API services .  you can generate  higher accuracy by combining  several  api out puts into one  or  taking  sample from several different  gps  location close to you IE 50km  away from you  and combining into one graph out put 

the CSV  are sent to /dev/shm to save on writing to and SD card since many will likely use in pin pi devices
it also creates  a 24 hr period  the  Maxmium Clear sky output, the estimated solar production and  measured solar  production  this can vary by 0-5 % also the percentage of normal  clear sky production and  number of hrs ofpower production ( rounded to 1/2 hr
