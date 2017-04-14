## Instance Price
Tencent Cloud CDB for MySQL currently supports two payment modes for instances: annual or monthly plan and pay by usage mode.

## Tiered Prices for Pay by Usage Mode
Starting from July 15, 2016, CDB for MySQL supports tiered prices for CDB for MySQL with a "pay by usage" billing model. A longer usage means a lower cost.
Depending on the usage duration, there are three tires for pay by usage mode:
0-4 days (within 4*24h): The tier 1 price shall apply
4-15 days (from 4*24h to 15*24h): The tier 2 price shall apply
Over 15 days (from 15*24h): The tier 3 price shall apply

## Prices for Different Regions

### North China (Beijing), South China (Guangzhou), and East China (Shanghai)
Since July 11, 2016, for regions like North China (Beijing), South China (Guangzhou), and East China (Shanghai), Cloud Database MySQL has supported only the separate billing mode for the purchase of memories and disks, providing users with flexible options.

**Instance price formula: Instance price = memory specification price + storage price. Renewal and upgrade of instances with original specifications shall be subject to the new price system.**

Additionally, our new tired price system for pay by usage mode is even preferential for longer users. For details, please refer to the following price lists:

### Memory Specification Price for North China (Beijing), South China (Guangzhou) - Guangzhou Zone 3, and East China (Shanghai)

| Configuration Type | Database Type | Instance Specification | QPS in Counts/Second | Monthly Discount Price (in CNY/Month) | Tier 1 price for pay by usage mode (0-4 days) (in CNY/Hour) | Tier 2 price for pay by usage mode (4-15 days) (in CNY/Hour) | Tier 3 price for pay by usage mode (above 15 days) (in CNY/Hour) |
|:--:|:--:|:--:|:--:|:--:|:--:|:--:|:--:|
| High IO | MySQL instance | 1,000 MB MEM | 1,000 | 107 | 0.3 | 0.23 | 0.15 |
| High IO | MySQL instance | 2,000 MB MEM | 2,400 | 214 | 0.6 | 0.45 | 0.30 |
| High IO | MySQL instance | 4,000 MB MEM | 4,400 | 427 | 1.19 | 0.89 | 0.60 |
| High IO | MySQL instance | 8,000 MB MEM | 7,200 | 854 | 2.38 | 1.78 | 1.19 |
| High IO | MySQL instance | 16,000 MB MEM | 18,000 | 1,708 | 4.75 | 3.56 | 2.38 |
| High IO | MySQL instance | 32,000 MB MEM | 25,000 | 3,416 | 9.49 | 7.12 | 4.75 |
| High IO | MySQL instance | 64,000 MB MEM | 37,689 | 6,832 | 18.98 | 14.24 | 9.49 |
| High IO | MySQL instance | 96,000 MB MEM | 40,919 | 9,110 | 25.31 | 18.98 | 12.66 |
| High IO | MySQL instance | 128,000 MB MEM | 61,378 | 13,664 | 37.96 | 28.47 | 18.98 |
| High IO | MySQL instance | 244,000 MB MEM | 122,755 | 27,238 | 75.92 | 56.94 | 37.46 |
| High IO | MySQL instance | 488,000 MB MEM | 245,509 | 54,656 | 151.83 | 113.87 | 75.92 |
| High IO | MySQL read-only instance | 1,000 MB MEM | 1,000 | -- | 0.15 | 0.12 | 0.08 |
| High IO | MySQL read-only instance | 2,000 MB MEM | 2,400 | -- | 0.30 | 0.23 | 0.15 |
| High IO | MySQL read-only instance | 4,000 MB MEM | 4,400 | -- | 0.60 | 0.45 | 0.30 |
| High IO | MySQL read-only instance | 8,000 MB MEM | 7,200 | -- | 1.19 | 0.89 | 0.60 |
| High IO | MySQL read-only instance | 16,000 MB MEM | 18,000 | -- | 2.38 | 1.78 | 1.19 |
| High IO | MySQL read-only instance | 32,000 MB MEM | 25,000 | -- | 4.75 | 3.56 | 2.38 |
| High IO | MySQL read-only instance | 64,000 MB MEM | 37,689 | -- | 9.49 | 7.12 | 4.75 |
| High IO | MySQL read-only instance | 96,000 MB MEM | 40,919 | -- | 12.66 | 9.49 | 6.33 |
| High IO | MySQL read-only instance | 128,000 MB MEM | 61,378 | -- | 18.98 | 14.24 | 9.49 |
| High IO | MySQL read-only instance | 244,000 MB MEM | 122,755 | -- | 37.96 | 28.47 | 18.98 |
| High IO | MySQL read-only instance | 488,000 MB MEM | 245,509 | -- | 75.92 | 56.94 | 37.96 |

### Memory Specification Price for South China (Guangzhou) - Guangzhou Zone 2

| Configuration Type | Database Type | Instance Specification | QPS in Counts/Second | Monthly Discount Price (in CNY/Month) | Tier 1 price for pay by usage mode (0-4 days) (in CNY/Hour) | Tier 2 price for pay by usage mode (4-15 days) (in CNY/Hour) | Tier 3 price for pay by usage mode (above 15 days) (in CNY/Hour) |
|:--:|:--:|:--:|:--:|:--:|:--:|:--:|:--:|
| High IO | MySQL instance | 360 MB MEM | 120 | 21 | 0.11 | 0.08 | 0.06 |
| High IO | MySQL instance | 1,000 MB MEM | 1,000 | 112 | 0.31 | 0.23 | 0.15 |
| High IO | MySQL instance | 2,000 MB MEM | 2,400 | 223 | 0.62 | 0.46 | 0.31 |
| High IO | MySQL instance | 4,000 MB MEM | 4,400 | 446 | 1.24 | 0.93 | 0.62 |
| High IO | MySQL instance | 8,000 MB MEM | 7,200 | 891 | 2.47 | 1.86 | 1.24 |
| High IO | MySQL instance | 12,000 MB MEM | 15,000 | 1,336 | 3.71 | 2.78 | 1.86 |
| High IO | MySQL instance | 16,000 MB MEM | 18,000 | 1,782 | 4.95 | 3.71 | 2.47 |
| High IO | MySQL instance | 24,000 MB MEM | 23,000 | 2,672 | 7.42 | 5.57 | 3.71 |
| High IO | MySQL instance | 48,000 MB MEM | 37,000 | 5,344 | 14.84 | 11.13 | 7.42 |
| High IO | MySQL read-only instance | 360 MB MEM | 120 | -- | 0.06 | 0.04 | 0.03 |
| High IO | MySQL read-only instance | 1,000 MB MEM | 1,000 | -- | 0.15 | 0.12 | 0.08 |
| High IO | MySQL read-only instance | 2,000 MB MEM | 2,400 | -- | 0.31 | 0.23 | 0.15 |
| High IO | MySQL read-only instance | 4,000 MB MEM | 4,400 | -- | 0.62 | 0.46 | 0.31 |
| High IO | MySQL read-only instance | 8,000 MB MEM | 7,200 | -- | 1.24 | 0.93 | 0.62 |
| High IO | MySQL read-only instance | 12,000 MB MEM | 15,000 | -- | 1.86 | 1.39 | 0.93 |
| High IO | MySQL read-only instance | 16,000 MB MEM | 18,000 | -- | 2.47 | 1.86 | 1.24 |
| High IO | MySQL read-only instance | 24,000 MB MEM | 23,000 | -- | 3.71 | 2.78 | 1.86 |
| High IO | MySQL read-only instance | 48,000 MB MEM | 37,000 | -- | 7.42 | 5.57 | 3.71 |


#### Storage Price

| Database Type | Monthly Discount Price (in CNY/GB/Month) | Pay by Usage Price (in CNY/GB/Hour) |
|:--:|:--:|:--:|
| MySQL instance | 0.8 | 0.0022 |
| MySQL read-only instance | 0.8 | 0.0022 |


### Southeast Asia (Hong Kong) 
**Instance price formula: Instance price = memory specification price + storage price. Renewal and upgrade of instances with original specifications shall be subject to the new price system.**

Additionally, our new tired price system for pay by usage mode is even preferential for longer users. For details, please refer to the following price lists:
#### Memory Specification Price

| Configuration Type | Database Type | Instance Specification | QPS in Counts/Second | Monthly Discount Price (in CNY/Month) | Tier 1 price for pay by usage mode (0-4 days) (in CNY/Hour) | Tier 2 price for pay by usage mode (4-15 days) (in CNY/Hour) | Tier 3 price for pay by usage mode (above 15 days) (in CNY/Hour) |
|:--:|:--:|:--:|:--:|:--:|:--:|:--:|:--:|
| High IO | MySQL instance |360 MB MEM|120|62|0.17|0.13 |0.09 |
| High IO | MySQL instance | 1,000 MB MEM | 1,000 | 171 | 0.47 | 0.36 | 0.24 |
| High IO | MySQL instance | 2,000 MB MEM | 2,400 | 342 | 0.95 | 0.71 | 0.47 |
| High IO | MySQL instance | 4,000 MB MEM | 4,400 | 684 | 1.90 | 1.42 | 0.95 |
| High IO | MySQL instance | 8,000 MB MEM | 7,200 | 1,367 | 3.80 | 2.85 | 1.90 |
| High IO | MySQL instance | 12,000 MB MEM | 15,000 | 2,050 | 5.69 | 4.27 | 2.85 |
| High IO | MySQL instance | 16,000 MB MEM | 18,000 | 2,734 | 7.59 | 5.69 | 3.80 |
| High IO | MySQL instance | 24,000 MB MEM | 23,000 | 4,100 | 11.39 | 8.54 | 5.69 |
| High IO | MySQL instance | 48,000 MB MEM | 37,000 | 8,200 | 22.78 | 17.08 | 11.39 |

#### Storage Price

| Database Type | Monthly Discount Price (in CNY/GB/Month) | Pay by Usage Price (in CNY/GB/Hour) |
|:--:|:--:|:--:|
| MySQL instance | 1.2 | 0.0033 |

### Southeast Asia (Singapore) 
**Instance price formula: Instance price = memory specification price + storage price. Renewal and upgrade of instances with original specifications shall be subject to the new price system.**

Additionally, our new tired price system for pay by usage mode is even preferential for longer users. For details, please refer to the following price lists:
#### Memory Specification Price

| Configuration Type | Database Type | Instance Specification | QPS in Counts/Second | Monthly Discount Price (in CNY/Month) | Tier 1 price for pay by usage mode (0-4 days) (in CNY/Hour) | Tier 2 price for pay by usage mode (4-15 days) (in CNY/Hour) | Tier 3 price for pay by usage mode (above 15 days) (in CNY/Hour) |
|:--:|:--:|:--:|:--:|:--:|:--:|:--:|:--:|
| High IO | MySQL instance | 1,000 MB MEM | 1,000 | 175 | 0.49 | 0.37 | 0.25 |
| High IO | MySQL instance | 2,000 MB MEM | 2,400 | 350 | 0.98 | 0.73 | 0.49 |
| High IO | MySQL instance | 4,000 MB MEM | 4,400 | 699 | 1.95 | 1.46 | 0.98 |
| High IO | MySQL instance | 8,000 MB MEM | 7,200 | 1,397 | 3.89 | 2.92 | 1.95 |
| High IO | MySQL instance | 16,000 MB MEM | 18,000 | 2,794 | 7.77 | 5.83 | 3.89 |
| High IO | MySQL instance | 32,000MB MEM | 25,000 | 5,588 | 15.53 | 11.65 | 7.77 |
| High IO | MySQL instance | 64,000 MB MEM | 37,689 | 11,175 | 31.05 | 23.29 | 15.53 |
| High IO | MySQL instance | 96,000 MB MEM | 40,919 | 14,900 | 41.39 | 31.05 | 20.7 |
| High IO | MySQL instance | 128,000 MB MEM | 61,378 | 22,350 | 62.09 | 46.57 | 31.05 |
| High IO | MySQL instance | 244,000 MB MEM | 122,755 | 44,700 | 124.17 | 93.13 | 62.09 |
| High IO | MySQL instance | 488,000 MB MEM | 245,509 | 89,400 | 248.34 | 186.25 | 124.17 |
| High IO | MySQL read-only instance | 1,000 MB MEM | 1,000 |--| 0.25 | 0.19 | 0.13 |
| High IO | MySQL read-only instance | 2,000 MB MEM | 2,400 |--| 0.49 | 0.37 | 0.25 |
| High IO | MySQL read-only instance | 4,000 MB MEM | 4,400 |--| 0.98 | 0.73 | 0.49 |
| High IO | MySQL read-only instance | 8,000 MB MEM | 7,200 |--| 1.95 | 1.46 | 0.98 |
| High IO | MySQL read-only instance | 16,000 MB MEM | 18,000 |--| 3.89 | 2.92 | 1.95 |
| High IO | MySQL read-only instance | 32,000 MB MEM | 25,000 |--| 7.77 | 5.83 | 3.89 |
| High IO | MySQL read-only instance | 64,000 MB MEM | 37,689 |--| 15.53 | 11.65 | 7.77 |
| High IO | MySQL read-only instance | 96,000 MB MEM | 40,919 |--| 20.7 | 15.53 | 10.35 |
| High IO | MySQL read-only instance | 128,000 MB MEM | 61,378 |--| 31.05 | 23.29 | 15.53 |
| High IO | MySQL read-only instance | 244,000 MB MEM | 122,755 |--| 62.09 | 46.57 | 31.05 |
| High IO | MySQL read-only instance | 488,000 MB MEM | 245,509 |--| 124.17 | 93.13 | 62.09 |

#### Storage Price

| Database Type | Monthly Discount Price (in CNY/GB/Month) | Pay by Usage Price (in CNY/GB/Hour) |
|:--:|:--:|:--:|
| MySQL instance | 1.2 | 0.0033 |
| MySQL read-only instance | 1.2 | 0.0033 |

### North America (Toronto) 
**Instance price formula: Instance price = memory specification price + storage price. Renewal and upgrade of instances with original specifications shall be subject to the new price system.**

Additionally, our new tired price system for pay by usage mode is even preferential for longer users. For details, please refer to the following price lists:
#### Memory Specification Price
| Configuration Type | Database Type | Instance Specification | QPS in Counts/Second | Monthly Discount Price (in CNY/Month) | Tier 1 price for pay by usage mode (0-4 days) (in CNY/Hour) | Tier 2 price for pay by usage mode (4-15 days) (in CNY/Hour) | Tier 3 price for pay by usage mode (above 15 days) (in CNY/Hour) |
|:--:|:--:|:--:|:--:|:--:|:--:|:--:|:--:|
| High IO | MySQL instance | 360 MB MEM | 120 | 66 | 0.18 | 0.14 | 0.09 |
| High IO | MySQL instance | 1,000 MB MEM | 1,000 | 183 | 0.51 | 0.38 | 0.25 |
| High IO | MySQL instance | 2,000 MB MEM | 2,400 | 365 | 1.01 | 0.76 | 0.51 |
| High IO | MySQL instance | 4,000 MB MEM | 4,400 | 729 | 2.02 | 1.52 | 1.01 |
| High IO | MySQL instance | 8,000 MB MEM | 7,200 | 1,458 | 4.05 | 3.04 | 2.02 |
| High IO | MySQL instance | 12,000 MB MEM | 15,000 | 2,186 | 6.07 | 4.55 | 3.04 |
| High IO | MySQL instance | 16,000 MB MEM | 18,000 | 2,915 | 8.10 | 6.07 | 4.05 |
| High IO | MySQL instance | 24,000 MB MEM | 23,000 | 4,372 | 12.14 | 9.11 | 6.07 |
| High IO | MySQL instance | 48,000 MB MEM | 37,000 | 8,744 | 24.29 | 18.22 | 12.14 |

#### Storage Price

| Database Type | Monthly Discount Price (in CNY/GB/Month) | Pay by Usage Price (in CNY/GB/Hour) |
|:--:|:--:|:--:|
| MySQL instance | 1.2 | 0.0033 |

## Exceeding the Instance Disk Capacity Limit
To ensure your business operation, please upgrade the database instance specification or purchase further disk storage when your disk is going to run out of space.
Instance will be locked and read-only if the storage data exceeds the instance limit. You can remove the read-only status by **expanding the capacity or deleting some database tables on the console**.
To avoid repeated triggering of locked status of the database, the locked status will be removed for restoring normal read/write functions only when the instance's free space is above 20% or more than 50 GB (whichever is met first).

## Synchronization Traffic Fee from Disaster Recovery Instance
During the promotion period, disaster recovery instance synchronization traffic of CDB for MySQL is free of charge.
Charges for commercialized use will be announced later.
