## 1 Table expansion
Expansion in Cloud Memcached includes storage expansion, interface expansion and port expansion.
Storage expansion:
Cloud Memcached automatically reserves about 20% of the space for each business each day as a data growth buffer. For example, if space to used for a table space is 80 GB, it will allocate 96 GB to the table. Submit a ticket to apply for storage expansion if the daily growth of table data exceeds 20%. Capacity expansion in Cloud Memcached is a data migration process, which does not affect the hit rate. 
Interface/port expansion:
Submit a ticket to apply for interface/port expansion.

## 2 Table capacity reduction
Table capacity reduction refers to the reduction of table-occupied space, that is, storage capacity reduction. Because of the need to reserve buffer space, the table utilization after capacity reduction will not exceed 80%. The table capacity is reduced by a minimum of 1 GB decrement. A reduction that can cause a utilization above 80% is not allowed.
Currently, Cloud Memcached tables do not support automatic capacity reduction. To implement capacity reduction, you need to submit a ticket for an application. Our OPS personnel will implement capacity reduction for you.
Before your application, the service is still charged based on the originally occupied space (including the buffer space expanded automatically from the original used space) during peak hours.
## 3 Automatic data clean-up
Note:
(1) The data cannot be restored after being cleared. Please confirm that the data in the table has been backed up or is no longer used before clearing it.
(2) For each application, a maximum of 50 GB space occupied by the table can be cleared on a daily basis. If the occupied space exceeds 50 GB, contact us for technical support by submitting a ticket.

On the Cloud Memcached management view page in Console, click the "Clear" button next to the table to be cleaned up. After your confirmation for the operation, the cleaning begins at backend. When the cleaning is completed, a message indicating the successful cleaning will appear.

![](//qzonestyle.gtimg.cn/qzone/vas/opensns/res/img/NoSQLClearTable.jpg)

## 4 Return table
Note:
(1) The table cannot be restored after being returned. Please confirm that the data in the table has been backed up or is no longer used before returning the table.

On the Cloud Memcached management view page in Console, check the table to be returned, and click the "Return Selected Table" button. After your click the "Submit for Return" button, the data clean-up begins and the table is deleted at backend.

![](//qzonestyle.gtimg.cn/qzone/vas/opensns/res/img/NoSQLDeleteTable.jpg)

## 5 Enable "expire"
1. To use the expire feature, you first need to enable it for the corresponding CMEM instance in Tencent Cloud console.
![](https://mc.qcloudimg.com/static/img/5fe836860fcf211c0984d84946735d0e/cmem.png)
2. After this feature is enabled, set the expiration time for the key in the code. For more information, please see the settings of memcached in various languages.
3. Note: The key set before "expire" is enabled will not automatically expire.

## 6 View monitoring information

Click "Monitoring View" button on the left of NoSQL management page to enter the monitoring information page.

For more information about the metrics, please see [Cloud Memcached Monitoring Metrics](/doc/product/248/云缓存Memcached监控指标说明)

## 7 API "Check Operating Data"
For more information, please see API "Check Operating Data of Cloud Memcached".

## 8 Data rollback
Contact us by submitting a ticket.

## 9 Connection diagnostics
For more information, please see: [Cloud Memcached Connection Diagnostics](https://cloud.tencent.com/doc/product/241/3247)
