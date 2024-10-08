import math
from haversine import inverse_haversine, Direction

def get_final_cords(lat_i, lon_i, vel_x, vel_y, ):
    h= 20

    g =10

    lat_i = 28.465
    lon_i = 77.22
    initial_pos = (lat_i, lon_i)


    vel_x = 5 
    vel_y = 5

    t = math.sqrt((2*h)/g)
    print("time of flight= ", t)

    x_r = vel_x*t
    y_r = vel_y*t
    print("x and y ranges of the projectile.. ",x_r, y_r)

    net_distance = math.sqrt((x_r*x_r)+(y_r*y_r))
    print("total distance travelled = ",net_distance)

    rad = math.atan(vel_y/vel_x)
    print('radians of travel direction', rad)

    (finalLat, finalLon) = inverse_haversine(initial_pos, net_distance, rad)

    final_pos = (finalLat, finalLon)

    print("final lat and lon", final_pos)
    return final_pos

final_pos = get_final_cords(28.465, 77.22, 5, 5)

print(final_pos)
