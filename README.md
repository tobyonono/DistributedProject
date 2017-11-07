# DistributedProject
Project for Distro


Implemented Caching + Directory Services

Cache has a maximum size and when a file is read/written the cache is checked to make sure it isn't full before it adds to it. If it is full the oldest entry in the cache is deleted to make room for the newer entry.
