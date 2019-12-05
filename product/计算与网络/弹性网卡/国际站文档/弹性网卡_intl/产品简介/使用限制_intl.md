The maximum number of ENIs that can be bound to a CVM and that of private IPs that can be bound to each ENI vary greatly with CPU and memory configurations. The limits are shown in the following table. For more information, please see [Use Limits on Other VPC Products](https://cloud.tencent.com/doc/product/215/537).

| CVM Configuration           | Max. Number of ENIs | Max. Number of IPs Bound to Each ENI |
| --------------------------- | :------------------ | :----------------------------------- |
| CPU: 1-core   Memory: 1 GB  | 2                   | 2                                    |
| CPU: 1-core   Memory: >1 GB | 2                   | 6                                    |
| CPU: 2-core                 | 2                   | 10                                   |
| CPU: 4-core   Memory: < 16G | 4                   | 10                                   |
| CPU: 4-core  Memory: >16 GB | 4                   | 20                                   |
| CPU: 8-12 core              | 6                   | 20                                   |
| CPU: >12-core               | 8                   | 30                                   |