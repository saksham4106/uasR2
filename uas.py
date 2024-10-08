import math
import haversine 

f1 = open("file1.txt", "r")
f2 = open("file2.txt", "r")

d1 = f1.read().split(" ")
d2 = f2.read().split(" ")
# lat1 = 28.644800
# lon1 = 77.216721

# lat2 = 28.645000
# lon2 = 77.217000

# vx = 5
# vy = 5

lat1 = int(d1[0])
lon1 = int(d1[1])

lat2 = int(d2[0])
lon2 = int(d2[1])

vx = int(d1[2])
vy = int(d1[3])



m = 1.5   # mass
h = 20
Cd = 0.47   # coefficient of drag
g = 9.8 # gravity at surface of earth
p = 1.2   # viscosity of air
area = 1   # assuming area to be 1 for now 
k = Cd * 0.5 * p * area   # F = -kv^2 wala k
permissibleLimit = 10    # range 


def haversine(lat1, lon1, lat2, lon2):

    lat1_rad, lon1_rad, lat2_rad, lon2_rad = map(math.radians, [lat1, lon1, lat2, lon2])

    dlat = lat2_rad - lat1_rad
    dlon = lon2_rad - lon1_rad

    a = math.sin(dlat / 2)**2 + math.cos(lat1_rad) * math.cos(lat2_rad) * math.sin(dlon / 2)**2
    c = 2 * math.atan2(math.sqrt(a), math.sqrt(1 - a))

    distance = 6371e3 * c
    return distance

def getTimeofFlight():
    global h 
    a = math.sqrt(g * m / k)

    dt = 0.0001
    v = 0
    t = 0
    c = 90

    while h > 0 :
        dv = a * ( (math.exp(c * t) - 1 ) / (math.exp(c*t) + 1) )  * dt 
        v += dv 

        h -= v * dt 
        t += dt
        
    return t 

def getChangeInX(tim, vi):
    delx = m/k * math.log(k * vi * tim / m + 1)
    return delx

def checkifPayloadAllowed(lat1, lon1):
    global vx, vy
    t = getTimeofFlight()
    dx = getChangeInX(t, vx)    # change in x in total time of flight
    dy = getChangeInX(t, vy)   # change in y in total time of flight

    new_latitude  = lat1  + (dy / 6371e3) * (180 / math.pi)
    new_longitude = lon1 + (dx / 6371e3) * (180 / math.pi) / math.cos(lat1 * math.pi/180) # lon changes with change in lat

    d = haversine(new_latitude, new_longitude, lat2, lon2)

    if d > permissibleLimit:
        return False 
    else:
        return True





lat = lat1
lon = lon1
initial_dist = haversine(lat1, lon1, lat2, lon2)

while True:
    
    del_lat = vy / 111320
    del_lon = vx/(111320 * math.cos(math.radians(lat)))
    lat += del_lat
    lon += del_lon

    if checkifPayloadAllowed(lat, lon):
        print("Payload successfully landed at " , lat, lon)
        break 
    
    current = haversine(lat, lon, lat2, lon2)
    print(current)
    if(current > initial_dist):
        print("Payload can't  reach")
        break 






