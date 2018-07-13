Currently, the major version of Tencent Cloud master-slave Redis is 2.8.23. Version 3.2.6 will be available soon.

The features of various versions of Redis are listed below.
## 3.2.X
- Support for data partition
- Support for geo-spatial index and GEO command
- Optimized memory to store the same data with less space
- Optimized BITFIELD command
	

## 2.8.X
- Support for command with a data type of sorted set 
- Improved elasticity and fault tolerance of read-only copies.
- Support for partial re-synchronization.
- User-defined minimum number of read-only copies with persistent availability.
- Full support for pub/sub, which can notify the client about the events occurring on the server.
- Automatic detection of failure of master node and failover to a salve node.

## 2.6.X
- Support for lua script.
- Removal of the limit on the client
- Improved aof performance
- Filtering of "key" within milliseconds
- Support for the new commands "dump" and "restore" (serialization and deserialization).
- Optimized performance of big data storage


