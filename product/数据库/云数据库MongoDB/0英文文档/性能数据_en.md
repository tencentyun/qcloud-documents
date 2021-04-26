## Performance Test Instructions

### Tool
[Yahoo! Cloud Serving Benchmark](https://github.com/brianfrankcooper/YCSB)

### Test Method
1. A single data entry is 1 KB
2. Occupy 80% of the instance capacity. For example: if the instance capacity is 100 GB, put 80 GB of data in it
3. Perform 50% read and 50% update operations to get QPS (Queries Per Second) data
4. Since there can be difference between the performances under different scenarios, please select instances with the appropriate specifications according to your business demand and test data

## Performance Data of High IO Instances
| CPU | memory | QPS |
|:--:|:--:|
| 1 core | 2 GB | 3000 |
| 2 cores | 4 GB | 5000 |
| 2 cores | 6 GB | 6000 |
| 4 cores | 8 GB | 9000 |
| 4 cores | 12 GB | 14000 |
| 6 cores | 16 GB | 20000 |
| 10 cores | 24 GB | 25000 |
| 12 cores | 32 GB | 27000 |
| 18 cores | 48 GB | 30000 |
| 24 cores | 64 GB | 33000 |

## Performance Data of High IO Instance (10 Gigabyte)
| CPU | Memory | Number of sets| Number of documents in a single set| Test data set (GB) | Runtime (S) | Data sampling interval (S) | Average QPS (rounded) |
|:--:|:--:|:--:|:--:|:--:|:--:|:--:|:--:|
| 2 cores | 4 GB | 2 | 100 million | 79 | 1800 | 10 | 5000 |
| 4 cores | 8 GB | 3 | 100 million | 118 | 1800 | 10 | 9000 |
| 6 cores | 16 GB | 6 | 100 million | 237 | 1800 | 10 | 20000 |
| 12 cores | 32 GB | 6 | 200 million | 426 | 1800 | 10 | 27000 |
| 24 cores | 64 GB | 15 | 200 million | 1161 | 1800 | 10 | 33000 |
| 24 cores | 128 GB | 30 | 200 million | 2317 | 1800 | 10 | 36000 |
| 32 cores | 240 GB | 40 | 200 million | 3031 | 1800 | 10 | 39000 |
