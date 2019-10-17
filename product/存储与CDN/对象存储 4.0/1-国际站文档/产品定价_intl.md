## Billing Method
COS Standard is billed monthly, postpaid based on actual usage. The billing is done between the third and fifth day of each month. During this time, the previous month's fees will be calculated to generate the bill.
## Billing Information
Bills for COS are generated monthly. The regions supported in the Chinese mainland include Beijing, Shanghai, Guangzhou, and Chengdu. For more information on supported regions, please see [Available Regions](/doc/product/436/6224).
Different Tencent Cloud products within the same region access each other over a private network by default and no traffic fees are charged for these connections. For this reason, we recommend selecting the same region when purchasing different Tencent Cloud products to generate cost savings.
> To determine whether the private network is used for CVM connections to COS, for example:
> Perform a ping on the COS domain name from CVM. If a private IP is returned, it means the CVM and COS connect to each other over the private network. Otherwise, the connection is made over the public network.
> Generally, a private IP address takes the form of `10.*.*.*` or `100.*.*.*`.

### Storage Fees
**Note:** 

> - Billing unit for storage fees: USD/GB/month

> - **Average storage per day = the total of the average storage at each hour of the day ÷ 24 hours**
>    **Storage per month = the total of average storage per day ÷ number of days in that month** 
> - COS Infrequent Access is billed at a minimum of 64 KB. This means when a file is smaller than 64 KB, the storage fee is charged at 64 KB.
>   The storage period for objects using COS Infrequent Access is a minimum of 30 days. If an object is deleted or transferred to another storage type before the end of the 30-day period, the storage fee for that object is still calculated as a 30-day period.

|     | Mainland China | Hong Kong | Singapore | Frankfurt | Toronto | Mumbai |Seoul | Silicon Valley | Virginia | Bangkok | Moscow | Tokyo |
| :--------: | :-----------: | :-------: | :-------: | :-------: | :-----: | ------ | ------ | ------ | ------ | ------ | ------ |-- |
|     COS Standard      |     0.024      |   0.022   |   0.022   |   0.02    |  0.02   | 0.024 |0.024|0.024|0.02|0.024|0.024|0.0200|
| COS Infrequent Access |     0.018      |   0.016   |   0.016   |   0.014   |  0.014  | 0.018 |0.018|0.018|0.014|0.018|0.018|0.0140|

### Request Fee
**Note:**

> - Billing unit for request fees: USD/10,000 requests
> - The request fee is billed at a minimum of 10,000 requests. If the number of requests is less than 10,000, the request fees are billed at the rate for 10,000 requests. 

|      | Mainland China | Hong Kong | Singapore | Frankfurt | Toronto | Mumbai |Seoul | Silicon Valley | Virginia | Bangkok | Moscow |Tokyo |
| :-----: | :------------: | :-------: | :-------: | :-------: | :-----: | ------- | ------- | ------- | ------- | ------ | ------ |-- |
|     COS Standard      |     0.002      |   0.002   |   0.003   |   0.002   |  0.002  |0.003|0.002|0.002|0.002|0.002|0.002|0.0020|
| COS Infrequent Access |      0.01      |   0.01    |   0.015   |   0.01    |  0.01   |0.015|0.01|0.01|0.01|0.01|0.01|0.0100|

### Data Retrieval Fees
**Note:** 
> - Billing unit for data retrieval fees: USD/GB

|     | Mainland China | Hong Kong | Singapore | Frankfurt | Toronto | Mumbai |Seoul | Silicon Valley | Virginia | Bangkok | Moscow |Tokyo |
| :------: | :------------: | :-------: | :-------: | :-------: | :-----: | ------- | ------- | ------ | ------ | ----- | ----- |-- |
|     COS Standard      |       0        |     0     |     0     |     0     |    0    |0|0|0|0|0|0|0|
| COS Infrequent Access |     0.002      |   0.002   |   0.003   |   0.002   |  0.002  |0.003|0.002|0.002|0.002|0.003|0.002|0.0020|

### Traffic Fees
**Note:** 
> - Billing unit for traffic fees: USD/GB
> - Traffic fees are priced at the same rate for the two storage types.

|        | Mainland China | Hong Kong | Singapore | Frankfurt | Toronto | Mumbai |Seoul | Silicon Valley | Virginia | Bangkok | Moscow |Tokyo |
| :---------: | :------------: | :-------: | :-------: | :-------: | :-----: | ------- | ----- | ------- | ----- | ------ | ------ |- |
| Downstream traffic in the public network |      0.1       |   0.08    |   0.072   |   0.07    |  0.07   |0.1|0.12|0.07|0.07|0.12|0.07|0.0700|
| CDN origin-pull traffic  |      0.02      |   0.08    |   0.072   |   0.07    |  0.07   |0.1|0.12|0.07|0.07|0.12|0.07|0.0700|
|  Cross-region replication traffic     |      0.05      |   0.08    |   0.072   |   0.07    |  0.07   |0.1|0.12|0.07|0.07|0.12|0.07|0.0700|
