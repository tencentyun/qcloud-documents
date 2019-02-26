Tencent Cloud CDB for MySQL currently supports two payment modes for instances: monthly or annual prepaid mode and postpaid mode (Before making any purchase in the postpaid mode, it is required to make an identity verification. For more information about the identity verification, please see the <a href="https://cloud.tencent.com/document/product/378/3629" target="_blank">Identity Verification Guide</a>).  
The monthly or annual payment is a prepaid billing mode. For more information, please see <a href="https://cloud.tencent.com/document/product/555/9618" target="_blank">Prepaid Billing Description</a>.  
For more information about postpaid billing mode, please see <a href="https://cloud.tencent.com/document/product/555/9617" target="_blank">Postpaid Billing Description</a>.  
For information about the billing process, please see <a href="https://cloud.tencent.com/document/product/555/7437" target="_blank">Billing Process Description</a>.
## Tiered Prices for the Postpaid Mode
Starting from July 15, 2016, tiered prices in the postpaid mode is available to CDB for MySQL. The longer the use time, the cheaper the price.
Depending on the use time, the prices of the postpaid mode are divided into three steps:
- 0-4 days (within 4*24h): The postpaid Step 1 will apply.
- 4-15 days (from 4*24h to 15*24h): The postpaid Step 2 will apply.
- Over 15 days (starting from 15*24h): The postpaid Step 3 will apply.

For information about specific prices, please see "[Prices for Different Regions](#document_price)".
<span id="document_price"></span>
## Prices for Different Regions

#### 1. North China (Beijing), South China (Guangzhou), East China (Shanghai) and Southwest (Chengdu)
Since July 11, 2016, for regions like North China (Beijing), South China (Guangzhou), East China (Shanghai) and Southwest (Shanghai), CDB for MySQL has supported only the separate billing mode for the sales of memories and disks, providing users with flexible options.
**Instance price calculation formula: Instance price = Memory specification fee + Storage space fee. For renewal and upgrade of instances with the original specification, please refer to the new price system standard.**
Meanwhile, with regard to the new tiered postpaid prices, the longer the use time, the cheaper the price. For more information, please refer to the list of prices:

| Configuration Type | Database Type | Instance Specification | QPS in Counts/Second | Discounted Monthly Price (CNY/Month) | Postpaid Price Step 1 (0-4 days) (CNY/Hour) | Postpaid Price Step 2 (4-15 days) (CNY/Hour) | Postpaid Price Step 3 (above 15 days) (CNY/Hour) |
|:--:|:--:|:--:|:--:|:--:|:--:|:--:|:--:|
| High IO | MySQL<br>Instance | 1,000 MB MEM | 1,000 | 102 | 0.29 | 0.22 | 0.15 |
| High IO | MySQL<br>Instance | 2,000 MB MEM | 2,400 | 204 | 0.57 | 0.43 | 0.29 |
| High IO | MySQL<br>Instance | 4,000 MB MEM | 4,400 | 408 | 1.14 | 0.85 | 0.57 |
| High IO | MySQL<br>Instance | 8,000 MB MEM | 7,200 | 816 | 2.27 | 1.70 | 1.14 |
| High IO | MySQL<br>Instance | 12,000MB MEM | 7,200 | 1,224 | 3.40 | 2.55 | 1.70 |
| High IO | MySQL<br>Instance | 16,000MB MEM | 18,000 | 1,632 | 4.54 | 3.40 | 2.27 |
| High IO | MySQL<br>Instance | 32,000MB MEM | 25,000 | 3,264 | 9.07 | 6.80 | 4.54 |
| High IO | MySQL<br>Instance | 64,000MB MEM | 37,689 | 6,528 | 18.14 | 13.60 | 9.07 |
| High IO | MySQL<br>Instance | 96,000MB MEM | 40,919 | 8,684 | 24.13 | 18.10 | 12.07 |
| High IO | MySQL<br>Instance | 128,000MB MEM | 61,378 | 13,056 | 36.27 | 27.20 | 18.14 |
| High IO | MySQL<br>Instance | 244,000MB MEM | 122,755 | 24,888 | 69.14 | 51.85 | 34.57 |
| High IO | MySQL<br>Instance | 488,000MB MEM | 245,509 | 49,776 | 138.27 | 103.70 | 69.14 |
| High IO | MySQL<br>Read-only Instance | 1,000 MB MEM | 1,000 | - | 0.15 | 0.11 | 0.08 |
| High IO | MySQL<br>Read-only Instance | 2,000 MB MEM | 2,400 | - | 0.29 | 0.22 | 0.15 |
| High IO | MySQL<br>Read-only Instance | 4,000 MB MEM | 4,400 | - | 0.57 | 0.43 | 0.29 |
| High IO | MySQL<br>Read-only Instance | 8,000 MB MEM | 7,200 | - | 1.14 | 0.85 | 0.57 |
| High IO | MySQL<br>Read-only Instance | 16,000 MB MEM | 18,000 | - | 2.27 | 1.70 | 1.14 |
| High IO | MySQL<br>Read-only Instance | 32,000 MB MEM | 25,000 | - | 4.54 | 3.40 | 2.27 |
| High IO | MySQL<br>Read-only Instance | 64,000 MB MEM | 37,689 | - | 9.07 | 6.80 | 4.54 |
| High IO | MySQL<br>Read-only Instance | 96,000 MB MEM | 40,919 | - | 12.07 | 9.05 | 6.80 |
| High IO | MySQL<br>Read-only Instance | 128,000 MB MEM | 61,378 | - | 18.14 | 13.60 | 9.07 |
| High IO | MySQL<br>Read-only Instance | 244,000 MB MEM | 122,755 | - | 34.57 | 25.93 | 17.29 |
| High IO | MySQL<br>Read-only Instance | 488,000 MB MEM | 245,509 | - | 69.14 | 51.85 | 34.57 |


 Storage prices:
 
| Database Type | Discounted Monthly Price (CNY/GB/Month) | Postpaid Price (CNY/GB/Hour) |
|:--:|:--:|:--:|
| MySQL Instance | 0.72 | 0.0022 |
| MySQL Read-only Instance | 0.72 | 0.0022 |


#### 2. Southeast Asia (Hong Kong)
**Instance price calculation formula: Instance price = Memory specification fee + Storage space fee. For renewal and upgrade of instances with the original specification, please refer to the new price system standard.**
Meanwhile, with regard to the new tiered postpaid prices, the longer the use time, the cheaper the price. For more information, please refer to the list of prices:

| Configuration Type | Database Type | Instance Specification | QPS in Counts/Second | Discounted Monthly Price (CNY/Month) | Postpaid Price Step 1 (0-4 days) (CNY/Hour) | Postpaid Price Step 2 (4-15 days) (CNY/Hour) | Postpaid Price Step 3 (above 15 days) (CNY/Hour) |
|:--:|:--:|:--:|:--:|:--:|:--:|:--:|:--:|
| High IO | MySQL<br>Instance | 360 MB MEM | 120 | 62 | 0.17 | 0.13 | 0.09 |
| High IO | MySQL<br>Instance | 1,000 MB MEM | 1,000 | 171 | 0.47 | 0.36 | 0.24 |
| High IO | MySQL<br>Instance | 2,000 MB MEM | 2,400 | 342 | 0.95 | 0.71 | 0.47 |
| High IO | MySQL<br>Instance | 4,000 MB MEM | 4,400 | 684 | 1.90 | 1.42 | 0.95 |
| High IO | MySQL<br>Instance | 8,000 MB MEM | 7,200 | 1,367 | 3.80 | 2.85 | 1.90 |
| High IO | MySQL<br>Instance | 12,000 MB MEM | 15,000 | 2,050 | 5.69 | 4.27 | 2.85 |
| High IO | MySQL<br>Instance | 16,000 MB MEM | 18,000 | 2,734 | 7.59 | 5.69 | 3.80 |
| High IO | MySQL<br>Instance | 24,000 MB MEM | 23,000 | 4,100 | 11.39 | 8.54 | 5.69 |
| High IO | MySQL<br>Instance | 48,000 MB MEM | 37,000 | 8,200 | 22.78 | 17.08 | 11.39 |

Storage prices:

| Database Type | Discounted Monthly Price (CNY/GB/Month) | Postpaid Price (CNY/GB/Hour) |
|:--:|:--:|:--:|
| MySQL Instance | 1.2 | 0.0033 |

#### 3. Southeast Asia (Singapore)
**Instance price calculation formula: Instance price = Memory specification fee + Storage space fee. For renewal and upgrade of instances with the original specification, please refer to the new price system standard.**
Meanwhile, with regard to the new tiered postpaid prices, the longer the use time, the cheaper the price. For more information, please refer to the list of prices:

| Configuration Type | Database Type | Instance Specification | QPS in Counts/Second | Discounted Monthly Price (CNY/Month) | Postpaid Price Step 1 (0-4 days) (CNY/Hour) | Postpaid Price Step 2 (4-15 days) (CNY/Hour) | Postpaid Price Step 3 (above 15 days) (CNY/Hour) |
|:--:|:--:|:--:|:--:|:--:|:--:|:--:|:--:|
| High IO | MySQL<br>Instance | 1,000 MB MEM | 1,000 | 175 | 0.49 | 0.37 | 0.25 |
| High IO | MySQL<br>Instance | 2,000 MB MEM | 2,400 | 350 | 0.98 | 0.73 | 0.49 |
| High IO | MySQL<br>Instance | 4,000 MB MEM | 4,400 | 699 | 1.95 | 1.46 | 0.98 |
| High IO | MySQL<br>Instance | 8,000 MB MEM | 7,200 | 1,397 | 3.89 | 2.92 | 1.95 |
| High IO | MySQL<br>Instance | 16,000 MB MEM | 18,000 | 2,794 | 7.77 | 5.83 | 3.89 |
| High IO | MySQL<br>Instance | 32,000MB MEM | 25,000 | 5,588 | 15.53 | 11.65 | 7.77 |
| High IO | MySQL<br>Instance | 64,000MB MEM | 37,689 | 11,175 | 31.05 | 23.29 | 15.53 |
| High IO | MySQL<br>Instance | 96,000MB MEM | 40,919 | 14,900 | 41.39 | 31.05 | 20.7 |
| High IO | MySQL<br>Instance | 128,000 MB MEM | 61,378 | 22,350 | 62.09 | 46.57 | 31.05 |
| High IO | MySQL<br>Instance | 244,000MB MEM | 122,755 | 44,700 | 124.17 | 93.13 | 62.09 |
| High IO | MySQL<br>Instance | 488,000MB MEM | 245,509 | 89,400 | 248.34 | 186.25 | 124.17 |
| High IO | MySQL<br>Read-only Instance | 1,000 MB MEM | 1,000 | - | 0.25 | 0.19 | 0.13 |
| High IO | MySQL<br>Read-only Instance | 2,000 MB MEM | 2,400 | - | 0.49 | 0.37 | 0.25 |
| High IO | MySQL<br>Read-only Instance | 4,000 MB MEM | 4,400 | - | 0.98 | 0.73 | 0.49 |
| High IO | MySQL<br>Read-only Instance | 8,000 MB MEM | 7,200 | - | 1.95 | 1.46 | 0.98 |
| High IO | MySQLv<br>Read-only Instance | 16,000 MB MEM | 18,000 | - | 3.89 | 2.92 | 1.95 |
| High IO | MySQL<br>Read-only Instance | 32,000 MB MEM | 25,000 | - | 7.77 | 5.83 | 3.89 |
| High IO | MySQL<br>Read-only Instance | 64,000 MB MEM | 37,689 | - | 15.53 | 11.65 | 7.77 |
| High IO | MySQL<br>Read-only Instance | 96,000 MB MEM | 40,919 | - | 20.7 | 15.53 | 10.35 |
| High IO | MySQL<br>Read-only Instance | 128,000 MB MEM | 61,378 | - | 31.05 | 23.29 | 15.53 |
| High IO | MySQL<br>Read-only Instance | 244,000 MB MEM | 122,755 | - | 62.09 | 46.57 | 31.05 |
| High IO | MySQL<br>Read-only Instance | 488,000 MB MEM | 245,509 | - | 124.17 | 93.13 | 62.09 |

Storage prices:

| Database Type | Discounted Monthly Price (CNY/GB/Month) | Postpaid Price (CNY/GB/Hour) |
|:--:|:--:|:--:|
| MySQL Instance | 1.2 | 0.0033 |
| MySQL Read Only Instance | - | 0.0033 |

#### 4. North America (Toronto)
**Instance price calculation formula: Instance price = Memory specification fee + Storage space fee. For renewal and upgrade of instances with the original specification, please refer to the new price system standard.**
Meanwhile, with regard to the new tiered postpaid prices, the longer the use time, the cheaper the price. For more information, please refer to the list of prices:

| Configuration Type | Database Type | Instance Specification | QPS in Counts/Second | Discounted Monthly Price (CNY/Month) | Postpaid Price Step 1 (0-4 days) (CNY/Hour) | Postpaid Price Step 2 (4-15 days) (CNY/Hour) | Postpaid Price Step 3 (above 15 days) (CNY/Hour) |
|:--:|:--:|:--:|:--:|:--:|:--:|:--:|:--:|
| High IO | MySQL<br>Instance | 360 MB MEM | 120 | 66 | 0.18 | 0.14 | 0.09 |
| High IO | MySQL<br>Instance | 1,000 MB MEM | 1,000 | 183 | 0.51 | 0.38 | 0.25 |
| High IO | MySQL<br>Instance | 2,000 MB MEM | 2,400 | 365 | 1.01 | 0.76 | 0.51 |
| High IO | MySQL<br>Instance | 4,000 MB MEM | 4,400 | 729 | 2.02 | 1.52 | 1.01 |
| High IO | MySQL<br>Instance | 8,000 MB MEM | 7,200 | 1,458 | 4.05 | 3.04 | 2.02 |
| High IO | MySQL<br>Instance | 12,000 MB MEM | 15,000 | 2,186 | 6.07 | 4.55 | 3.04 |
| High IO | MySQL<br>Instance | 16,000 MB MEM | 18,000 | 2,915 | 8.10 | 6.07 | 4.05 |
| High IO | MySQL<br>Instance | 24,000 MB MEM | 23,000 | 4,372 | 12.14 | 9.11 | 6.07 |
| High IO | MySQL<br>Instance | 48,000 MB MEM | 37,000 | 8,744 | 24.29 | 18.22 | 12.14 |

Storage prices:

| Database Type | Discounted Monthly Price (CNY/GB/Month) | Postpaid Price (CNY/GB/Hour) |
|:--:|:--:|:--:|
| MySQL Instance | 1.2 | 0.0033 |

#### 5. Western U.S. (Silicon Valley)
**Instance price calculation formula: Instance price = Memory specification fee + Storage space fee. For renewal and upgrade of instances with the original specification, please refer to the new price system standard.**
Meanwhile, with regard to the new tiered postpaid prices, the longer the use time, the cheaper the price. For more information, please refer to the list of prices:

| Configuration Type | Database Type | Instance Specification | QPS in Counts/Second | Discounted Monthly Price (CNY/Month) | Postpaid Price Step 1 (0-4 days) (CNY/Hour) | Postpaid Price Step 2 (4-15 days) (CNY/Hour) | Postpaid Price Step 3 (above 15 days) (CNY/Hour) |
|:--:|:--:|:--:|:--:|:--:|:--:|:--:|:--:|
| High IO | MySQL<br> Instance | 1,000 MB MEM | 1,000 | 178 | 0.50 | 0.38 | 0.25 |
| High IO | MySQL<br> Instance | 2,000 MB MEM | 2,400 | 356 | 1.00 | 0.76 | 0.50 |
| High IO | MySQL<br> Instance | 4,000 MB MEM | 4,400 | 712 | 2.00 | 1.52 | 1.00 |
| High IO | MySQL<br> Instance | 8,000 MB MEM | 7,200 | 1,424 | 4.00 | 3.04 | 2.00 |
| High IO | MySQL<br> Instance | 16,000 MB MEM | 18,000 | 2,848 | 8.00 | 6.08 | 4.00 |
| High IO | MySQL<br> Instance | 32,000 MB MEM | 25,000 | 5,696 | 16.00 | 12.16 | 8.00 |
| High IO | MySQL<br> Instance | 64,000 MB MEM | 37,689 | 11,392 | 32.00 | 24.32 | 16.00 |
| High IO | MySQL<br> Instance | 96,000 MB MEM | 40,919 | 17,088 | 48.00 | 36.48 | 24.00 |
| High IO | MySQL<br> Instance | 128,000 MB MEM | 61,378 | 22,784 | 64.00 | 48.64 | 32.00 |
| High IO | MySQL<br> Instance | 244,000 MB MEM | 122,755 | 43,432 | 122.00 | 92.72 | 61.00 |
| High IO | MySQL<br> Instance | 488,000 MB MEM | 245,509 | 86,864 | 244.00 | 185.44 | 122.00 |
| High IO | MySQL<br> Read-only Instance | 1,000 MB MEM | 1,000 | - | 0.25 | 0.19 | 0.13 |
| High IO | MySQL<br> Read-only Instance | 2,000 MB MEM | 2,400 | - | 0.50 | 0.37 | 0.25 |
| High IO | MySQL<br> Read-only Instance | 4,000 MB MEM | 4,400 | - | 1.00 | 0.76 | 0.50 |
| High IO | MySQL<br> Read-only Instance | 8,000 MB MEM | 7,200 | - | 2.00 | 1.52 | 1.00 |
| High IO | MySQL<br> Read-only Instance | 16,000 MB MEM | 18,000 | - | 4.00 | 3.04 | 2.00 |
| High IO | MySQL<br> Read-only Instance | 32,000 MB MEM | 25,000 | - | 8.00 | 6.08 | 4.00 |
| High IO | MySQL<br> Read-only Instance | 64,000 MB MEM | 37,689 | - | 16.00 | 12.16 | 8.00 |
| High IO | MySQL<br> Read-only Instance | 96,000 MB MEM | 40,919 | - | 24.00 | 18.24 | 12.00 |
| High IO | MySQL<br> Read-only Instance | 128,000 MB MEM | 61,378 | - | 32.00 | 24.32 | 16.00 |
| High IO | MySQL<br> Read-only Instance | 244,000 MB MEM | 122,755 | - | 61.00 | 46.36 | 31.05 |
| High IO | MySQL<br> Read-only Instance | 488,000 MB MEM | 245,509 | - | 122.00 | 97.72 | 61.00 |

Storage prices:

| Database Type | Discounted Monthly Price (CNY/GB/Month) | Postpaid Price (CNY/GB/Hour) |
|:--:|:--:|:--:|
| MySQL Instance | 0.8 | 0.0022 |
| MySQL Read Only Instance | - | 0.0022 |

## Instance Renewal Management
On the Renewal Management page, a set of functions related to instances are available, including "Batch Resource Renewal", "Set Auto Renewal", "Set Unified Expiration Date" and "Cancel Non-Renewal". For more information, please see <a href="https://cloud.tencent.com/document/product/555/7454" target="_blank">Renewal Management</a>.

## Instance Upgrade Fee
Total upgrade fee=T/30*C, where T is the number of days left before the expiration date of the instance, and C is the difference of monthly prepaid fee between the target configuration and existing configuration.
For example: You have an instance with 1 G MEM and 100 G hard drive (prepaid 174 CNY/Month), and there are 15 days left before expiration. What you need to do is to upgrade this instance to that with 1 G MEM and 200 G hard drive (prepaid 246 CNY/Month). Total upgrade fee = 15/30 * (246-174) = 36 CNY.

>**Note:**
To ensure the normal operation of your business, when the hard disk space almost runs out, please upgrade the database instance specifications or purchase hard disk space. For more information, please see [Upgrade Database Instance Specification](https://cloud.tencent.com/document/product/236/7271).
An instance will be locked and read only if its storage data exceeds the instance limit. You can remove the read-only status by **expanding the capacity or deleting some database tables on the console**.
To avoid repeated triggering of the locked status of the database, the locked status will be removed for restoring normal read/write functions only when the instance's free space is above 20% or more than 50 GB (whichever is met first).

## Synchronization Traffic Fee from Disaster Recovery Instance
During the promotion period, disaster recovery instance synchronization traffic of CDB for MySQL is free of charge. Charges for commercialized use will be announced later.

[2]:	https://cloud.tencent.com/document/product/555/9618
[3]:	https://cloud.tencent.com/document/product/555/9617
[4]:    https://cloud.tencent.com/document/product/555/7437
[5]:    https://buy.cloud.tencent.com/calculator/cdb

