## Setting Service Access Type
### Public Network Access

- A Layer-4 load balancer (LB) (1 CNY/day) that supports public network is created automatically.
- You can access the service via public network using LB VIP and access port. Meanwhile, the CVM port opens automatically.

### Private Network Access

- A Layer-4 LB that supports private network is created automatically.
- You can access the service via private network using LB VIP and access port. Meanwhile, the CVM port opens automatically.

### Access Within a Cluster

- This service access type only supports service access within a cluster.
- You can access the service within a cluster using service name or service IP +access port.

The above three types can also be configured with Layer-7 LB (HTTP/HTTPS) to forward to the service. For more information, please see [How to Use Layer-7 LB for Container Services](https://www.qcloud.com/document/product/457/8841?!preview=true&lang=zh).


