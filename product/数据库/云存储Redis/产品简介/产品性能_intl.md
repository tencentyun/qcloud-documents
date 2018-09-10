

### Performance References
The performance values may vary with commands and their execution time in the production environment. The tested values in this document are obtained based on specific parameters and for reference only. To get the actual performance values, perform a test on a real-life service.

 - Single-node performance
  
| CRS Instance Specification | Number of Connections | Max QPS |
|:---------:|:---------:|:--------:|
| Redis 2.8 Master/Slave 8 GB | 9000 | 85,000 |
| Redis 4.0 8GB | 10000 | 100,000 |
| CKV Master/Slave 8 GB |  9000    | 120,000 |

 
 - Performance of the Cluster version
 
   Redis Cluster performance = Redis Master/Slave performance * number of nodes
 
    CKV Cluster performance = CKV Master/Slave performance * number of nodes


### Test Method

 - Testing environment
 
| Number of CVMs in the pressure test client | CVM cores | CVM MEM | Region | CRS instance size |
|:---------:|:---------:|:---------:|:---------:|:---------:|
| 3 | 2 cores |8G | Guangzhou Zone 2 | Open source Stand-alone 8G | 
| 3 | 2 cores |8G | Guangzhou Zone 2 | Open source Master/Slave 8G | 
| 3 | 2 cores |8G | Guangzhou Zone 2 | CKV Master/Slave 8G |


 - Test parameters
 ```
redis-benchmark -h 10.66.187.x -p 6379 -a crs-1znib6aw:chen2016 -t set -c 3500 -d 128 -n 25000000 -r 5000000
redis-benchmark -h 10.66.187.x -p 6379 -a crs-1z5536aw:chen2016 -t set -c 3500 -d 128 -n 25000000 -r 5000000
redis-benchmark -h 10.66.187.x -p 6379 -a crs-090rjlih:1234567 -t set -c 3500 -d 128 -n 25000000 -r 5000000
```
 - QPS calculation
Calculate the sum of the QPS tested by 3 pressure test clients (redis-benchmark).



