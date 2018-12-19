## Billing Method

COS is a postpaid service which charges based on your actual usage amount. The bill for the current month will be generated and processed between the 3rd and 5th day of the next month. The bills for COS include Standard Storage Bill, Low-frequency Storage Bill and Nearline Storage Bill. 

* COS Standard Storage Monthly Bill consists of three items:

**Storage Fee** + **Traffic Fee** + **Request Fee**

* COS Low-frequency Storage Monthly Bill consists of five items:

**Storage Fee** + **Traffic Fee** + **Request Fee** + **Data Reading Fee** + **Early Deletion Fee** 

* COS Nearline Storage Monthly Bill consists of five items:

**Storage Fee** + **Traffic Fee** + **Request Fee** + **Data Reading Fee** + **Early Deletion Fee** 

*Note: You can use the COS Fee Calculator in the Product Introduction page to estimate your charges and plan your budget in advance.*

## Storage Fee

Storage Fee is charged based on your monthly average storage usage. The formula for calculating monthly average storage usage is shown below:

**Monthly average storage usage** = The sum of **daily average storage usage** of the month ÷  **Number of days in the month**,

**Daily average storage usage** = The sum of **hourly average storage usage** of the day ÷ **24 hours**,

Storage fee is charged in a tiered method. Fee for storage that exceeds the current tier will be calculated according to the unit price of the next tier. The unit price goes down as you use more storage.

| Type  | Standard Storage  |  Low-frequency Storage  |  Nearline Storage |
| ------------ | ------------ | ------- | -------- |
| Storage fee | 0 GB - 50 GB------0 CNY/GB (free allowance)</br> Above 50 GB ------- 0.13 CNY/GB|   0.1 CNY/GB | 0.06 CNY/GB |
| Minimum storage size | None | 64 KB | 64 KB |

*Note: The storage fee for COS has been adjusted in January, 2017. Bills starting from January will be calculated according to the new prices*
*Note: The minimum storage unit for Low-frequency Storage and Nearline Storage is 64 KB, which means the storage for storing a file smaller than 64 KB will be considered as 64 KB, and storage fee will be calculated accordingly.* 
  
## Traffic Fee

Traffic fee is charged in a tiered method. Fee for traffic that exceeds the current tier will be calculated according to the unit price of the next tier. The unit price goes down as you use more traffic.

| Traffic type    | Definition              | Standard Storage      | Low-frequency Storage      | Nearline Storage        |
| ------- | ----------------------------- | -------------- | -------------- | --------- |
| Inbound traffic     | Data is transmitted into COS                      | Free  | Free     | Free      |
| Private network traffic</br> (same region)  | Traffic between COS and </br>other Tencent Cloud products (not including CDN)     | Free             | Free    | Free  |
| CDN back-to-origin traffic | Back-to-origin traffic generated when </br>accessing COS CDN via Tencent Cloud CDN | 0 GB - 10 GB -- 0 CNY/GB </br>  Above 10 GB -- 0.15 CNY/GB |  0.15 CNY/GB  |     0.15 CNY/GB    |  
| Public network outbound traffic   | IDC traffic generated when</br> accessing COS through public network        | 0 GB - 10 GB -- 0 CNY/GB </br>  10 GB - 500 GB -- 0.64 CNY/GB </br>  Above 500 GB -- 0.6 CNY/GB | 0 GB - 500 GB -- 0.64 CNY/GB </br>  Above 500 GB -- 0.6 CNY/GB | 0 GB - 500 GB -- 0.64 CNY/GB </br>  Above 500 GB -- 0.6 yuan/GB |

*Note: Traffic delivered to user terminals through CDN is not accounted as COS fee. Such charges are calculated according to CDN pricing standard. Refer to [CDN Pricing](http://cloud.tencent.com/doc/product/228/%E8%AE%A1%E8%B4%B9%E8%AF%B4%E6%98%8E) for details.*

**Comparison between the prices of the two COS data transmission methods**

Customers can either choose to let users access the files stored at COS origin server directly through public network BGP bandwidth, or configure acceleration for the files using Tencent Cloud CDN and let terminals access the files via acceleration nodes that have been deployed across the country by CDN.

The comparison between the two methods is shown below. Customers may choose which one to use according to their business demands:



| Transmission method        | Advantage                                       | Disadvantage                                       |
| ----------- | ---------------------------------------- | ---------------------------------------- |
| Access COS directly through public network | This methods provides a choice for customers who don't wish to use Tencent Cloud CDN in their business structure for acceleration, in which case they can use this method to transmit data to the public network directly from COS.  | High cost (0.64 yuan/GB), and speed is slower than using CDN acceleration (users will need to access where the COS origin server is located via public network, from their current locations).  |
| Access COS through CDN  | low cost. CDN acceleration traffic fee + CDN back-to-origin traffic fee. Maximum cost is 0.34 yuan/GB + 0.15 yuan/GB = 0.49 yuan/G. In addition, CDN cache hit rate will also be taken into account. There will be no CDN back-to-origin traffic (0.15 yuan/GB) if requests successfully hit cache when accessing CDN.  |                                          |
|             | Fast access. Users are able to access files that are cached on the nearest CDN node.            | None                                        |

## Request Fee

Operations against COS (by using Web console or Restful API) are both considered calling APIs. The fee for calling COS APIs is calculated based on number of requests. The first 10,000 requests within one billing cycle are free.

| Request type                 | Standard Storage        | Low-frequency Storage        |  Nearline Storage        |
| -------------------- | ---------- | --------- |  --------- |
| Read request (GET)             | 0 - 1,000,000 times ------- 0 yuan/10,000 times </br> Above 1,000,000 times ------- 0.01 yuan/10,000 times   |  0.05 yuan/10,000 times  |  0.06 yuan/10,000 times  |
|  Write request (PUT/POST/DELETE)    | 0 - 100,000 times -------0 yuan/10,000 times </br> Above 100,000 times ------- 0.01 yuan/10,000 times |  0.5 yuan/10,000 times  |  0.6 yuan/10,000 times  |

## Data Reading Fee

Low-frequency Storage and Nearline Storage will charge data reading fees. The volume of read data is usually the total outbound traffic (private network outbound traffic, IDC outbound traffic, CDN back-to-origin traffic).

| Type                 |  Standard Storage        |  Low-frequency Storage        |  Nearline Storage        |
| --------------------| --------- | --------- |  --------- |
| Data read             |  None  |  0.02 yuan/GB  |  0.06 yuan/GB  |


## Data Early Deletion Fee

The minimum storage time is 30 days for Low-frequency Storage and 60 days for Nearline Storage. Deleting, overwriting or moving data stored in Low-frequency Storage or Nearline Storage to another storage level before the data has been stored for the minimum number of days, are all considered early deletion. In this case, the remaining fee for storing the data for the rest of days will still be charged. For example, if you delete 10G of low-frequency data after it has been stored for only 10 days, we will still charge the storage fee for storing 10G of data for 30 days.

| Type                 |  Standard Storage        | Low-frequency Storage        |  Nearline Storage        |
| -------------------- | --------- | --------- |  --------- |
| Data early deletion             |  None  |   30 days  |  60 days  |

*Note: Modifying Object custom Header, modifying Object privilege and appending upload are not considered early deletion.


