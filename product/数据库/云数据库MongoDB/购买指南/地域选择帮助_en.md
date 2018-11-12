#### Tips for Region Selection

Currently, Tencent Cloud Database MongoDB only provides two available regions: **East China (Shanghai) and South China (Guangzhou)**;
**Note:**
1. Cloud products in the same region can communicate with each other through private network
2. Cloud products in different regions cannot communicate with each other through private network
   1) CVMs in different regions cannot access each other through private network, also, they cannot access cloud databases and cloud caches in different regions
   2) You can only select CVMs in the current region when binding Cloud Load Balancer to CVMs.
   3) CVMs can only access other CVMs, Cloud Object Storage and elastic web engine in other regions through public network 
3. When purchasing cloud services, it is recommended to choose the region closest to your customer to minimize access latency and improve download speed;
