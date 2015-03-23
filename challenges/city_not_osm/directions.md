# Adding bike lanes in the city's database but not in OSM

OSM currently has some major gaps in coverage in comparison with the city data.
As a result, this challenge is mostly adding new data. Exciting!


## Are you modifying or adding a new bike lane?

For each task in this challenge there are three potential situations:

 1. **The bike lane is already well-mapped in OSM**. You look at the line of the
    city's bike lane and there is already a bike lane in OSM that matches pretty
    well.
    
    You're done here. Either the data was already in OSM or someone beat you to
    the task.
 2. **The bike lane is already in OSM, but it doesn't line up very well** with 
    the city's data. Look around in a 50-foot radius of the bike lane you're 
    supposed to draw, do you see a bike lane in OSM that follows the same 
    street? Judging from the aerial imagery, is the OSM bike lane in the wrong 
    place?
    
    If so, nudge the bike lane into the proper location using the aerial imagery
    and the city's data.
 3. **The bike lane doesn't exist in OSM at all**. In step 2 you checked around
    the city bike lane and didn't find anything.
    
    When this happens, draw a line that follows the portion of the bike lane
    that is being shown to you. Use the tagging guide below to help decide how 
    to tag your line.


## Tagging guide

We recommend reading the OSM Wiki page on
[bicycles](http://wiki.openstreetmap.org/wiki/Bicycle), which contains a
detailed list of potential bike lane scenarios and how you should tag them. But
here are some general guidelines:

 * Only use [highway=cycleway](http://wiki.openstreetmap.org/wiki/Tag:highway%3Dcycleway)
    if the bike lane is not on a road.
 * Watch out for roads that have
   [cycleway=lane](http://wiki.openstreetmap.org/wiki/Bicycle#Cycle_lanes_in_oneway_motor_car_roads)
   tagged on them. It's easy to think you need to add a new bike lane when it
   is already incorporated into a road.
 * Even when a bike lane is separated from a road, if it runs along the road it
   is preferred that you use
   [segregated=yes](http://wiki.openstreetmap.org/wiki/Bicycle#Miscellaneous)
   (examples S3 and S4).
