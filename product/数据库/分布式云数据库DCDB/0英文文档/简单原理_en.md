## 1. Horizontal Sharding
Data in DCDB is calculated using ShardKey (a shard field) and a specific hash algorithm, and then stored in the corresponding shard depending on the result.
As shown below:
![](https://mc.qcloudimg.com/static/img/57840ef0e96459693947f66ad9139bf0/image.png)

## 2. Data Aggregation (Consolidation)
When you query data from a DCDB instance, DCDB automatically queries data from each shard and aggregate the result.
![](https://mc.qcloudimg.com/static/img/76ac86ff49af90e8660bf85f9bf5725d/image.png)


## 3. Read-write Separation

A read-only account is used to implement automatic distribution of read request to slave and return the result.

![](https://mc.qcloudimg.com/static/img/e302e114b8de2b6db5883d927893a6e3/image.png)
