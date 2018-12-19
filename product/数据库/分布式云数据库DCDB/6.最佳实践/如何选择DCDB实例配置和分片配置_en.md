## Overview of DCDB selection

DCDB is made up of shards. The specification and number of shards determine the processing abilities of DCDB instances. Theoretically,

- DCDB instance read and write concurrency performance = ∑ (performance of a shard with certain specification * number of the shards)
- DCDB instance transaction performance = ∑ (transaction performance of a shard with certain specification * 70% * number of the shards)

Therefore, high specification and large quantity of shards means strong processing ability to the instance. The sharding performance of a DCBD instance is mainly related to CPU/memory and measured by QPS. Specific performance indicators can be found in the sharding performance part.


## How to decide on DCDB shard specification

Specification of DCDB shard is determined by three factors: performance, capacity and other requirements.

**Performance**: By predicting the performance capacity and possible increments for at least six months, you can define the total CPU/memory size required for your distributed instance.
**Capacity**: By predicting the disk capacity and possible increments for at least one year, you can define the total disk size required for your distributed instance.
**Other requirements**: That one shard stores at least **50 million lines of data** is recommended. [broadcast table and single table](https://cloud.tencent.com/document/product/557/8764), join and other businesses within the node shall also be considered.

> Note: It is recommended to ensure high specification for single shard with relatively small quantity of shards.

Judging from the above, we recommend to you the following policies based on the predicted business models:

- For functional testing and no special performance requirements: 2 shards, and the specification for each one: **memory: 2 GB, disk: 25 GB**.
- In initial stage of business, total size of data is small but grows fast: 2 shards, and the specification for each one: **memory: 16 GB, disk: 200 GB**.
- In stable development stage, sharding is based on actual business conditions: 4 shards, and the specification for each one: **current business peak * growth rate / 4**.


## Test of DCDB Sharding Performance

Database benchmark performance test is for modifying descriptions of sysbench 0.5: otlp script in sysbench is modified; read/write ratio is set to 1:1 and controlled by executing test command parameters "oltp_point_selects" and "oltp_index_updates". All test cases in this document do 4 Select operations and 1 Update operation, and keep read/write ratio to 4:1.

|vCPU (Core)|Memory (GB)|Storage Space (GB)|Data set (GB)|Number of clients|Number of concurrence in single client|QPS|TPS|
|:--:|:--:|:--:|:--:|:--:|:--:|:--:|:--:|
|1|2 GB|100 GB|46 GB|1|128|1880|351|
|2|4 GB|200 GB|76 GB|1|128|3983|797|
|2|8 GB|200 GB|142 GB|1|128|6151|1210|
|4|16 GB|400 GB|238 GB|1|128|10098|2119|
|4|32 GB|700 GB|238 GB|2|128|20125|3549|
|8|64 GB|1 T|378 GB|2|128|37956|7002|
|12|96 GB|1.5 T|378 GB|3|128|51026|10591|
|16|120 GB|2 T|378 GB|3|128|81050|15013|
|24|240 GB|3 T|567 GB|4|128|96891|17698|
|48|480 GB|6 T|567 GB|6|128|140256|26599|


> TPS is a single TPS, but not a distributed transaction TPS.
> 
> According to the requirements on operation policies, current DCDB instances (or part of them) adopt the policy of excess usage of idle resources, so CPU utilization may exceed 100% on your monitoring screen.

