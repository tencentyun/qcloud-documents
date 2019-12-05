#### Testing Environment

| CVMs Under Stress Test | CVM Cores | CVM Memory | Zone | CRS Instance Size |
|:---------:|:---------:|:---------:|:---------:|:---------:|
| 3 | 2 | 8 GB | Guangzhou Zone 2 | 8 GB Master/Slave instance | 


#### Testing Command
```
redis-benchmark -h 10.66.187.77 -p 6379 -a crs-1znib6aw:chen2016 -t set -c 3500 -d 128 -n 25000000 -r 5000000
```


#### Statistical Method
QPS is calculated as the sum of QPSs of 3 CVMs under stress test

#### Performance Data
QPS is calculated as the sum of QPSs of 3 CVMs under stress test

| CRS Instance Specification | Connections | QPS |
|:---------:|:---------:|:--------:|
| 8 GB | 9000 | 85000 |
