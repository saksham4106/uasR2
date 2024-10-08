# How it works
A loop is iterated in which the location of the UAV is constantly updated according to it's given velocities 
In each iteration, the payload is simulated to be dropped and is checked if it will make it to the destination 

## How is it simulated? 
1. using another loop, the time of flight of the uav is calculated using the function getTimeOfFlight()
2. using the total time, the change in x and y for the complete journey is evaluated, and the distance travelled is used to generate
a new set of latitude and longitude coordinates.
3.  Then using the haversine algorithm, we compute the distance between the new set and the destination coordinates. if the distance is under the range of permissible value, we drop the payload, otherwise it isn't dropped and the uav continues on its path.
4. If the distance measured is greater than the initial distance itself, it means the UAS is going in further direction than the destination and the payload isn't dropped. 
