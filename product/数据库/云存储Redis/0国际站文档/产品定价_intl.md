## Postpaid
 Redis supports tiered prices in postpaid mode. The longer the usage duration, the lower the cost. Tier 3 price in postpaid mode is basically the same as the price in prepaid mode. Depending on the usage duration, the prices in postpaid mode are divided into three tiers:<br>
 - Tier 1 (0 to 4 days): price per hour = monthly price`/30/24*2`.<br>
 - Tier 2 (4 to 15 days): price per hour = monthly price`/30/24*1.5`.<br>
 - Tier 3 (more than 15 days): price per hour = monthly price`/30/24`.<br>
 - Formula: Tier 1 price = 2 * Tier 3 price, Tier 2 price = 1.5 * Tier 1 price.
 <br>
 **Note:** For instances with expanded or reduced capacity, as well as isolated instances, the price is recalculated starting from Tier 1.

 ### In GB/Hour by region (Tier 3)
 | Configuration | USD/GB/Hour | USD/GB/Month | Region |
 |:--:|:--:|:--:|:--:|
 | 1 GB MEM |0.034704|24.98688| Beijing, Shanghai, Guangzhou, Chengdu, Chongqing |
 | 1 GB MEM |0.029196|21.02112| Virginia in US East, Silicon Valley in US West |
 | 1 GB MEM |0.036108|25.99776| Hong Kong, Singapore |
 | 1 GB MEM |0.045792|32.97024| Mumbai |
 | 1 GB MEM |0.037512|27.00864| Seoul |
 | 1 GB MEM |0.041688|30.01536| Frankfurt |
 | 1 GB MEM |0.024984|17.98848| Moscow |
 | 1 GB MEM |0.045792|32.97024| Bangkok |
 | 1 GB MEM |0.026388|18.99936| Tokyo |
 | 1 GB MEM |0.050004|36.00288| North America |

 ### Detailed specifications

 ##### Redis Community engine
 | Specification (G) | Max Connections | Max Throughput (MB/s) |
 | ---------- | ---------- | ------------------- | 
 | 0.25       | 10000       | 10                  |
 | 1          | 10000       | 16                  | 
 | 2          | 10000       | 24                  | 
 | 4          | 10000       | 24                  | 
 | 8          | 10000       | 24                  | 
 | 12         | 10000       | 32                  |
 | 16         | 10000       | 32                  | 
 | 20         | 10000       | 48                  | 
 | 24         | 10000       | 48                  | 
 | 32         | 10000       | 48                  | 
 | 40         | 10000       | 64                  | 
 | 48         | 10000       | 64                  | 
 | 60         | 10000       | 64                  | 

 ##### Redis-CKV engine (Master/Slave)
 | Specification (G) | Max Connections | Max Throughput (MB/s) |
 | ---------- | ---------- | ------------------- |
 | 4          | 12000       | 24                  | 
 | 8          | 12000       | 24                  |
 | 16         | 12000       | 32                  | 
 | 24         | 12000       | 32                  | 
 | 32         | 12000       | 32                  | 
 | 48         | 20000      | 64                  | 
 | 64         | 20000      | 64                  | 
 | 80         | 20000      | 64                  | 
 | 96         | 20000      | 64                  | 
 | 128        | 20000      | 128                 | 
 | 160        | 20000      | 128                 | 
 | 192        | 20000      | 128                 | 
 | 256        | 20000      | 256                 | 
 | 320        | 20000      | 256                 | 
 | 384        | 20000      | 256                 | 




