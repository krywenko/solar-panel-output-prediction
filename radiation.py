 
from pysolar.solar import *
import datetime
from datetime import  timezone
import argparse
parser = argparse.ArgumentParser()
parser.add_argument('--foo', help='foo help')


parser.add_argument("-lon", "--longitude",
                        type=float,
                        #action="append",
                        default=[],
                        help="Longitude imput %(prog)s")
parser.add_argument("-lat", "--latitude",
                        type=float,
                        #action="append",
                        default=[],
                        help="Llatitude imput %(prog)s")
parser.add_argument("-t", "--time",
                        type=int,
                        #action="append",
                        default=[],
                        help="LUTC epoc time imput %(prog)s")

args = parser.parse_args()
#print(args)


ts = datetime.datetime.fromtimestamp(args.time,timezone.utc)
#print(ts)
#print(ts.strftime('%Y,%m,%d,%H,%M,%S'))

Y=int(ts.strftime('%Y'))
M=int(ts.strftime('%m'))
D=int(ts.strftime('%d'))
H=int(ts.strftime('%H'))
m=int(ts.strftime('%M'))
s=int(ts.strftime('%S'))


latitude_deg = (args.latitude) # positive in the northern hemisphere
longitude_deg = (args.longitude) # negative reckoning west from prime meridian in Greenwich, England
date = datetime.datetime(Y,M,D,H,m,s, tzinfo=datetime.timezone.utc)
#print(date)

#print(get_azimuth(latitude_deg, longitude_deg, date))
altitude_deg = get_altitude(latitude_deg, longitude_deg, date)
#print(altitude_deg)
#print(args.time)
print(radiation.get_radiation_direct(date, altitude_deg))
