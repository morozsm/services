Some auxilary web services.

Runs in docker on localhost.

Exposes on port 8888:

/ip - returns client IP
/memcached - returns True or False if memcached reacheable on port 11211 on client's IP
Accepts GET arguments:
/memcached?host=some_ip&port=someport - Allows to define custom IP or port to check.
Defaults to port 11211 on client's IP

